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

from good_info import GoodInfoList

if __name__ == "__main__":

	goods_info_list = GoodInfoList()
	goods_info_list.read_file('goods2_test.info')

	print('------------------- Содержимое файла -----------------')

	print(goods_info_list)

	print()    
	print('Сортировка по name и по убыванию')
	goods_info_list.sort('name', True)
	for element in goods_info_list.goods_list:
		print(element)

	print()
	print('Cреднее отклонение для всех цен товаров')
	print(goods_info_list.get_std())

	print()    
	print('Сортировка по cost и по возрастанию')
	goods_info_list.sort('cost', False)
	for element in goods_info_list.goods_list:
		print(element)

	print()
	print('Список самых дорогих товаров')
	for element in goods_info_list.most_expensive_products():
		print(element)

	print()
	print('Список самых дешёвых товаров')
	for element in goods_info_list.cheapest_product():
		print(element)

	print()	
	print('Средняя цена')
	print(goods_info_list.average_price())

	print()	
	print('Список заканчивающихся товаров')
	for element in goods_info_list.ending_products():
		print(element)

	print()
	print('Список после удаления товара: сахар 1кг')
	goods_info_list.del_good()
	for elеment in goods_info_list.goods_list:
		print(elеment)


	print()
	print('Список после удаления самых дорогих товаров')
	goods_info_list.remove_expensive()
	print(goods_info_list)

	print()
	print('Обращение по индексу без переопределения __getitem__')
	print('{}:{}:{}'.format(goods_info_list.goods_list[0].product_name, goods_info_list.goods_list[0].cost_product, goods_info_list.goods_list[0].number_goods))

	print()
	print('Обращение по индексу с переопределённым __getitem__')
	print('{}:{}:{}'.format(goods_info_list[0].product_name, goods_info_list[0].cost_product, goods_info_list[0].number_goods))

	print()
	name = 'хлеб серый хлебозавод'
	print('Обращение по индексу, в качестве индекса - название товара')
	for element in goods_info_list[name]:
		print('{}:{}:{}'.format(element.product_name, element.cost_product, element.number_goods))


	print()
	print('Вывод объекта')
	print(goods_info_list)

	print()
	print('Количество товаров')
	print(len(goods_info_list))

	print()
	print('До удаления последнего товара')
	print(goods_info_list)

	goods_info_list.remove_last()
	print()
	print('После удаления последнего товара')
	print(goods_info_list)

'''
	print()
	print('Удаление просроченного товара')
	for element in goods_info_list.del_expired_product():
		print(element)

'''

