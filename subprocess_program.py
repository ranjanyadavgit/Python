import subprocess

result = subprocess.run(['ls','-l'],capture_output=True, text=True)


print('STDOUT')
print(result.stdout)

print("STRERROR")
print(result.stderr)

print("STDOUT")
print(result.stdout)

print("error code",result.returncode)

------
Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/day-15 (main)
$ python l_subprocess.py 
STDOUT
total 1
-rw-r--r-- 1 Lenovo 197121   0 Oct 14 15:49 api.py
-rw-r--r-- 1 Lenovo 197121 256 Oct 28 02:11 l_subprocess.py

STRERROR

STDOUT
total 1
-rw-r--r-- 1 Lenovo 197121   0 Oct 14 15:49 api.py
-rw-r--r-- 1 Lenovo 197121 256 Oct 28 02:11 l_subprocess.py

error code 0


