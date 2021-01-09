# Пришло время разместить свой проект в сети
# для того чтобы любой человек смог получить
# доступ к нему
# также хотелось бы отслеживать версию данного
# проекта чтобы не создавать кучу папок для разных
# версий своего проекта

# для выполнения задания используйте готовый
# выполненный проект по задаче task2-classes

# Задание 1: установите систему контроля версий Git:
# https://git-scm.com/downloads, ознакомьтесь с ней
# Команды: https://proglib.io/p/git-cheatsheet/
# Первоое знакомство:
# https://medium.com/nuances-of-programming/знакомство-с-git-и-github-руководство-для-начинающих-54ea2567d76c

# Задание 2: Зарегестрируйтесь на https://github.com

# Задание 3: Создайте свой репозиторий
# https://vertex-academy.com/tutorials/ru/kak-sozdat-repozitorij-na-github/

# Задание 4(опционально): Установите GitHub для Windows ил другой Git клиент
# https://desktop.github.com
# Дополнительная информация:
# https://o7planning.org/ru/10283/using-github-with-github-desktop
# Другие gui клиенты для git
# https://techrocks.ru/2020/04/24/best-git-gui-for-mac-linux-windows/

# Задание 5: Разместите проект на своём репозитории в github.com

# Задание 6:  оформите файл README.md с описанием вашего проекта
# http://ilfire.ru/kompyutery/shpargalka-po-sintaksisu-markdown-markdaun-so-vsemi-samymi-populyarnymi-tegami/
'''
можно поставить typora для редактирования файлов  .md
'''
# задание 7:
# Реализуйте функции
# __len__() для GoodInfolist
# get_std() получает среднее отклонение для всех цен товаров
# remove_last() удаляет последний товар

# Сделайте commit и запушьте изменения (push) в ветку мастер(main)
# вашего репозитория на github


class GoodInfo:
    """
    Класс GoodInfo используется для хранения информации о товаре.
    
    Attributes
    ----------
    product_name (str): название товара
    cost_product (int): цена товара
    number_goods (int): количество товара
    """

    product_name = 'product_name'
    number_goods = 'number_goods'
    cost_product = 'cost_product'

    def __init__(self, product_name, cost_product, number_goods):
        self.product_name = product_name
        self.cost_product = cost_product
        self.number_goods = number_goods

    def __str__(self):
        # переопределяем вывод         
        return 'Название товара: {}. Цена: {}руб. Количество: {}.'\
               .format(self.product_name, self.cost_product, self.number_goods)


class GoodInfoList:
    """
    Класс GoodInfoList работы со списком товаров.
    
    Attributes
    ----------
    goods_list (:obj: str, int, int): список объектов GoodInfo


    Methods
    -------
    data_control()
    проверяет корректность вводимых данных

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

    def ending_products(self):
    выводит список заканчивающихся товаров
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
        line_ok = []
        # проверка данных
        for line in strings_list:
            if line == '\n':
                print('Пустая строка в файле!')
            elif len(line) < 7:
                print('Отсутствуют данные в файле!')
            else:
                # формируем список с проверенными записями
                line_ok.append(line)
        return line_ok

    def read_file(self, file_path):
        """
        Метод считывает данные из файла
        :param file_path: имя файла
        :type file_path: str
        """
        file_obj = open(file_path, "r", encoding="utf-8")
        # получаем список в котором содержится строки из файла
        strings_list = file_obj.readlines()
        file_obj.close()
        for line in GoodInfoList.data_control(strings_list):
            line_split = line.split(":")
            self.add(GoodInfo(line_split[0],
                              int(line_split[1]),
                              int(line_split[2].replace("\n", ""))))

    def add(self, good_info):
        """
        Метод добавляет товар
        :param good_info: объект GoodInfo с информацией о товаре
        :type good_info: (:obj: str, int, int): объект GoodInfo
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

    def __getitem__(self, key):
        # переопределяем вывода по индексу
        return self.goods_list[key]

    def __str__(self):
        # переопределяем вывод
        result_list = []
        for element in self.goods_list:
            result_list.append(str(element))
        return '\n'.join(result_list)

# -----------------------------------------


goods_info_list = GoodInfoList()
goods_info_list.read_file('goods')

print("Общее количество товаров - {total_count}"
      .format(total_count=len(goods_info_list.goods_list)))

sum = 0
for element in goods_info_list.goods_list:
    sum += element.cost_product
print("Средняя цена товара - {average_cost}"
      .format(average_cost=sum / len(goods_info_list.goods_list)))

for element in goods_info_list.most_expensive_products():
    print("Самый дорогой товар - {good_name}, Цена - {good_cost}"
          .format(good_name=element.product_name,
                  good_cost=element.cost_product))

for element in goods_info_list.ending_products():
    print("Заканчивается товар - {good_name}, Осталось - {good_cost}"
          .format(good_name=element.product_name,
                  good_cost=element.cost_product))
