import os


files = []
x = 0
i = 10
answ = {}

for dirpath, dirnames, filenames in os.walk('/home/splakh2201/Рабочий стол'):
    for file in filenames:
        path1 = os.path.join(dirpath, file)
        files.append(os.stat(path1).st_size)
max_size = max(files)

while x != (len(str(max_size))):
    answ.setdefault(i, 0)
    x += 1
    i *= 10

for name in files:
    answ[10**len(str(name))] += 1
print(answ)


