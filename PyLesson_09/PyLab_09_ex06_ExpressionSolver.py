user = input("Enter in a mathematical expression such as 2 * 5...")
equation = user.split()

i = 0
while i < len(equation):
    if i < len(equation) and equation[i] == "*" or "/":
        if equation[i] == "*":
            equation[i] = (int(equation[i-1]) * int(equation[i+1]))
            equation.pop(i+1)
            equation.pop(i-1)
        elif equation[i] == "/":
            equation[i] = (int(equation[i-1]) / int(equation[i+1]))
            equation.pop(i+1)
            equation.pop(i-1)
    i+=1

i = 0
while i < len(equation):
    if i < len(equation) and equation[i] == "+" or "-":
        if equation[i] == "+":
            equation[i] = (int(equation[i-1]) + int(equation[i+1]))
            equation.pop(i+1)
            equation.pop(i-1)
        elif equation[i] == "-":
            equation[i] = (int(equation[i-1]) - int(equation[i+1]))
            equation.pop(i+1)
            equation.pop(i-1)
    i+=1
#do you need recursion if the expression is more complex like: 4/5*53-23???
print(equation)

    
            
