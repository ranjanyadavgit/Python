import subprocess
directory="/var/log"

result=subprocess.run(["du", "-sh",directory], capture_output=True, text=True)

print(f"Disk usage for {directory}: {result.stdout.strip()}")

