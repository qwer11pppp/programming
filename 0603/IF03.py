#File name : if03.py
#IF (조건문)에서 조건문이 True이면 if 아래에 있는 명령어들이 실행
#   그렇지 않고 elif  조건문이  True이면 elif 아래에 있는 명령들이 실행
#   그렇지 않고 elif  조건문이  True이면 elif 아래에 있는 명령들이 실행
#...
#그렇지 않으면 ( 위의 조건들ㅇ True가 아니면) else  아래에 있는 명령들이 실핼

a = int(input("점수 입력 : "))

if a >= 90:
    print("당신의 학접은 A 입니다.")
elif a >= 80:
    print("당신의 학점은B입니다. ")
elif a >= 70:
    print("당신의 학점은 C입니다. ")
elif a >= 60:
    print("당신의 학점은 D입니다. ")
else:
    print("당신의 학점은 F입니다. ")


print("수고하셨습니다. ")

