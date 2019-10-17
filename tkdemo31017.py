import subprocess
f = open("test.log", "a", encoding="utf-8")
# windows: dir
command = "ls -al"
# windows: shell=True
result = subprocess.run(command, shell=True, stdout=f)
print(result)
f.close()