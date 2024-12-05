import os
import pandas as pd
import numpy as np

def parse_excel_to_data_array(file_path, sheet_name, indicators_to_save):
    """
    Парсит данные из Excel-файла по заданным показателям и формирует data_array и data_types.

    :param file_path: Путь к Excel-файлу
    :param sheet_name: Название листа с данными
    :param indicators_to_save: Список показателей для сохранения
    :return: data_array, data_types, years
    """
    # Чтение всех данных из Excel файла
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None, None, None

    data_array = []
    data_types = []
    years = []

    # Преобразуем список показателей в набор для быстрого поиска
    indicators_set = set(indicators_to_save)

    i = 0
    while i < len(df):
        row = df.iloc[i].fillna('').astype(str).tolist()

        # Ищем строку с заголовками таблицы (содержащую "Показатель")
        if any('Показатель' in cell for cell in row):
            header_row = df.iloc[i].fillna('').astype(str).tolist()
            columns_indices = [idx for idx, col in enumerate(header_row) if col.strip() not in ["Цель", "Примечание", "Комментарий", "Примечания", ""]]
            # Извлекаем годы из заголовков
            extracted_years = []
            for idx in columns_indices[1:]:  # Первый столбец — это показатель
                col_name = header_row[idx]
                year = col_name.strip().replace('г.', '').strip()
                if year.isdigit():
                    extracted_years.append(int(year))
                else:
                    extracted_years.append(year)
            if not years:
                years = extracted_years

            # Считываем данные до пустой строки или до конца файла
            data_start = i + 1
            data_end = data_start
            while data_end < len(df):
                data_row = df.iloc[data_end].fillna('').astype(str).tolist()
                if all(cell.strip() == '' for cell in data_row):
                    break
                data_end += 1

            data_df = df.iloc[data_start:data_end, columns_indices].reset_index(drop=True)
            data_df.columns = [header_row[idx] for idx in columns_indices]

            # Удаляем ненужные столбцы
            data_df = data_df.loc[:, ~data_df.columns.isin(["Цель", "Примечание", "Комментарий", "Примечания"])]

            # Проходим по каждому показателю и собираем данные
            for idx_row, row_data in data_df.iterrows():
                indicator_name = row_data.iloc[0]
                if indicator_name in indicators_set:
                    values = row_data.iloc[1:].tolist()
                    # Преобразуем значения в числовой формат
                    numeric_values = []
                    for val in values:
                        try:
                            val = str(val).replace(',', '.').strip()
                            numeric_values.append(float(val))
                        except:
                            numeric_values.append(np.nan)  # Используем np.nan для удобства вычислений

                    # Проверяем, есть ли хотя бы одно числовое значение (не nan)
                    if not all(np.isnan(numeric_values)):
                        # Если есть nan, заменяем их на среднее значение по остальным
                        if any(np.isnan(numeric_values)):
                            mean_value = np.nanmean(numeric_values)
                            # Если mean_value является nan (т.е. все значения nan), мы пропустим этот показатель
                            if np.isnan(mean_value):
                                continue  # Пропускаем этот показатель
                            else:
                                # Заменяем nan на среднее значение
                                numeric_values = [mean_value if np.isnan(v) else v for v in numeric_values]
                        data_types.append(indicator_name)
                        data_array.append(numeric_values)
                # else:
                #     print(f"Показатель '{indicator_name}' не в списке сохранения.")
            i = data_end  # Переходим к следующей строке после таблицы
        else:
            i += 1

    # Проверяем, удалось ли получить данные
    if not data_array:
        print("Не удалось получить данные для обработки.")
        return None, None, None

    # Выравниваем длины списков значений
    max_len = max(len(values) for values in data_array)
    data_array = [values + [np.nan]*(max_len - len(values)) for values in data_array]

    return data_array, data_types, years

# Список показателей для сохранения (без процентов и нечисловых значений)
indicators_to_save = [
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
    "Коэффициент обновления техники",
    "Коэффициент обеспеченности опытным оборудованием",
    "Коэффициент внедрения новой продукции",
    "Коэффициент инновационного роста",
    "Торговая марка  (Trademark), млн $",
    "Реклама (Advertising), млн $",
    "Спонсорские взносы (Sponsorship Fee), млн $",
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
    "Коэффициент долга к активам (Debt to Assets Ratio)",
    "Задолженность компании (Debt), млн $",
    "Эффект финансового рычага / Degree of Financial Leverage (DFL), доли",
    "Валовая прибыль (Gross profit), млн $",
    "Выручка от продаж (Revenue), млн $",
    "Прибыль до налогообложения / Pre-tax profit, млн $",
    "Прибыль до вычета процентов и налогов / EBIT (earnings before interest and taxes), млн $",
    "Прибыль от обычной деятельности / Profit from ordinary activities, млн $",
    "Чистая прибыль (Net Profit), млн $",
    "Чистая прибыль после уплаты налогов (NP after taxes), млн $",
    "Чистый денежный поток (NCF), млн $",
    "Объем продаж (Sales of products), млн $",
    "Фондоотдача",
    "Коэффициент оборачиваемости оборотных средств",
    "Коэффициент оборачиваемости общего капитала",
    "Инвестиции в трансфер технологий, млн $",
    "Новые собственные проекты по трансферу технологий, ед.",
    "Доходы от продажи лицензий, млн $",
    "Создание (выделение) дочерних предприятий, ед."
]

# Пример использования
input_file = '..//Аэрбас.xlsx'        # Укажите путь к вашему Excel-файлу
output_file = 'CopyPaste.txt'         # Укажите путь к выходному файлу

result = parse_excel_to_data_array(input_file, 'Лист1', indicators_to_save)

if result:
    data_array, data_types, years = result
    # Сохраняем данные в файл
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Добавляем необходимую шапку
            f.write("# Сгенерированные строки для вставки:\n")
            f.write(f"Ip = {len(data_array)}  # Количество начальных точек (число строк)\n")
            f.write("sigma = 0.5  # Примерное значение сигма\n")
            f.write("d = 40  # Процент новых клеток для добавления\n")
            f.write("K = 100  # Максимальное количество итераций\n")
            f.write("e = 0.1  # Порог изменения среднего значения популяции\n")
            f.write("beta = 10  # Коэффициент клонирования\n")
            f.write("Nc = 5  # Количество клонов на каждую точку\n")
            f.write(f"gamma = 10  # Коэффициент мутации\n")
            f.write(f"ndim = {len(years)}  # Размерность данных (количество столбцов)\n")
            f.write("percent = 100  # Процент новых клеток\n\n")

            # Формируем строку data_array
            f.write("data_array = [\n")
            for values in data_array:
                # Заменяем nan на 'None' в строковом формате
                values_str = [str(v) if not np.isnan(v) else 'None' for v in values]
                f.write(f"    [{', '.join(values_str)}],\n")
            f.write("]  # Данные для алгоритма (массив)\n\n")

            # Формируем строку data_types
            f.write("data_types = [\n")
            for dtype in data_types:
                f.write(f"    \"{dtype}\",\n")
            f.write("]\n")

            # Дополнительно можно сохранить годы, если необходимо
            f.write("\nyears = [\n")
            for year in years:
                f.write(f"    {year},\n")
            f.write("]\n")

        print(f"Файл успешно создан: {output_file}")

        # Выводим первые строки файла для проверки
        with open(output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Содержимое первых строк:\n{''.join(lines[:20])}")

    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
else:
    print("Не удалось получить данные для обработки.")
