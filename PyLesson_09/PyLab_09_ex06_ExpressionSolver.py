user = input("Enter in a mathematical expression such as 2 * 5...")
equation = user.split(" ")

i = 0
while i < len(equation):
    if i < len(equation) and equation[i] == "*" or "/":
        if equation[i] == "*":
            equation[i] = (int(equation[i-1]) * int(equation[i+1]))
        else:
            equation[i] = (int(equation[i-1]) / int(equation[i+1]))
        equation.remove[i-1]
        equation.remove[i]
    i+=1

i = 0
while i < len(equation):
    if i < len(equation) and equation[i] == "+" or "-":
        if equation[i] == "+":
            equation[i] = (int(equation[i-1]) + int(equation[i+1]))
        else:
            equation[i] = (int(equation[i-1]) - int(equation[i+1]))
        equation.remove[i-1]
        equation.remove[i]
    i+=1

print(equation)

    
            
