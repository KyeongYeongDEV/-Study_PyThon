#파일 읽고 쓰기

f = open("새파일.txt", 'w')
f.close()
#프로그램을 실행해보면 디렉터리에 새로운 파일 하나 생성된 것을 확인할 수 있을 것이다.
#이 파이을 생성하기 위해 우리는 파이썬 내장 함수 open을 사용하였다
#open함수는 다음 과 같이 "파일 열기 모드"를 입력값으로 받고 결괏값으로 파일 객체를 돌려준다.

#'r' 읽기모드 - 파일을 읽기만 할 때 사용
#'w' 쓰기모드 - 파일에 내용을 쓸 때 사용
#'a' 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

#만약 새파일.txt 파일을 C:/doit 디렉터리에 생성하고 싶다면 
f = open("C:/doit/새파일.txt", 'w')
f.close()


#파일을 쓰기 모드로 열어 출력값 적기
f = open("C:/doit/새파일.txt", 'w')
for i in range(1,10):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
#위의 코드를 실행 시키면 메모장에 출력값이 적혀 저장되어 있다

#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
#readline 함수 이용하기
f = open("C:/doit/새파일.txt", 'r') #읽기 모드로 연 후
line = f.readline() #readline을 사용해서 첫 번째 줄을 읽어 출력하는 경우이다
print(line)
f.close()

#모든 줄을 읽어서 화면에 출력하고 싶다면
f = open("C:/doit/새파일.txt", 'r')
while True: #무한 루프 안에서 
    line = f.readline() #readline을 사용해서 계속 한 줄씩 게속 읽는다
    if not line: break #더이상 읽을 줄이 없으면 break
    print(line)
f.close()

#키보드로 입력받는 위와 비슷한 예제
while True:
    data = input()
    if not data: break
    print(data)

#readlines 함수 사용하기
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
#readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.

#줄 바꿈(\n)문자 제거하기 strip()
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

#read() 함수 사용하기
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기
#쓰기모드 'w'로 파일을 열 떄 이미 존재하는 파일을 열면 
#그 파일의 내용이 모두 사라지게 된다
#하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가를 하려면
#추가모드 'a'로 열면 된다.
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#while문과 함께 사용하기
#while문은 close() 역할을 자동으로 해준다.
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")