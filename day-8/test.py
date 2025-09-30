
servers=['web-server-1','web-server-2','web-server3']

print(servers)

servers.append('web-servers-4')
print(servers)

servers2=('database-server-1','database-server-2','database-server-3')
print(servers2)

servers2.append('database-server-4')
print(servers2)

Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/day-8
$ python main.py 
['web-server-1', 'web-server-2', 'web-server3']
['web-server-1', 'web-server-2', 'web-server3', 'web-servers-4']
('database-server-1', 'database-server-2', 'database-server-3')
Traceback (most recent call last):
  File "C:\Python\day-8\main.py", line 12, in <module>
    servers2.append('database-server-4')
    ^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
