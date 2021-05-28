
file = open("abc.txt")
data = " "
for i in range(5):
    data = file.read()
    info = data.split()
    print(info)