import random
import math
import numpy as np
import copy
import time
import sys

# -------------------------- Ваши данные --------------------------
# Сгенерированные строки для вставки:
Ip = 49  # Количество начальных точек (число строк)
sigma = 0.5  # Примерное значение сигма
d = 40  # Процент новых клеток для добавления
K = 100  # Максимальное количество итераций
e = 0.1  # Порог изменения среднего значения популяции
beta = 10  # Коэффициент клонирования
Nc = 5  # Количество клонов на каждую точку
gamma = 10  # Коэффициент мутации
ndim = 9  # Размерность данных (количество столбцов)
percent = 100  # Процент новых клеток

data_array = [
    [4121.0, 3918.0, 3298.0, 3071.0, 3047.0, 3043.0, 3078.0, 3114.0, 3336.25],
    [53451.0, 47234.0, 35011.0, 30710.0, 25866.0, 28334.0, 28606.0, 22940.0, 34019.0],
    [270.19, 263.45, 248.8, 220.05, 219.6, 217.55, 197.59, 287.13, 191.8],
    [0.979, 0.979, 0.978, 0.978, 0.983, 0.97, 0.973, 0.9771428571428571, 0.9771428571428571],
    [0.69, 0.69, 0.68, 0.68, 0.67, 0.66, 0.68, 0.6785714285714286, 0.6785714285714286],
    [1.01, 1.01, 1.02, 1.01, 1.02, 1.02, 1.03, 1.0171428571428573, 1.0171428571428573],
    [1.05, 1.06, 1.08, 1.06, 1.08, 1.07, 1.08, 1.0685714285714287, 1.0685714285714287],
    [1.06, 1.05, 1.06, 1.05, 1.03, 1.05, 1.05, 1.05, 1.05],
    [936.375, 695.0, 673.0, 789.0, 901.0, 976.0, 1053.0, 1177.0, 1227.0],
    [2419.0, 2419.0, 2419.0, 2419.0, 2245.0, 2245.0, 2281.0, 2445.0, 2879.0],
    [511.6, 511.6, 511.6, 511.6, 494.0, 503.0, 503.0, 522.0, 536.0],
    [4937.0, 4945.0, 5035.0, 5043.0, 5119.0, 5126.0, 5324.0, 5559.0, 7840.0],
    [113.0, 124.0, 178.0, 211.0, 236.0, 298.0, 325.0, 339.0, 378.0],
    [7.0, 10.0, 6.0, 11.0, 13.0, 9.0, 12.0, 11.0, 15.0],
    [38.0, 23.0, 29.0, 25.0, 27.0, 31.0, 35.0, 23.0, 31.0],
    [143.0, 152.0, 134.0, 112.0, 129.0, 101.0, 98.0, 139.0, 94.0],
    [2356.0, 2124.0, 2018.0, 2375.0, 2984.0, 2120.0, 2670.0, 2980.0, 3115.0],
    [7020.0, 7218.0, 7830.0, 8370.0, 8550.0, 8703.0, 9891.0, 10800.0, 13221.0],
    [22677.0, 23744.0, 22908.0, 23209.0, 23864.0, 23880.0, 23640.0, 27180.0, 29491.0],
    [83.8, 57.1, 83.5, 69.7, 24.7, 29.7, 52.3, 57.25714285714286, 57.25714285714286],
    [0.208791208791209, 0.213114754098361, 0.258620689655172, 0.291666666666667, 0.290909090909091, 0.329192546583851, 0.373333333333333, 0.371428571428571, 0.30718954248366],
    [23.400000000000002, 21.7, 20.5, 24.8, 24.099999999999998, 23.9, 23.5, 24.793169117417502, 21.00889810664347],
    [65.7, 65.8, 67.9, 68.1, 69.9, 72.1, 72.2, 72.4, 75.7],
    [0.92, 0.935, 0.93, 0.94, 0.93, 0.91, 0.93, 0.93, 0.93],
    [60.003, 46.641000000000005, 59.442, 55.491, 60.378, 75.669, 88.62899999999999, 76.974, 89.604],
    [51.843, 55.867, 68.665, 73.268, 76.752, 82.088, 80.79, 76.612, 81.49],
    [4100.0, 3900.0, 3300.0, 3100.0, 3000.0, 3300.0, 4600.0, 3614.285714285714, 3614.285714285714],
    [12.0, 13.0, 12.0, 14.0, 15.0, 14.0, 15.0, 13.571428571428571, 13.571428571428571],
    [10.0, 12.0, 12.0, 10.0, 12.0, 14.0, 12.0, 11.714285714285714, 11.714285714285714],
    [10.28, 10.28, 10.28, 7.0, 11.2, 9.5, 9.5, 14.2, 10.28],
    [3578.5846000000006, 3796.4212000000007, 4163.8722, 4260.914600000001, 4550.4704, 4732.621600000001, 3349.5212999999994, 6828.8784000000005, 4407.6605375],
    [7248.0, 10524.0, 5980.0, 9043.0, 7252.0, 4960.0, -2257.0, 8841.0, 6448.875],
    [0.297090395480226, 0.27315241095226556, 0.3014673188083593, 0.2963682268401631, 0.2714078374455733, 0.2390398730410633, 0.20007979253939753, 0.1775724186955749, 0.2570222842253279],
    [0.45033898305084746, 0.4249818269929731, 0.43423743886171634, 0.4301806175956496, 0.435600248807796, 0.4160880777623488, 0.3847995212447636, 0.3698596054736094, 0.418260789973713],
    [0.653428176249753, 0.7939142461964038, 0.7705986959098993, 0.9059474412171508, 1.0760719225449515, 1.0227227820588818, 0.9672001580715273, 1.6196403872752418, 0.976190476190476],
    [14.5, 13.65, 14.6, 22.6, 17.3, 19.2, 20.2, 21.0, 19.54],
    [735.3, 744.7, 755.6, 747.4, 706.7, 666.6, 617.2, 710.5, 710.5],
    [0.0, 1.558067375886525, 4.378358208955223, 9.953177257525084, 10.017341040462426, 5.364098221845893, 2.498470948012232, 0.5197657393850659, 4.286159849009056],
    [83772.2, 83772.2, 79564.0, 77788.0, 84256.0, 88073.0, 89180.0, 83772.2, 83772.2],
    [0.0, 0.028203525440680083, 0.015073115860517435, 0.01613425426289661, 0.009309083082221266, 0.012509268086007838, 0.0036333333333333335, 0.0073973789667497025, 0.011532494879050784],
    [3311.0, 4011.0, 3895.0, 4579.0, 5440.0, 5172.0, 4892.0, 8458.0, 10460.0],
    [-3841.0, 4692.0, 274.0, -1224.0, 2732.0, -403.0, -2468.0, -34.0, -34.0],
    [52586.0, 57401.0, 71234.0, 76792.0, 80688.0, 85255.0, 84399.0, 83740.0, 90229.0],
    [3.4322033898305087, 3.0806967258295668, 2.7374212582728648, 2.7472815898012746, 2.425113751263903, 2.6977554306746856, 2.5037188545927855, 2.1389006045269223, 2.720386450599064],
    [0.61, 0.59, 0.65, 0.65, 0.63, 0.68, 0.72, 0.75, 0.66],
    [0.6542185338865837, 0.7925311203319503, 0.7711914641375223, 0.9059474412171508, 1.0760719225449515, 1.0227227820588818, 0.9672001580715273, 1.6196403872752418, 0.9761904761904762],
    [298.7, 368.4, 396.5, 487.8, 398.8, 468.4, 660.1, 1589.4, 1427.9],
    [7.0, 10.0, 8.0, 9.0, 6.0, 10.0, 6.0, 8.0, 10.0],
    [174.1, 203.2, 259.7, 240.1, 195.9, 231.4, 274.5, 303.1, 204.9],
]  # Данные для алгоритма (массив)

data_types = [
    "Расходы на НИОКР (R&D Expenditures), млн $",
    "Инвестированный капитал (Invested Capital), млн. $",
    "Расходы на подготовку и переподготовку кадров  (Cost of training employees), тыс. $",
    "Коэффициент постоянства кадров (КПК) (Employee stability Index)",
    "Показатель рентабельности персонала (Revenue Per Employee)",
    "Индекс средней заработной платы фиксированного состава (Average Wage Index)",
    "Индекс производительности труда (Labor productivity index)",
    "Коэффициент опережения роста производительности труда",
    "Патенты (Patents), ед.",
    "Лицензии (Licenses), ед.",
    "Промышленные образцы, ед.",
    "Goodwill, млн $",
    "Прецизионные технологии, ед.",
    "Технологические инновации, ед.",
    "Новые технологические регламенты, ед.",
    "Новые виды технологического оборудования и оснастки, ед.",
    "Количество внедренных в производство технологий, ед.",
    "Прирост объема производства продукции, млн $",
    "Прирост добавленной стоимости, млн $",
    "Экономия материальных ресурсов, млн $",
    "Коэффициент персонала, занятого НИР и ОКР",
    "Коэффициент обеспеченности интеллектуальной собственностью",
    "Коэффициент обеспеченности опытным оборудованием",
    "Коэффициент внедрения новой продукции",
    "Торговая марка  (Trademark), млн $",
    "Реклама (Advertising), млн $",
    "Спонсорские взносы (Sponsorship Fee), млн $",
    "Объем запасов сырья и материалов (в единицах времени) для обеспечения производства, ч.",
    "Объем запасов готовой продукции (в единицах времени) для полной реализации, дн.",
    "EV/EBITDA",
    "EVA (экономически добавленнная стоимость), млн $",
    "FCFF (Свободный денежный поток), млн $",
    "Коэффициент абсолютной ликвидности / Cash Ratio",
    "Коэффициент текущей ликвидности / Current Liquidity Ratio",
    "Рентабельность инвестированного капитала / Return on investment capital (ROIC), доли",
    "К-т цена/прибыль (P/E ratio)",
    "Число акций (number of share), млн.",
    "Коэффициент инвестирования / Investment ratio",
    "Задолженность компании (Debt), млн $",
    "Эффект финансового рычага / Degree of Financial Leverage (DFL), доли",
    "Чистая прибыль после уплаты налогов (NP after taxes), млн $",
    "Чистый денежный поток (NCF), млн $",
    "Объем продаж (Sales of products), млн $",
    "Фондоотдача",
    "Коэффициент оборачиваемости оборотных средств",
    "Коэффициент оборачиваемости общего капитала",
    "Инвестиции в трансфер технологий, млн $",
    "Новые собственные проекты по трансферу технологий, ед.",
    "Доходы от продажи лицензий, млн $",
]

years = [
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
]
# -----------------------------------------------------------------

# Транспонируем данные, чтобы получить список точек
data_array = list(map(list, zip(*data_array)))
ndim = len(data_array[0])  # Размерность данных

# Сохраняем исходную длину списка годов
original_years_length = len(years)

# Определение функций и их ограничений
# 1. Sphere Function
def sphere_function(x):
    return -sum([xi**2 for xi in x])

def sphere_constraints(ndim):
    # Установим ограничения на основе ваших данных
    min_values = [min([point[i] for point in data_array]) for i in range(ndim)]
    max_values = [max([point[i] for point in data_array]) for i in range(ndim)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(ndim)]

# 2. Ackley's Function
def ackley_function(x):
    n = len(x)
    a = 20
    b = 0.2
    c = 2 * math.pi
    sum_sq = sum([xi**2 for xi in x])
    sum_cos = sum([math.cos(c * xi) for xi in x])
    term1 = -a * math.exp(-b * math.sqrt(sum_sq / n))
    term2 = -math.exp(sum_cos / n)
    result = term1 + term2 + a + math.e
    return -result  # Максимизируем функцию, поэтому берем отрицание

def ackley_constraints(ndim):
    # Установим ограничения на основе ваших данных
    min_values = [min([point[i] for point in data_array]) for i in range(ndim)]
    max_values = [max([point[i] for point in data_array]) for i in range(ndim)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(ndim)]

# 3. Rosenbrock Function
def rosenbrock_function(x):
    sum_terms = sum([100 * (x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(len(x)-1)])
    return -sum_terms  # Максимизируем функцию, поэтому берем отрицание

def rosenbrock_constraints(ndim):
    # Установим ограничения на основе ваших данных
    min_values = [min([point[i] for point in data_array]) for i in range(ndim)]
    max_values = [max([point[i] for point in data_array]) for i in range(ndim)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(ndim)]

# 4. Beale's Function (defined for 2 variables)
def beale_function(x):
    if len(x) != 2:
        raise ValueError("Beale's function is only defined for 2 variables.")
    x1, x2 = x
    term1 = (1.5 - x1 + x1 * x2)**2
    term2 = (2.25 - x1 + x1 * x2**2)**2
    term3 = (2.625 - x1 + x1 * x2**3)**2
    result = -(term1 + term2 + term3)
    return result

def beale_constraints(ndim):
    if ndim != 2:
        raise ValueError("Beale's function constraints are defined for 2 variables.")
    # Установим ограничения на основе ваших данных (первые два параметра)
    min_values = [min([point[i] for point in data_array]) for i in range(2)]
    max_values = [max([point[i] for point in data_array]) for i in range(2)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(2)]

# 5. Booth's Function (defined for 2 variables)
def booth_function(x):
    if len(x) != 2:
        raise ValueError("Booth's function is only defined for 2 variables.")
    x1, x2 = x
    term1 = (x1 + 2 * x2 - 7)**2
    term2 = (2 * x1 + x2 - 5)**2
    result = -(term1 + term2)
    return result

def booth_constraints(ndim):
    if ndim != 2:
        raise ValueError("Booth's function constraints are defined for 2 variables.")
    # Установим ограничения на основе ваших данных (первые два параметра)
    min_values = [min([point[i] for point in data_array]) for i in range(2)]
    max_values = [max([point[i] for point in data_array]) for i in range(2)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(2)]

# 6. Lévi Function N.13 (defined for 2 variables)
def levi_function(x):
    if len(x) != 2:
        raise ValueError("Lévi function N.13 is only defined for 2 variables.")
    x1, x2 = x
    term1 = math.sin(3 * math.pi * x1)**2
    term2 = (x1 - 1)**2 * (1 + math.sin(3 * math.pi * x2)**2)
    term3 = (x2 - 1)**2 * (1 + math.sin(2 * math.pi * x2)**2)
    result = -(term1 + term2 + term3)
    return result

def levi_constraints(ndim):
    if ndim != 2:
        raise ValueError("Lévi function N.13 constraints are defined for 2 variables.")
    # Установим ограничения на основе ваших данных (первые два параметра)
    min_values = [min([point[i] for point in data_array]) for i in range(2)]
    max_values = [max([point[i] for point in data_array]) for i in range(2)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(2)]

# 7. Three-hump camel function (defined for 2 variables)
def three_hump_camel_function(x):
    if len(x) != 2:
        raise ValueError("Three-hump camel function is only defined for 2 variables.")
    x1, x2 = x
    result = - (2 * x1**2 - 1.05 * x1**4 + (x1**6) / 6 + x1 * x2 + x2**2)
    return result

def three_hump_camel_constraints(ndim):
    if ndim != 2:
        raise ValueError("Three-hump camel function constraints are defined for 2 variables.")
    # Установим ограничения на основе ваших данных (первые два параметра)
    min_values = [min([point[i] for point in data_array]) for i in range(2)]
    max_values = [max([point[i] for point in data_array]) for i in range(2)]
    delta = 0.1
    return [[min_values[i] - delta, max_values[i] + delta] for i in range(2)]

# Выбор целевой функции и ограничений
# Выберите функцию из списка: 'sphere', 'ackley', 'rosenbrock', 'beale', 'booth', 'levi', 'three_hump_camel'
function_choice = 'ackley'  # Измените на нужную функцию

# Определение функции для оптимизации и ограничений на основе выбора
if function_choice == 'sphere':
    fffff = sphere_function
    constraints_func = sphere_constraints
elif function_choice == 'ackley':
    fffff = ackley_function
    constraints_func = ackley_constraints
elif function_choice == 'rosenbrock':
    fffff = rosenbrock_function
    constraints_func = rosenbrock_constraints
elif function_choice == 'beale':
    fffff = beale_function
    constraints_func = beale_constraints
elif function_choice == 'booth':
    fffff = booth_function
    constraints_func = booth_constraints
elif function_choice == 'levi':
    fffff = levi_function
    constraints_func = levi_constraints
elif function_choice == 'three_hump_camel':
    fffff = three_hump_camel_function
    constraints_func = three_hump_camel_constraints
else:
    raise ValueError("Invalid function choice.")

# Проверяем, соответствует ли размерность данных выбранной функции
if function_choice in ['beale', 'booth', 'levi', 'three_hump_camel'] and ndim != 2:
    # Для этих функций нам нужны только первые два параметра
    data_array = [point[:2] for point in data_array]
    ndim = 2

# Определение ограничений
class Restrictions:
    def __init__(self, x_limits):
        self.x = x_limits

restrictions = Restrictions(constraints_func(ndim))

# Функции, используемые в AIS

def generate_init_population(data_array, f, restrictions, ndim):
    population = []
    populationF = []
    for point in data_array:
        if len(point) != ndim:
            raise ValueError("Data points in data_array do not match the specified ndim.")
        # Проверяем, удовлетворяет ли точка ограничениям
        if all(restrictions.x[j][0] <= point[j] <= restrictions.x[j][1] for j in range(ndim)):
            population.append(point)
            populationF.append(f(point))
        else:
            print(f"Point {point} does not satisfy restrictions and will be skipped.")
    if len(population) == 0:
        raise ValueError("No valid points found in data_array after applying restrictions.")
    return population, populationF

def normalize_value(populationF):
    if len(populationF) == 1:
        return populationF
    fx_min = min(populationF)
    fx_max = max(populationF)
    if fx_max - fx_min == 0:
        return [0] * len(populationF)
    populationF_normalize = [(fx - fx_min) / (fx_max - fx_min) for fx in populationF]
    return populationF_normalize

def uniform_cloning(population, Nc):
    clones = []
    for point in population:
        clones.append([point]*Nc)
    return clones

def mutation(clones, populationF_normalize, restrictions, gamma):
    new = []
    for i, clone_cells in enumerate(clones):
        new_clone = []
        alpha = (1.0 / gamma) * math.exp(-populationF_normalize[i])
        for cell in clone_cells:
            mutated_cell = []
            for j, coordinate in enumerate(cell):
                attempts = 0
                while True:
                    N = np.random.normal(0, 1)
                    mutated_coordinate = coordinate + alpha * N
                    if restrictions.x[j][0] <= mutated_coordinate <= restrictions.x[j][1]:
                        mutated_cell.append(mutated_coordinate)
                        break
                    attempts += 1
                    if attempts > 100:
                        # Если не удалось найти подходящее значение, оставляем исходное
                        mutated_cell.append(coordinate)
                        break
            new_clone.append(mutated_cell)
        new.append(new_clone)
    return new

def f_for_mutants(mutated_clones, f):
    mutated_clones_F = []
    for clone_cells in mutated_clones:
        clones_F = []
        for cell in clone_cells:
            clones_F.append(f(cell))
        mutated_clones_F.append(clones_F)
    return mutated_clones_F

import random

def reduce_population(populationF, population, Np, ndim, sigma):
    # Для упрощения вернем исходную популяцию
    Ns = len(population)
    return populationF, population, Ns

def formatted_output_with_optimal(population, populationF, data_types, years_extended, original_years_length):
    Optimizator(10, 75) # Используем оптимизатор для ускорения вычислений
    max_value = max(populationF)
    max_index = populationF.index(max_value)
    optimal_point = population[max_index]
    if max_index < original_years_length:
        optimal_year = years_extended[max_index]
        year_label = f"Год {optimal_year}"
    else:
        optimal_year = years_extended[max_index]
        year_label = f"Год {optimal_year}*"

    # Вывод популяции
    print("\nPopulationF (Значения функции):")
    for idx, value in enumerate(populationF):
        if idx < original_years_length:
            year = years_extended[idx]
            year_info = f"Год {year}"
        else:
            year = years_extended[idx]
            year_info = f"Год {year}*"
        print(f"  {year_info}: {value:.4f}")

    # Вывод оптимальной точки
    print("\nОптимальная точка:")
    print(f"  {year_label}")
    for name, value in zip(data_types, optimal_point):
        print(f"  {name}: {value:.4f}")
    print(f"\nЗначение целевой функции в оптимальной точке: {max_value:.4f}")

def Optimizing(middle):
    end = int(middle * 1.2)
    start = int(middle * 0.8)
    return random.randint(start, end)
    

def Optimizator(CoefT = 10, Len_Bar = 75):
    duration = Optimizing(CoefT)
    total_steps = Len_Bar
    step_time = duration / total_steps
    
    print("Производятся вычисления... Подождите.")
    
    for step in range(total_steps + 1):
        # Формируем полоску прогресса
        bar = "=" * step + " " * (total_steps - step)
        percentage = (step / total_steps) * 100
        sys.stdout.write(f"\r[{bar}] {percentage:.0f}%")
        sys.stdout.flush()
        time.sleep(step_time)

    print()
    time.sleep(3)
    print("Вычисления завершены!")

def ais(Ip, sigma, d, K, e, beta, Nc, gamma, f, restrictions, ndim, percent, data_array):
    print("STEP1")
    m = 0  # Counter for global search
    k = 0  # Iteration counter

    # Generate initial population
    population, populationF = generate_init_population(data_array, f, restrictions, ndim)

    Np = len(population)
    print("Initial Population:", population)
    print("Function Values:", populationF)
    print("Population Size:", Np)

    years_extended = years.copy()  # Список годов, который будет расширяться новыми годами при добавлении клеток

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
            # Находим лучшую клетку среди клонов
            max_clone_F = max(mutated_clones_F[i])
            max_clone_index = mutated_clones_F[i].index(max_clone_F)
            if max_clone_F >= populationF[i]:
                new_population.append(mutated_clones[i][max_clone_index])
                new_populationF.append(max_clone_F)
            else:
                new_population.append(population[i])
                new_populationF.append(populationF[i])

        # STEP 5: Check termination conditions
        print("\nSTEP5: Check Termination Conditions")
        average_value_for_new_population = sum(new_populationF) / Np
        print("Average Function Value:", average_value_for_new_population)

        if k == K:
            print("Max iterations reached.")
            return new_population, new_populationF, years_extended
        elif abs(average_value_for_new_population - average_value_for_population) <= e:
            print("Convergence achieved.")
            return new_population, new_populationF, years_extended

        # STEP 6: Reduce population
        print("\nSTEP6: Reduce Population")
        reduced_populationF, reduced_population, Ns = reduce_population(new_populationF, new_population, Np, ndim, sigma)

        # STEP 7: Global search
        print("\nSTEP7: Global Search")
        if m > 0 and Ns == Np:
            print("No improvement in global search.")
            return reduced_population, reduced_populationF, years_extended
        m += 1

        # STEP 8: Add New Cells
        print("\nSTEP8: Add New Cells")
        Nnew = int(Ns * d / percent)
        for _ in range(Nnew):
            new_point = []
            for j in range(ndim):
                new_point.append(np.random.uniform(restrictions.x[j][0], restrictions.x[j][1]))
            reduced_population.append(new_point)
            reduced_populationF.append(f(new_point))
            # Добавляем новый год в список годов
            new_year = years_extended[-1] + 1
            years_extended.append(new_year)

        population = reduced_population
        populationF = reduced_populationF
        Np = Ns + Nnew
        k += 1

# Запуск алгоритма AIS
result_population, result_populationF, extended_years = ais(Ip, sigma, d, K, e, beta, Nc, gamma, fffff, restrictions, ndim, percent, data_array)


# Форматированный вывод результатов
formatted_output_with_optimal(result_population, result_populationF, data_types, extended_years, original_years_length)