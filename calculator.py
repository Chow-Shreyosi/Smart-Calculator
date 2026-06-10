def add(num1, num2):
        return num1 + num2

def sub(num1, num2):
        return num1 - num2
        
def mul(num1, num2):
       return num1 * num2
       
def div(num1, num2):
    if num2 != 0:
       return num1 / num2
    else:
            return "invalid"
    
def mod(num1, num2):
       return num1 % num2
    
def pow(num1, num2): 
       return num1 ** num2
       
def sq(num1):
       return num1 ** 2
       
def sqrt (num1):
        return num1 ** 0.5
      
history = []


print("SMART CALCULATOR")
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
print("Modulous")
print("Power")
print("Square")
print("Square root")
print("History")
operator = input("Enter operand:")
if  operator == "+":
            result = add(num1, num2)
elif  operator == "-":
             result = sub(num1, num2)
elif  operator == "*":
             result = mul(num1, num2)
elif  operator == "/":
             result = div(num1, num2)
elif  operator == "%":
             result = mod(num1, num2)
elif operator == "^":
             result = pow(num1, num2)
elif operator == "^2":
             result = sq(num1)
elif operator == "sqrt":
              result = sqrt(num1)
else:
                      print("invalid")
                      
history.append(result)
print("Result =", result)
print("History =", history)
 