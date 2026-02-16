import math #Import the math module
a=int(input('Please enter the first side of the triangle: ')) #Enter the first side and convert it to an integer
b=int(input('Please enter the second side of the triangle: ')) #Enter the second side and convert it to an integer
c=int(input('Please enter the third side of the triangle: ')) #Enter the third side and convert it to an integer
s=1/2*(a+b+c) #Calculate s
area=math.sqrt(s*(s-a)*(s-b)*(s-c)) #Call the sqrt function to calculate the area
print('The area of this triangle is: ', area) #Output the area of the triangle