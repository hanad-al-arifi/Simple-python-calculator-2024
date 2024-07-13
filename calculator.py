# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   ##This function adds two numbers

   return x + y

def subtract(x, y):
  ##This function subtracts two numbers

   return x - y

def multiply(x, y):
   ##This function multiplies two numbers

   return x * y

def divide(x, y):
   ##This function divides two numbers

   return x / y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))
else:
    print("Invalid input")
