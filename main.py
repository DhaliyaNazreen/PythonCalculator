from replit import clear

from logo import logo


def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

def modulus(a,b):
  return a%b

def exp(a,b):
  return a^b

operations = {
              "+" :add , 
              "-":subtract, 
              "*": multiply,
              "/":divide,
              
              
            }
def calculator():
  print("Welcome to Calculator")
  print(logo)
  
  
  num_1 = float(input('Enter the first number: '))
    
  for key in operations:
    print(key)
  continue_var = True
  while continue_var:
    operation_symbol = input("Pick an operation from above symbols: ")
    num_2 = float(input('Enter the next number: '))
    
    calculation_function = operations[operation_symbol]
    result = calculation_function(num_1, num_2)
    
    print(f"{num_1} {operation_symbol} {num_2} = {result}")
    
    continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  
    if continue_calc == "y":
        num_1 = result
  
    else:
      continue_var = False
      clear()
      calculator()

calculator()
    
  
