num = int(input("하나의 수를 입력하세요 : "))

result = " 3의 배수도 5의 배수도 아니다. "

if num%3 == 0 :
     result = " 3의 배수입니다. "

if num%5 == 0 :
     result = " 5의 배수입니다. "

if num%3 == 0 and num%5 == 0 :
     result = " 3의 배수이고 5의 배수입니다. "

print(result)
