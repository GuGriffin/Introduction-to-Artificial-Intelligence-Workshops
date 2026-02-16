f = open("1.txt","r")
content = f.read()
list_1 = content.split()
for i in range(len(list_1)):
	list_1[i] = int(list_1[i])
list_1.sort()
print(list_1)
f.close()