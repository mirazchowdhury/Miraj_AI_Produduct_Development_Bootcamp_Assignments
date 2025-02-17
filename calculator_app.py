def calculator(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

value_1 = float(input("Enter first value : "))
value_2 = float(input("Enter second value: "))

result= calculator(value_1,value_2)
print(result)
