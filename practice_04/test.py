# a = ''
#a=int(input())
#c = int(a)

c=2


if isinstance(c, int):
    print('int')
elif isinstance(c, str):
    print('str')
elif isinstance(c, float):
    print('float')  

from datetime import date, timedelta

line = '2020-01-02'
production_date = date.fromisoformat(line)

v = '-1'

if int(v) < 0:
    print('-1')
