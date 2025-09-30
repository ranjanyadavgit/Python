import sys

type = sys.argv[1]

if type == "t2.micro":
  print("we will charge you 2 dollar per day")
elif type == "t2.medium":
  print("we will charge you 4 dollar per day")
elif type == "t2.xlarge":
  print("we will charge you 8 dollar per day")
else:
  print("ivalid input")

Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/day-7
$ python main.py t2.xlarge
we will charge 8 dollar per day
