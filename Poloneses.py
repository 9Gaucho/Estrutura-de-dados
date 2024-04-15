def poloneses(expression):
    values = []

    for index in expression.split():
        if index.isdigit():
            values.append(float(index))
        else:
            num2 = values.pop()
            num1 = values.pop()
            if index == '+':
                values.append(num1 + num2)
            elif index == '-':
                values.append(num1 - num2)
            elif index == '*':
                values.append(num1 * num2)
            elif index == '/':
                values.append(num1 / num2)
            elif index == '^':
                values.append(num1 ** num2)

    return values[0]

# Exemplo
equation1 = "2 3 + 4 *"
equation2 = "10 5 - 2 +"
equation3 = "8 6 * 2 /"
equation4 = "2 3 ^"
equation5 = "5 2 1 + ^"

print("Resultado 1:", poloneses(equation1))
print("Resultado 2:", poloneses(equation2))
print("Resultado 3:", poloneses(equation3))
print("Resultado 4:", poloneses(equation4))
print("Resultado 5:", poloneses(equation5))
