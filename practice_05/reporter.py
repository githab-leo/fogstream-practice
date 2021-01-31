# Разделите вашу программу разработанную в задании task3 на два модуля:
# good_info и reporter. Сделайте модуль reporter точкой запуска.
# Обновите документацию в файле README.md в вашем репозитории, указав
# какой модуль необходимо запускать.

# Добавьте в GoodInfo новое свойство/аттрибут - Дата поставки (день, месяц, год).
# Обновите метод добавления товара. При добавлении в случае если ДАТА поставки
# меньше текущей нужно выдавать сообщение об ошибке.

# Добавьте в GoodInfo новое свойство/аттрибут - Срок годности. Обновите
# метод добавления товара. Добавьте внутренний метод - Проверить срок, который удаляет
# товары с истёкшим сроком годности, метод должен возвращать список товаров GoodInfoList

# добавьте возможность получения элемента по ключу good_name в GoodInfoList
# изменив метод __getitem__()
# если таких элементов несколько верните список GoodInfoList

# Добавьте в модуль reporter пример демонстрации новых возможностей программы
# Для проверки используйте файл, приложенный к заданию goods2.info
# Данные в файле находятся в в формате:
# Имя товара:Цена:Количество:Дата поставки:Время хранения(в днях)


"""
Модуль reporter предназначен для вывода информации о товарах.

"""

from good_info import GoodInfoList
import logging
import argparse


# создаем регистратор
log_rep = logging.getLogger('reporter')
log_rep.setLevel(logging.INFO)
# создаём обработчик логера
handler = logging.FileHandler('output.log')
handler.setLevel(logging.INFO)
# строка формата сообщения
STRFMT = '[%(asctime)s] [%(name)s] [%(levelname)s] [%(filename)s] [%(funcName)s] > %(message)s'
# строка формата времени
DATEFMT = '%Y-%m-%d %H:%M:%S'
# создаем форматтер
formatter = logging.Formatter(fmt=STRFMT, datefmt=DATEFMT)
# добавляем форматтер к 'ch'
handler.setFormatter(formatter)
# обработчик добавляется в логгер
log_rep.addHandler(handler)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-rname', default='goods2.info')
    parser.add_argument('-wname')
    namespace = parser.parse_args()

    print('---------------- Проблемы при считывании файла --------------')
    log_rep.info('---------------- Проблемы при считывании файла --------------')
    goods_info_list = GoodInfoList()
    goods_info_list.read_file(namespace.rname)

    print('----------------- Вывод информации о товарах ---------------')
    log_rep.info('----------------- Вывод информации о товарах ---------------')

    msg = "Общее количество товаров - {total_count}" \
        .format(total_count=len(goods_info_list))
    print(msg)
    log_rep.info(msg)

    msg = "Средняя цена товара - {average_cost}" \
        .format(average_cost=goods_info_list.average_price())
    print(msg)
    log_rep.info(msg)

    for element in goods_info_list.most_expensive_products():
        msg = "Самый дорогой товар - {good_name}, Цена - {good_cost}" \
            .format(good_name=element.product_name,
                    good_cost=element.cost_product)
        print(msg)
        log_rep.info(msg)

    for element in goods_info_list.ending_products():
        msg = "Заканчивается товар - {good_name}, Осталось - {good_cost}" \
            .format(good_name=element.product_name,
                    good_cost=element.cost_product)
        print(msg)
        log_rep.info(msg)

    if namespace.wname:
        print('---------------- Проблемы при записи файла --------------')
        log_rep.info('---------------- Проблемы при записи файла --------------')
        goods_info_list.write_file(namespace.wname)


if __name__ == "__main__":
    main()


