
$ python myscript.py arg1 arg2 arg3
Script name: myscript.py
First argument: arg1
Second argument: arg2
Third argument: arg3

Lenovo@DESKTOP-M5DT73G MINGW64 ~ (feature/new)
$ cat myscript.py
import sys

print("Script name:", sys.argv[0])
print("First argument:", sys.argv[1])
print("Second argument:", sys.argv[2])
print("Third argument:", sys.argv[3])

