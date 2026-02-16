stuInfos = []  # List to store all student information

def printMenu():  # Function to print the menu
    print("=" * 20)
    print(" Student Management System V1.0 ")
    print("1. Add Student Information")
    print("2. Delete Student Information")
    print("3. Show All Student Information")
    print("0. Exit System")
    print("=" * 20)

# Function to add a student's information
def addStuInfo():
    newNum = input("Enter the student's ID: ")  # Prompt to enter student ID
    newName = input("Enter the student's name: ")  # Prompt to enter student name
    newSex = input("Enter the student's gender (Male/Female): ")  # Prompt to enter student gender
    newInfo = {}  # Create a dictionary to store student info
    # Assign values to dictionary
    newInfo['num'] = newNum
    newInfo['name'] = newName
    newInfo['gender'] = newGender
    stuInfos.append(newInfo)  # Add the student's info to the list

# Function to delete a student's information
def delStuInfo(student):
    del_num = input("Enter the student ID to delete: ")  # Prompt to enter student ID for deletion
    for stu in student:  # Iterate through the list of students
        if stu['num'] == del_num:  # Check if the ID matches the input ID
            student.remove(stu)  # Remove the student from the list

# Function to display all student information
def showStuInfo():
    print("=" * 20)
    print("Student information:")
    print("=" * 20)
    print("No.    ID    Name   Gender")  # Header
    i = 1
    # Iterate through the list of students and print their details
    for tempInfo in stuInfos:
        print(f"{i}      {tempInfo['num']}      {tempInfo['name']}     {tempInfo['Gender']}")
        i += 1

# Main function to control the flow of the program
def main():
    while True:
        printMenu()  # Print the menu
        key = input("Enter the corresponding number for the function: ")  # Get user input
        if key == '1':  # Add student information
            addStuInfo()
        if key == '2':  # Delete student information
            delStuInfo(stuInfos)
        elif key == '3':  # Show student information
            showStuInfo()
        elif key == '0':  # Exit the program
            quit_con = input("Are you sure you want to exit? (Yes or No): ")
            if quit_con == 'Yes':
                break

# Start the program
main()
