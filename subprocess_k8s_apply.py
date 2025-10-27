import subprocess

manifest_file="deployment.yaml"

result=subprocess.run(["kubectl","apply","-f",manifest_file],capture_output="True",text="True")

print(result.stdout)
