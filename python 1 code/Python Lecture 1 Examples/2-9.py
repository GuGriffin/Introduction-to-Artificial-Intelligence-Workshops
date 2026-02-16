
a=int(input('Enter the first side of the triangle:')) #Enter the first side of the triangle and convert it to an integer
b=int(input('Enter the second side of the triangle:')) #Enter the second side and convert it to an integer
c=int(input('Enter the third side of the triangle:')) #Enter the third side and convert it to an integer s=1/2*(a+b+c) #Calculate s import math #Import math module area=math.sqrt(s*(s-a)*(s-b)*(s-c)) #Import math module area=math. to integer
s=1/2*(a+b+c) #Calculate s
import math #Import math module
area=math.sqrt(s*(s-a)*(s-b)*(s-c)) #Calculate the area by calling the sqrt function
print('The area of this triangle is:',area) #Output the area of the triangle