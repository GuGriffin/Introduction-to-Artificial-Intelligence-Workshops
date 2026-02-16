arr = []
length = int(input("请输入数字的总个数（必须为奇数）:"))
i = 0
while i < length:
   num =  int(input("输入第%d个数字:"%(i+1)))
   arr.append(num)
   i+=1
arr.sort()
index = int(length/2)
print(arr[index])