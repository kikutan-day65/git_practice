def get_math_function(operation):
    def add(num1, num2):
        return num1 + num2

    def subtraction(num1, num2):
        return num1 - num2

    def multiplication(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2


    if operation == "+":
        return add
    elif operation == "-":
        return subtraction
    elif operation == "*":
        return multiplication
    elif operation == "/":
        return division
    

add_func = get_math_function("+")
sub_func = get_math_function("-")
mul_func = get_math_function("*")
div_func = get_math_function("/")


print(add_func(10, 10))
print(sub_func(24, 17))
