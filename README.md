# fogstream-practice
### Программа для развития практических навыков программирования на курсах от fogstream.

Программа работает с информацией о товарах, данная онформация берётся из файла "goods".

##### Версия practice_03
Содержит следующий функционал:
* Удаление товара по имени.
* Удаление самых дорогих товаров.
* Сортировка списка товаров по имени, стоимости, количеству.
* Вывод списка самых дорогих товаров.
* Вывод списка самых дешёвых товаров.
* Вывод списка заканчивающихся товаров.
* Выводит среднее квадратичное отклонение для всех цен товаров.
* Удаляет последний товар.
* Рассчитывает среднюю цену товаров.

Выводит информацию:
* Общее количество товаров.
* Средняя цена товара.
* Самый дорогой товар.
* Заканчивающийся товар.

Запускается программа из терминала командой: python practice_03.py

##### Версия practice_04

Содержит следующий функционал:
* Удаление товара по имени.
* Удаление самых дорогих товаров.
* Сортировка списка товаров по имени, стоимости, количеству.
* Вывод списка самых дорогих товаров.
* Вывод списка самых дешёвых товаров.
* Вывод списка заканчивающихся товаров.
* Выводит среднее квадратичное отклонение для всех цен товаров.
* Удаляет последний товар.
* Рассчитывает среднюю цену товаров.

Выводит информацию:
* Общее количество товаров.
* Средняя цена товара.
* Самый дорогой товар.
* Заканчивающийся товар.

Программа состоит из модулей good_info.py и reporter.py, запускается из терминала командой: python reporter.py

##### Версия practice_05

Содержит следующий функционал:
* Удаление товара по имени.
* Удаление самых дорогих товаров.
* Сортировка списка товаров по имени, стоимости, количеству.
* Вывод списка самых дорогих товаров.
* Вывод списка самых дешёвых товаров.
* Вывод списка заканчивающихся товаров.
* Выводит среднее квадратичное отклонение для всех цен товаров.
* Удаляет последний товар.
* Рассчитывает среднюю цену товаров.

Выводит информацию:
* Общее количество товаров.
* Средняя цена товара.
* Самый дорогой товар.
* Заканчивающийся товар.

Программа состоит из модулей good_info.py и reporter.py, запускается из терминала командой: python reporter.py

Программа reporter.py работает с данными из указанных файлов, имеет два не обязательных параметра -rname и -wname.
python reporter.py 
по умолчанию считывает данные из goods2.info, находящийся в том же каталоге

python reporter.py -rname read.info 
считывает данные с указанного файла read.info, находящийся в том же каталоге

python reporter.py -rname d:\read.info 
считывает данные с указанного файла read.info

python reporter.py -wname wr.txt 
считывает данные из goods2.info и записывает в wr.txt, находящийся в том же каталоге 

python reporter.py -rname read.info -wname d:\new\wr.txt
считывает данные с указанного файла read.info и записывает в wr.txt, находящийся по указанному пути

Так же программа формирует в своём каталоге файл output.log. Там фиксируется результат работы программы и возникающие ошибки.














