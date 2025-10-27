import subprocess

# Run kubectl command
result = subprocess.run(
    ["kubectl", "get", "pods", "-n", "default"],
    capture_output=True,
    text=True
)

print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)
print("Return Code:", result.returncode)

-----------------
Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/day-15 (main)
$ python l_subprocess.py 
STDOUT:
 
STDERR:
 E1028 02:24:27.451095    4952 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
E1028 02:24:27.459048    4952 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
E1028 02:24:27.463811    4952 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
E1028 02:24:27.468428    4952 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
E1028 02:24:27.473594    4952 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
Unable to connect to the server: dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it.

Return Code: 1
