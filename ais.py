import random
import math
import numpy as np
import copy
from q import qsort
from test_functions import *
from contextlib import contextmanager
from sys import getrecursionlimit, setrecursionlimit

# -------------------------- Вставьте сгенерированные строки здесь --------------------------
# Сгенерированные строки для вставки:
Ip = 12  # Количество начальных точек (число строк)
sigma = 0.5  # Примерное значение сигма
d = 40  # Процент новых клеток для добавления
K = 100  # Максимальное количество итераций
e = 0.1  # Порог изменения среднего значения популяции
beta = 10  # Коэффициент клонирования
Nc = 5  # Количество клонов на каждую точку
gamma = 10  # Коэффициент мутации
ndim = 15  # Размерность данных (количество столбцов)
percent = 100  # Процент новых клеток
data_array = [[8050.0, 7945.0, 8240.0, 9350.0, 8320.0, 8245.0, 9045.0, 9130.0, 8245, 8820.0, 8925.0, 10610.0, 12350.0, 8245, 8245], [42.0, 43.0, 40.0, 42.0, 50.0, 50.0, 50.0, 51.0, 53.0, 56.0, 57.0, 57.0, 56.0, 52.0, 53.0], [0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0], [140000.0, 146000.0, 140000.0, 132000.0, 123000.0, 120000.0, 146000.0, 112000.0, 126000.0, 97000.0, 100000.0, 105000.0, 110000.0, 114000.0, 114000.0], [1225.0, 1300.0, 1375.0, 1350.0, 1317.25, 1245.0, 1100.25, 1098.0, 1087.75, 987.95, 1007.25, 1023.3, 1037.35, 1045.6, 1059.0], [0.0575, 0.0544, 0.0589, 0.0708, 0.0676, 0.0687, 0.062, 0.0815, 0.076, 0.0909, 0.0893, 0.101, 0.1123, 0.1078, 0.1106], [4.384, 4.2857, 4.1096, 5.7143, 6.8182, 2.439, 21.667, 23.288, 12.5, 23.016, 3.0928, 5.0, 4.7619, 3.6364, 0.0], [0.269185714, 0.213, 0.253971429, 0.294704545, 0.328707317, 0.324041667, 0.282876712, 0.378363095, 0.365041005, 0.5114811, 0.532321667, 0.493815873, 0.543736364, 0.573719298, 0.588140351], [14.13, 14.73, 14.13, 13.33, 12.43, 12.13, 14.73, 11.33, 12.73, 9.83, 10.13, 10.63, 11.13, 11.53, 11.53], [5071.5, 5005.35, 5191.2, 5890.5, 5241.6, 5194.35, 5698.35, 5751.9, 6035.4, 5556.6, 5622.75, 6684.3, 7780.5, 7742.7, 7944.3], [37686.0, 31098.0, 35556.0, 38901.0, 40431.0, 38885.0, 41300.0, 42376.66667, 45995.16667, 49613.66667, 53232.16667, 51850.66667, 59811.0, 65404.0, 67048.0], [1876.455, 1851.9795, 1920.744, 2179.485, 1939.392, 1921.9095, 2108.3895, 2128.203, 2233.098, 2055.942, 2080.4175, 2473.191, 2878.785, 2864.799, 2939.391]]  # Данные для алгоритма (массив)
# ------------------------------------------------------------------------------------------



fffff = AckleyF  # Функция
restrictions = rAckleyF  # Ограничения

# Проверяем размерность каждой точки в data_array
for point in data_array:
    if len(point) != ndim:
        raise ValueError(f"Point {point} does not match the specified ndim = {ndim}.")

# Генерируем начальные ограничения из data_array
restrictions.x = [[min(coord), max(coord)] for coord in zip(*data_array)]

# Дополняем restrictions.x до ndim, если требуется
if len(restrictions.x) < ndim:
    print(f"Extending restrictions.x from {len(restrictions.x)} to {ndim}")
    restrictions.x.extend([[-np.inf, np.inf]] * (ndim - len(restrictions.x)))

#1.2
def generate_init_population(data_array, f, restrictions, ndim):
    """
        Function generates a new population using provided data.

        data_array - input data for initialization,
        f - function,
        restrictions - field limit function,
        ndim - dimension.
    """
    population = []
    populationF = []

    # Проверяем, что каждая строка в data_array имеет нужную размерность
    for point in data_array:
        if len(point) != ndim:
            raise ValueError("Data points in data_array do not match the specified ndim.")
        # Проверяем ограничения и добавляем только допустимые точки
        if all(restrictions.x[j][0] <= point[j] <= restrictions.x[j][1] for j in range(ndim)):
            population.append(point)
            populationF.append(f(point))
        else:
            print(f"Point {point} does not satisfy restrictions and will be skipped.")

    if len(population) == 0:
        raise ValueError("No valid points found in data_array after applying restrictions.")

    return population, populationF


#2.1
def normalize_value(populationF):
    if len(populationF) == 1:
        return populationF
    fx_min = min(populationF)
    fx_max = max(populationF)
    populationF_normalize = [(fx - fx_min) / (fx_max - fx_min) for fx in populationF]
    return populationF_normalize

# 2.2.2 Uniform Cloning
def uniform_cloning(population, Nc):
    """
    Uniformly clones each individual in the population.
    
    Args:
        population: The current population of points.
        Nc: Number of clones for each point.
    
    Returns:
        List of cloned points.
    """
    clones = [[point] * Nc for point in population]
    return clones

def mutation(clones, populationF_normalize, restrictions, gamma):
    """
    Applies mutation to the clones based on normalized function values.
    
    Args:
        clones: List of cloned points.
        populationF_normalize: Normalized fitness values for the population.
        restrictions: Restrictions on the search space.
        gamma: Mutation factor.
    
    Returns:
        Mutated clones.
    """
    new = []
    for i, clone_cells in enumerate(clones):
        new_clone = []
        alpha = (1.0 / gamma) * math.exp(-populationF_normalize[i])
        for cell in clone_cells:
            mutated_cell = []
            for j, coordinate in enumerate(cell):
                while True:
                    if coordinate >= restrictions.x[j][1] - 0.1:
                        N = 0.0
                    else:
                        N = float(np.random.normal(0.01, 0.001))
                    mutated_coordinate = coordinate + alpha * N
                    if restrictions.x[j][0] <= mutated_coordinate <= restrictions.x[j][1]:
                        mutated_cell.append(mutated_coordinate)
                        break
            new_clone.append(mutated_cell)
        new.append(new_clone)
    return new

def f_for_mutants(mutated_clones, f):
    """
    Evaluates the fitness function for each mutated clone.
    
    Args:
        mutated_clones: List of mutated clones (nested list of points).
        f: Fitness function to evaluate.
    
    Returns:
        List of fitness values for each clone.
    """
    mutated_clones_F = []
    for clone_cells in mutated_clones:
        clones_F = []
        for cell in clone_cells:
            clones_F.append(f(cell))  # Вычисляем значение функции f для каждой клетки клона
        mutated_clones_F.append(clones_F)
    return mutated_clones_F

def formatted_output(population, populationF, data_types):
    """
    Форматированный вывод популяции и значений функции.
    
    Args:
        population: Список точек популяции.
        populationF: Значения функции для каждой точки.
        data_types: Описание типов данных.
    """
    print("\nPopulation (Популяция):")
    for i, row in enumerate(population):
        if i < len(data_types):
            formatted_values = [f"{value:.2f}" for value in row]
            print(f"  {data_types[i]}: {formatted_values}")
        else:
            print(f"  Дополнительный параметр {i + 1 - len(data_types)}: {row}")

    print("\nPopulationF (Значения функции):")
    for i, data_type in enumerate(data_types):
        if i < len(populationF):
            print(f"  {data_type}: {populationF[i]:.2f}")
        else:
            print(f"  Дополнительный параметр {i + 1 - len(populationF)}: {populationF[i]}")




data_types = [
    "Зарплаты и премии (Salaries and Awards, млн, $)",
    "Доля владельцев акций (Ownership share, %)",
    "Квалификация членов совета (Qualification)",
    "Среднесписочная численность персонала (Employees)",
    "Инвестиции в обучение (Staff Training, млн, $)",
    "Средняя зарплата на сотрудника (Average Salary, млн, $/чел)",
    "Текучесть персонала (Staff Frequency, %)",
    "Выручка на сотрудника (Profit per Employee, млн, $/чел)",
    "Доля инвестиций в управление (Investments in HR, %)",
    "Инвестиции в здоровье (Healthcare, млн, $)",
    "Выручка компании (Revenue, млн, $)",
    "Инвестиции в мобильность трудовых ресурсов (Labor Mobility, млн, $)"
]

#--------------------------------------------------AIS------------------------------------------------------------------
def ais(Ip, sigma, d, K, e, beta, Nc, gamma, f, restrictions, ndim, percent, data_array):
    """
    Algorithm of artificial immune system.

    Ip - initial number of points in population (overrides data_array size if provided),
    sigma - value of proximity between functions,
    d - percent of new cells which will be added in population,
    K - max number iteration of local search,
    e - value of proximity between average values of function in two various populations,
    beta|Nc - parameter of cloning procedure,
    gamma - parameter of mutation,
    f - function,
    restrictions - limits of function f,
    ndim - number of dimensions,
    data_array - initial data for population.
    """
    # STEP 1: Generate initial population
    print("STEP1")
    m = 0  # Counter for global search
    k = 0  # Iteration counter

    # Generate initial population
    population, populationF = generate_init_population(data_array, f, restrictions, ndim)

    Np = len(population)
    print("Initial Population:", population)
    print("Function Values:", populationF)
    print("Population Size:", Np)

    while True:
        # Calculate average adaptation of the population
        average_value_for_population = sum(populationF) / Np

        # STEP 2: Cloning the population
        print("\nSTEP2: Cloning")
        populationF_normalized = normalize_value(populationF)
        clones = uniform_cloning(population, Nc)

        # STEP 3: Mutate clones
        print("\nSTEP3: Mutation")
        mutated_clones = mutation(clones, populationF_normalized, restrictions, gamma)

        # STEP 4: Generate new population
        print("\nSTEP4: Generate New Population")
        mutated_clones_F = f_for_mutants(mutated_clones, f)

        # Combine original population with mutated clones
        new_population = []
        new_populationF = []

        for i in range(len(mutated_clones_F)):
            if mutated_clones_F[i][0] >= populationF[i]:
                new_population.append(mutated_clones[i][0])
                new_populationF.append(mutated_clones_F[i][0])
            else:
                new_population.append(population[i])
                new_populationF.append(populationF[i])

        # STEP 5: Check termination conditions
        print("\nSTEP5: Check Termination Conditions")
        average_value_for_new_population = sum(new_populationF) / Np
        print("Average Function Value:", average_value_for_new_population)

        if k == K:
            print("Max iterations reached.")
            return new_population, new_populationF
        elif abs(average_value_for_new_population - average_value_for_population) <= e:
            print("Convergence achieved.")
            return new_population, new_populationF

        # STEP 6: Reduce population
        print("\nSTEP6: Reduce Population")
        reduced_populationF, reduced_population, Ns = reduce_population(new_populationF, new_population, Np, ndim, sigma)

        # STEP 7: Global search
        print("\nSTEP7: Global Search")
        if m > 0 and Ns == Np:
            print("No improvement in global search.")
            return reduced_population, reduced_populationF
        m += 1

        # STEP 8: Add new cells
        print("\nSTEP8: Add New Cells")
        Nnew = int(Ns * d / percent)
        for _ in range(Nnew):
            new_points, new_pointsF = generate_init_population(data_array, f, restrictions, ndim)
            reduced_population.extend(new_points)
            reduced_populationF.extend(new_pointsF)

        population = reduced_population
        populationF = reduced_populationF
        Np = Ns + Nnew
        k += 1

def formatted_output_with_optimal(population, populationF, data_types):
    """
    Форматированный вывод популяции, значений функции и оптимальной точки.
    """
    # Транспонируем Population: теперь каждая строка — это отдельная точка
    transposed_population = list(zip(*population))

    # Определяем индекс оптимальной точки
    min_value = min(populationF)
    min_index = populationF.index(min_value)
    optimal_point = transposed_population[min_index]  # Соответствующая точка

    # Вывод популяции
    print("\nPopulation (Популяция):")
    for name, values in zip(data_types, population):
        formatted_values = [f"{value:.2f}" for value in values]
        print(f"  {name}: {formatted_values}")

    # Вывод значений функции
    print("\nPopulationF (Значения функции):")
    for name, value in zip(data_types, populationF):
        print(f"  {name}: {value:.2f}")

    # Вывод оптимальной точки
    print("\nОптимальная точка:")
    for name, value in zip(data_types, optimal_point):
        print(f"  {name}: {value:.2f}")
    print(f"\nЗначение целевой функции в оптимальной точке: {min_value:.2f}")





# Запуск алгоритма AIS
result = ais(Ip, sigma, d, K, e, beta, Nc, gamma, fffff, restrictions, ndim, percent, data_array)

# STEP 6: Reduce population
print("\nSTEP6: Reduce Population")

# STEP 7: Global search
print("\nSTEP7: Global Search")

# STEP 8: Add new cells
print("\nSTEP8: Add New Cells")

# Запуск форматированного вывода с оптимальной точкой
formatted_output_with_optimal(result[0], result[1], data_types)

