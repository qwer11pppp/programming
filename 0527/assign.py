#할당연산은 오른쪽에 있는 수시(constant variable operator function)
#을 연산 하여 왼쪽에 있는 변수를 할당하는 연산자

a=int(input("첫 번째 정수 : "))
b=int(input("두 번째 정수 : "))

a=a+1
print("a=b의 결과 = ",(a))
a+=b
print("a+=b의 결과 =",(a))
#+ - * / % // **
a<<=b
print("a<<=b의 결과 =",(a))
a &=b
print("a&=b의 결과 =",(a))
