#비트 연산은 두 수의 각각이 비트를 연산하여 수를 내어주는 연산

a= int(input("첫 번째 정수 : "))
b= int(input("두 번째 정수 : "))

print(a, "~", b, "=", (~a))
print(a, "&", b, "=", (a&b))
print(a, "^", b, "=", (a^b))
print(a, "|", b, "=", (a|b))

#shift 연산자는 각 비트를 주어진 수만큼 이동시키는 연산
print(a, "<<", b, "=", (a<<b))
print(a, ">>", b, "=", (a>>b))

