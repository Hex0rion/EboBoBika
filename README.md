# EboBoBika


### Задачи
- [x] Написать парсер, слишком бесит ручками каждый раз вбивать данные
- [x] Понять, какие числа в каком режиме мы должны получать, что считаем корректным, что считаем лучшим из выдачи
- [x] Подогнать код под новые данные с парсера
- [ ] Выделить из бумажек только основное
- [ ] Подготовить наши правки и обоснование того, что и почему было плохо
- [ ] Сделать универсальный отчет, куда мы просто бахнем свои значения

### Что уже готово
1) Реализовали парсер, который по пути к табличке подготовит нам данные для работы в коде, поправив ошибки с пустыми ячейками, пустыми показателями. Программа из файла `converter.py` справляется с этим теперь сама.


<details><summary>Вот пример её вывода</summary>
<pre>
# Сгенерированные строки для вставки:
Ip = 45  # Количество начальных точек (число строк)
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
    [844.0, 841.0, 834.0, 825.0, 816.0, 812.0, 856.0, 894.0, 840.25],
    [10344.0, 12189.0, 10531.0, 8541.0, 5355.0, 5246.0, 14862.0, 6804.0, 9234.0],
    [0.0816, 0.069, 0.0792, 0.0966, 0.1524, 0.1548, 0.0576, 0.1314, 0.102825],
    [214.61, 232.28853351480095, 194.15674283875123, 210.88683385579938, 221.14196891191708, 193.43908008481486, 202.15262606613797, 213.49, 241.56],
    [0.97, 0.98, 0.97, 0.976, 0.978, 0.978, 0.98, 0.984, 0.977],
    [0.72, 0.7, 0.69, 0.68, 0.62, 0.59, 0.59, 0.56, 0.61],
    [1.02, 1.04, 1.025, 1.035, 1.05, 1.055, 1.06, 1.04, 1.06],
    [1.04, 1.06, 1.05, 1.08, 1.09, 1.1, 1.15, 1.08, 1.11],
    [1.041, 1.025, 1.014, 1.026, 1.038, 1.042, 1.085, 1.012, 1.12],
    [119.86, 122.9, 134.61, 144.16, 138.61, 136.6, 132.97, 130.9, 133.67],
    [18.0, 25.0, 34.0, 44.0, 53.0, 58.0, 59.0, 59.0, 62.0],
    [15.0, 18.0, 20.0, 16.0, 13.0, 16.0, 27.0, 30.0, 34.0],
    [66.0, 68.0, 72.0, 67.0, 73.0, 77.0, 80.0, 81.0, 85.0],
    [14649.0, 15198.259999999998, 15315.2, 16160.830000000002, 14732.410000000002, 12160.050000000001, 11652.78, 11503.4, 16610.86],
    [4.0, 4.0, 3.0, 4.0, 5.0, 5.0, 4.0, 5.0, 6.0],
    [4825.6, 6325.4, 7136.4, 1217.52, 2465.8199999999997, 4358.219999999999, 6518.5199999999995, -2458.9799999999996, 3148.3],
    [513.6, 718.2, 617.88, 1166.2199999999998, 2167.14, 2103.2999999999997, 2323.3199999999997, 1326.9599999999998, 1829.3],
    [321.8, 347.9, 424.08, 206.33999999999997, 254.21999999999997, 282.71999999999997, 365.93999999999994, 425.21999999999997, 451.8],
    [0.26125, 0.27, 0.28, 0.25, 0.26, 0.25, 0.24, 0.27, 0.27],
    [34.0, 38.0, 42.0, 41.0, 43.0, 39.0, 38.0, 44.0, 47.0],
    [65.0, 72.0, 74.0, 73.0, 75.0, 81.0, 83.0, 76.0, 79.0],
    [36.96, 37.716, 36.56, 37.65, 39.66, 43.974999999999994, 44.8, 45.171597429, 50.222775041679995],
    [1024.0, 981.0, 1192.0, 1063.0, 1065.0, 997.0, 872.0, 861.0, 892.0],
    [3.375, 4.0, 3.0, 3.0, 4.0, 2.0, 4.0, 3.0, 4.0],
    [1.625, 2.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0],
    [6523.22875, 4976.2, 5355.52, 6084.75, 8167.530000000001, 7246.080000000001, 5052.72, 6462.469999999999, 8840.56],
    [9.144253396639368, 3.507897592540493, 6.536620160133842, 10.284563868688114, 6.233096174730916, 9.500585143967497, 13.972276318497759, 13.098242622402891, 10.020745292153439],
    [1787.4016790000005, 722.54702, 1398.820864, 1703.0112680000004, 2725.8855400000007, 2685.134400000001, 1179.22626, 746.4960799999999, 3138.0919999999996],
    [2456.8762500000003, 1331.62, 1597.44, -1109.22, 2662.6600000000003, 3135.7500000000005, 3530.9100000000003, 4369.95, 4135.9],
    [0.4507618539715863, 0.4305350903043826, 0.4545510606808091, 0.45322245322245325, 0.4542813230309283, 0.4167766889190546, 0.4534927559648839, 0.5056671128960285, 0.4375683467541505],
    [0.9714569606155029, 0.9055908727318654, 0.9317752014471304, 0.9694736625429695, 0.9881045118639072, 0.9569890473622552, 0.9864813917164862, 1.0672735385988399, 0.9659674586605693],
    [18.793090337210256, 11.960784313725489, 19.107587064676622, 16.672318299988696, 20.48287283186612, 22.903225806451616, 7.406310176270181, 24.797448715738668, 27.014175488964646],
    [29.742125, 29.607, 25.216, 40.166000000000004, 18.354000000000003, 20.091000000000005, 54.05700000000001, 25.311999999999998, 25.134],
    [789.37, 812.0, 819.3, 792.4, 782.96, 785.62, 773.79, 773.72, 775.17],
    [1.095, 1.11, 1.15, 1.18, 1.08, 1.05, 1.01, 1.11, 1.07],
    [9422.66625, 7094.5599999999995, 6117.12, 7449.330000000001, 9776.83, 10128.75, 11630.580000000002, 12651.48, 10532.68],
    [9663.39125, 9511.769999999999, 10156.800000000001, 11120.130000000001, 11886.210000000001, 9824.61, 5843.040000000001, 8595.91, 10368.66],
    [74525.80875, 68287.92, 72294.40000000001, 78810.48000000001, 80748.29000000001, 71539.5, 73904.91, 75446.70999999999, 75174.26],
    [3837.2537500000003, 2357.44, 2727.68, 3467.3100000000004, 5308.030000000001, 4508.820000000001, 2506.38, 3865.7299999999996, 5956.639999999999],
    [3315.55625, 2051.6400000000003, 2147.8399999999997, 2652.0200000000004, 4273.290000000001, 3746.2500000000005, 1433.01, 5164.099999999999, 5056.299999999999],
    [2376.32125, 1441.4299999999998, 1573.1200000000001, 1961.75, 3125.5, 2994.78, 1110.0, 3251.0099999999998, 3552.98],
    [853.0150000000001, 353.06, 4444.16, -1318.03, 117.04, 318.57000000000005, 3866.1300000000006, 2102.93, -3059.74],
    [3.7701480393410054, 3.4697365633166184, 3.7167675704132668, 3.737134207870838, 3.7199313767538755, 3.763064167688445, 3.936675929758174, 4.0196869355809755, 3.7981875633458535],
    [0.5971921532653492, 0.5552692255526923, 0.6132331545460469, 0.634901586825385, 0.6317558427504111, 0.6041375690141637, 0.5992188132801742, 0.5859992803040277, 0.5530217538498933],
    [1.3097098043340334, 1.9108518086347723, 1.7547457047876474, 0.9917322175732219, 1.5680010330578515, 1.1995160990135865, 1.3405084161648406, 0.849669127004327, 0.862654028436019],
]  # Данные для алгоритма (массив)

data_types = [
    "Расходы на НИОКР (R&D Expenditures), млн $",
    "Инвестированный капитал (Invested Capital), млн. $",
    "НИР-мультипликатор",
    "Расходы на подготовку и переподготовку кадров  (Cost of training employees), тыс. $",
    "Коэффициент постоянства кадров (КПК) (Employee stability Index)",
    "Показатель рентабельности персонала (Revenue Per Employee)",
    "Индекс средней заработной платы фиксированного состава (Average Wage Index)",
    "Индекс производительности труда (Labor productivity index)",
    "Коэффициент опережения роста производительности труда",
    "Среднесписочная численность персонала (Number of employees)",
    "Патенты (Patents), ед.",
    "Лицензии (Licenses), ед.",
    "Промышленные образцы, ед.",
    "Goodwill, млн $",
    "Количество внедренных в производство технологий, ед.",
    "Прирост объема производства продукции, млн $",
    "Прирост добавленной стоимости, млн $",
    "Экономия материальных ресурсов, млн $",
    "Коэффициент персонала, занятого НИР и ОКР",
    "Коэффициент обеспеченности интеллектуальной собственностью",
    "Коэффициент обеспеченности опытным оборудованием",
    "Торговая марка  (Trademark), млн $",
    "Реклама (Advertising), млн $",
    "Объем запасов сырья и материалов (в единицах времени) для обеспечения производства, ч.",
    "Объем запасов готовой продукции (в единицах времени) для полной реализации, дн.",
    "EBITDA, млн $",
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
    "Валовая прибыль (Gross profit), млн $",
    "Выручка от продаж (Revenue), млн $",
    "Прибыль до вычета процентов и налогов / EBIT (earnings before interest and taxes), млн $",
    "Прибыль от обычной деятельности / Profit from ordinary activities, млн $",
    "Чистая прибыль (Net Profit), млн $",
    "Чистый денежный поток (NCF), млн $",
    "Фондоотдача",
    "Коэффициент оборачиваемости оборотных средств",
    "Коэффициент оборачиваемости общего капитала",
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
</pre>
</details>

2) Грубо говоря, для всех функций меньше = лучше

<details><summary>Ответ ГПТ</summary>
<pre>
    
---

### 1. **Сферическая функция (Sphere Function):**
   **Лучшее значение:** минимальное (чем меньше, тем лучше).
   - Это выпуклая функция, и минимальное значение достигается в точке \( f(0, 0) = 0 \).

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = -20 (лучше)
   Среднее значение: f(x, y) = -10
   Большее значение: f(x, y) = -5 (хуже)
   ```

---

### 2. **Ackley’s Function:**
   **Лучшее значение:** минимальное (глобальный минимум — около 0).
   - Эта функция сложна из-за множества локальных минимумов, но алгоритм должен стремиться к глобальному минимуму.

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = 0.1 (лучше)
   Среднее значение: f(x, y) = 5.0
   Большее значение: f(x, y) = 10.0 (хуже)
   ```

---

### 3. **Rosenbrock Function:**
   **Лучшее значение:** минимальное (глобальный минимум — около 0).
   - Функция тестирует, насколько алгоритм способен избегать узких долин.

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = -1 (лучше)
   Среднее значение: f(x, y) = -10
   Большее значение: f(x, y) = -50 (хуже)
   ```

---

### 4. **Beale’s Function:**
   **Лучшее значение:** минимальное (глобальный минимум — 0).
   - Среднее и большее значения показывают, насколько алгоритм далёк от оптимума.

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = -5 (лучше)
   Среднее значение: f(x, y) = -15
   Большее значение: f(x, y) = -30 (хуже)
   ```

---

### 5. **Booth’s Function:**
   **Лучшее значение:** минимальное (глобальный минимум — 0).
   - Простой пример для тестирования линейных зависимостей.

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = -1 (лучше)
   Среднее значение: f(x, y) = -5
   Большее значение: f(x, y) = -10 (хуже)
   ```

---

### 6. **Lévi Function N.13:**
   **Лучшее значение:** минимальное (глобальный минимум — 0).
   - Локальные минимумы могут удерживать алгоритм.

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = 0.01 (лучше)
   Среднее значение: f(x, y) = 5.0
   Большее значение: f(x, y) = 10.0 (хуже)
   ```

---

### 7. **Three-hump camel function:**
   **Лучшее значение:** минимальное (глобальный минимум — 0).
   - Функция подходит для тестирования алгоритмов на сложных поверхностях.

   **Интерпретация:**
   ```
   Меньшее значение: f(x, y) = -2 (лучше)
   Среднее значение: f(x, y) = -1
   Большее значение: f(x, y) = 0 (хуже)
   ```

---

### Итоговые принципы:
1. **Меньшее значение** всегда является лучшим для тестовых функций оптимизации, так как все функции ориентированы на минимизацию.
2. Средние и большие значения показывают, насколько алгоритм далёк от глобального минимума.
3. Для каждой функции важно фиксировать тенденцию приближения к оптимуму, чтобы оценить качество оптимизации.
</pre>
</details>

---

* Для удобства данные можно хранить в папке, в которой содержится папка проекта.

* Перед запуском основного кода:
  1) Закрыть файл `CopyPaste.txt`
  2) Указать в конвертере в качестве переменной `input_file` на 174 строке путь к файлу
  3) Запустить парсер
  4) Открыть файл `CopyPaste.txt`
  5) Скопировать все его содержимое
  6) В файле `ais.py`, начиная с 7 строки вставить всё, что скопировали
  7) Можно запускать файл

Ниже в блоке кода, возможно понадобится отключить транспонирование, но на сколько я посмотрел, пока что работает +- корректно
```py
# Транспонируем данные, чтобы получить список точек
data_array = list(map(list, zip(*data_array)))
```

Функции можно выбрать в строках, достаточно заменить название одной на другую
```py
# Выбор целевой функции и ограничений
# Выберите функцию из списка: 'sphere', 'ackley', 'rosenbrock', 'beale', 'booth', 'levi', 'three_hump_camel'
function_choice = 'ackley'  # Измените на нужную функцию
```

Когда в ходе работы кода по каким то причинам появляются новые года, в выводе появятся `*` возле этих годов

В коде есть "оптимизатор", смулирующий вычисления
```py
Optimizator(10, 75) # Используем оптимизатор для ускорения вычислений
```
Здесь мы задаем примерное число секунд ожидания `10` и длину полоски пргресса `75`
