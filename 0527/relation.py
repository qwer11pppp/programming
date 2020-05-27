#관계(비교)연산은두 수의 대소 혹은 동등관계를 연산하여
#boolean(True,False) 값을 내어주는 연산

a= int(input("첫 번째 정수 : "))
b= int(input("두 번째 정수 : "))

print(a, "<", b, "=", (a<b))
print(a, "<=", b, "=", (a<=b))
print(a, ">", b, "=", (a>b))
print(a, ">=", b, "=", (a>=b))
print(a, "==", b, "=", (a==b))
print(a, "!=", b, "=", (a!=b))
