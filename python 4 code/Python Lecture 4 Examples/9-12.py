stuInfos = []  # used to store all student information
def printMenu():  # print function prompt print("="*20)
Print "Student Management System V2.0"
Print "1. Add student information"
Print "2. Delete student information"
Print "3. Display all student information"
Print "4. Save data"
Print "5. Restore data"
Print "0. Exit system" print("="*20)
#Add a student's information def addStuInfo():
newNum = input("Please input the new student's student ID:")  #prompt and retrieve the student ID
newName = input("Please input the new student's name:")  #prompt and retrieve the student's name
newSex = input("Please input the new student's gender (male/female):")  #prompt and retrieve the student's gender
newInfo = {}  #define a dictionary
#Assign values newInfo['num'] = newNum
newInfo['name'] = newName
newInfo['sex'] = newSex
stuInfos.append(newInfo)  #Add the element to the list
#Delete a student information def delStuInfo(student):
del_num = input("Please input the student ID to be deleted:")  #prompt and retrieve student ID
for stu in student:                         #iterate through the list
if stu['num'] == del_num:               #check if it matches the input ID
student.remove(stu)                 #delete the student information
#display all student information def showStuInfo():
print("=" * 20)
"The student's information is as follows: print("=" * 20)
Print("Serial Number   Student ID   Name   Gender") i = 1
#Iterate through the list that stores the student information and output the detailed information of each student. for tempInfo in stuInfos:
print("%d      %s      %s     %s" % (i, tempInfo['num'],tempInfo['name'], tempInfo['sex']))
i += 1
#Save to file def save_file():
with open('student.txt','w') as file:
file.write(str(stuInfos))  #converts the dictionary to a string and writes it to the file
#Restore data def recover_data():
global stuInfos
with open('student.txt','r') as file:
content = file.read()
stuInfos = eval(content)  #Convert the data back to its original type
#The main function controls the flow of the entire program. def main():
while True:
printMenu()                     #打印功能菜单
key = input("Please input the number corresponding to the function： ")#获取用户输入
if key == '1'：                      #添加学生信息

"printMenu()" 输出功能菜单。
"input()" 函数用于从用户处获取输入。
"key" 是用户输入的数字。
"if" 语句用于判断用户输入是否等于数字"1"。
如果等于，则执行添加学生信息的操作。 addStuInfo()
elif key == '2':  #delete student information delStuInfo(stuInfos)
elif key == '3':  #display student information showStuInfo()
elif key == '4':
save_file()
elif key == '5':
recover_data()
elif key == '0':                        #exit loop
quit_con = input("Are you sure you want to exit? (Yes or No):") if quit_con == 'Yes':
break
`main()` #calling the `main` function
while True:
printMenu()
key = input("Please input the number corresponding to the function： ")
if key == '1'：

"printMenu()"
"key = input("Please input the number corresponding to the function： ")"
"if key == '1'："
"#ADD studnet Info" 
"printMenu()" outputs the function menu.
"input()" function is used to obtain input from the user.
"key" is the numerical input from the user.
"if" statement is used to determine whether the user's input is equal to the number "1".
If it is equal, then the operation of adding student information is performed. addStuInfo()
elif key == '2':  #delete student information delStuInfo(stuInfos)
elif key == '3':  #display student information showStuInfo()
elif key == '4':
save_file()
elif key == '5':
recover_data()
elif key == '0':                        #exit loop
quit_con = input("Are you sure you want to exit? (Yes or No):") if quit_con == 'Yes':
break
`main()` #calling the `main` function
