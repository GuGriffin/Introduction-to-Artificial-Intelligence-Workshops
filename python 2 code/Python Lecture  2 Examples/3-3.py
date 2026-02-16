score = int(input("Please enter a percentage score: "))  # Input the value of the score and convert it to an integer

if score > 100 or score < 0:  # If the score is outside the valid range (0–100), display an error message
    print("Invalid input")
elif score >= 90:  # If the score is greater than or equal to 90 and less than or equal to 100, output "Excellent"
    print("Excellent")
elif score >= 80:  # If the score is greater than or equal to 80 and less than 90, output "Good"
    print("Good")
elif score >= 70:  # If the score is greater than or equal to 70 and less than 80, output "Average"
    print("Average")
elif score >= 60:  # If the score is greater than or equal to 60 and less than 70, output "Pass"
    print("Pass")
else:  # If none of the above conditions are met
    print("Fail")  # Output "Fail"
