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

'''
Модуль good_info содержит в себе классы для работы с информациеё о товарах.

Classes
--------
GoodInfo
GoodInfoList

'''


class GoodInfo:
    """
    Класс GoodInfo используется для хранения информации о товаре.
    
    Attributes
    ----------
    product_name (str): название товара
    cost_product (int): цена товара
    number_goods (int): количество товара
    delivery_date (datetime.date): дата поставки товара
    storage_time (int): время хранения(в днях)
    """

    product_name = 'product_name'
    number_goods = 'number_goods'
    cost_product = 'cost_product'
    delivery_date = "delivery_date"
    storage_time = 'storage_time'

    def __init__(self, product_name, cost_product,
                 number_goods, delivery_date, storage_time):
        self.product_name = product_name
        self.cost_product = cost_product
        self.number_goods = number_goods
        self.delivery_date = delivery_date
        self.storage_time = storage_time

    def __str__(self):
        # переопределяем вывод         
        return 'Название товара: {p_n}. Цена: {c_p}руб. Количество: {n_g}. Дата поставки: {d_d}. Время хранения: {s_t} дней.'.format(p_n=self.product_name, c_p=self.cost_product, n_g=self.number_goods, d_d=self.delivery_date, s_t=self.storage_time)


class GoodInfoList:
    """
    Класс GoodInfoList работы со списком товаров.
    
    Attributes
    ----------
    goods_list (:goods_info_list: str, int, int, datetime.date, int):
    список объектов GoodInfo


    Methods
    -------
    data_control()
    проверяет корректность вводимых данных

    del_expired_product()
    удаляет товар с истёкшим сроком годности
	
    read_file(file_path)
    считывает данные из файла file_path

    add(good_info):
    добавляет в goods_list иформацию о товаре

    del_good(name_good)
    удаляет товар с наименованием name_good

    remove_expensive()
    удаляет самые дорогие товары

    sort(key, rev=False)
    сортирует список товаров по ключу key: по имени товара (name),
    по стоимости (cost), по количеству (count)
    rev задаёт порядок сортировки, False - по возрастанию, True - по убыванию

    most_expensive_products()
    выводит список самых дорогих товаров

    cheapest_product()
    выводит список самых дешёвых товаров

    def ending_products():
    выводит список заканчивающихся товаров

    get_std():
    выводит среднее отклонение для всех цен товаров

    remove_last():
    удаляет последний товар

	average_price()
	выводит среднюю цену товаров
    """
    
    goods_list = None

    def __init__(self):
        self.goods_list = []

    @staticmethod
    def data_control(strings_list):
        """
        Метод проверяет корректность вводимых данных
        :param strings_list: список строк из файла
        :type strings_list: list
        :return: список корректных строк из файла
        :rtype: list
        """
        from datetime import date
        line_ok = []
        # проверка данных
        for line in strings_list:
            if line == '\n':
                print('Пустая строка в файле!')
            # предпологается, что в строке должно быть минимум 9 символов
            elif len(line) < 9:
                print('Отсутствуют данные в строке!')
            else:
                line_split = line.split(":")
                delivery_date = date.fromisoformat(line_split[3])
                if date.today() < delivery_date:
                    print('Дата поставки больше текущей!')
                else:
                    # формируем список с проверенными записями
                    line_ok.append(line)
        return line_ok
    
    def del_expired_product(self):
        """
        Метод удаляет товар с истёкшим сроком годности
        :return: список не просроченных товаров
        :rtype: list
        """
        from datetime import date, timedelta
        good_product = []
        for element in self.goods_list:
            # расчитываем окончание срока годности
            expiration_date = element.delivery_date +\
                              timedelta(days=element.storage_time)
            #print(expiration_date)
            if date.today() > expiration_date:
                print('Истёк срок годности: {}'.format(element.product_name))
            else:
                good_product.append(element)
        return good_product

    def read_file(self, file_path):
        """
        Метод считывает данные из файла
        :param file_path: имя файла
        :type file_path: str
        """
        from datetime import date
        file_goods_info_list = open(file_path, "r", encoding="utf-8")
        # получаем список в котором содержится строки из файла
        strings_list = file_goods_info_list.readlines()
        file_goods_info_list.close()
        for line in GoodInfoList.data_control(strings_list):
            line_split = line.split(":")
            product_name = line_split[0]
            cost_product = int(line_split[1])
            number_goods = int(line_split[2])
            delivery_date = date.fromisoformat(line_split[3])
            storage_time = int(line_split[4].replace("\n", ""))
            self.add(GoodInfo(product_name,
                              cost_product,
                              number_goods,
                              delivery_date,
                              storage_time))

    def add(self, good_info):
        """
        Метод добавляет товар
        :param good_info: объект GoodInfo с информацией о товаре
        :type good_info:
        (:goods_info_list: str, int, int, date): объект GoodInfo
        """
        self.goods_list.append(good_info)

    def del_good(self, name_good='сахар 1кг'):
        """
        Метод удаляет товар
        :param name_good: названеи товара
        :type name_good: str
        """
        for element in self.goods_list:
            if element.product_name == name_good:
                self.goods_list.remove(element)

    def remove_expensive(self):
        """
        Метод удаляет самые дорогие товары
        """
        for element in self.most_expensive_products():
            self.goods_list.remove(element)

    def sort(self, key, rev=False):
        """
        Метод сортирует список товаров по ключу и по возрастанию или убыванию.
        :param key: сортировка по имени товара (name),
        по стоимости (cost), по количеству (count)
        :type key: str
        :param rev: задаёт порядок сортировки,
        False - по возрастанию, True - по убыванию
        :type key: boolean
        """
        if key == 'name':
            self.goods_list.sort(key=lambda x:
            x.product_name.lower(), reverse=rev)
        elif key == 'cost':
            self.goods_list.sort(key=lambda x: x.cost_product, reverse=rev)
        else:
            self.goods_list.sort(key=lambda x: x.number_goods, reverse=rev)

    def most_expensive_products(self):
        """
        Метод выводит список самых дорогих товаров
        :return: список товаров с наибольшей ценой
        :rtype: list[GoodInfo(str, int, int)]
        """
        max_price = 0
        max_price_list = []
        for element in self.goods_list:
            if float(element.cost_product) == max_price:
                max_price_list.append(element)
            elif float(element.cost_product) > max_price:
                max_price_list = []
                max_price_list.append(element)
                max_price = float(element.cost_product)
        return max_price_list

    def cheapest_product(self):
        """
        Метод выводит список самых дешёвых товаров
        :return: список товаров с наименьшей ценой
        :rtype: list[GoodInfo(str, int, int)]
        """
        min_price = 999999999
        min_price_list = []
        for element in self.goods_list:
            if float(element.cost_product) == min_price:
                min_price_list.append(element)
            elif float(element.cost_product) < min_price:
                min_price_list = []
                min_price_list.append(element)
                min_price = float(element.cost_product)
        return min_price_list

    def ending_products(self):
        """
        Метод выводит список заканчивающихся товаров.
        :return: список заканчивающихся товаров 
        :rtype: list[GoodInfo(str, int, int)]
        """
        quantity_goods = 999999999
        ending_products_list = []
        for element in self.goods_list:
            if float(element.number_goods) == quantity_goods:
                ending_products_list.append(element)
            elif float(element.number_goods) < quantity_goods:
                ending_products_list = []
                ending_products_list.append(element)
                quantity_goods = float(element.number_goods)
        return ending_products_list

    def get_std(self):
        """
        Метод выводит среднее отклонение для всех цен товаров.
        :return: значение отклонения 
        :rtype: float
        """
        sum_cost = 0
        diffs = 0
        for element in self.goods_list:
            sum_cost += element.cost_product
        arithmetic_mean = sum_cost / len(self.goods_list)
        for element in self.goods_list:
            diffs += pow(element.cost_product - arithmetic_mean, 2)
        return  pow(diffs / len(self.goods_list), 0.5)

    def remove_last(self):
        """
        Метод удаляет последний товар.
        """
        self.goods_list.pop()

    def average_price(self):
        """
        Метод выводит среднюю цену товаров.
        :return: средняя цена товара 
        :rtype: float
        """
        sum = 0
        for element in self.goods_list:
            sum += element.cost_product
        return sum / len(self.goods_list)
    
    def __getitem__(self, key):
        # переопределяем вывода по индексу
        # когда обращаемся к объёкту класса GoodInfoList через[]
        # то возвращает элемент списка goods_list
        result_list = []
        if isinstance(key, int):
            return self.goods_list[key]
        else:
            # если в качестве ключа передаётся имя товара
            # то возвращается список товаров с этим именем
            for element in self.goods_list:
                if key == element.product_name:
                    result_list.append(element)
            return result_list
			
    def __str__(self):
        # переопределяем вывод
        result_list = []
        for element in self.goods_list:
            # str(element) вызывает __str__ GoodInfo
            result_list.append(str(element))
        return '\n'.join(result_list)

    def __len__(self):
        return len(self.goods_list)




