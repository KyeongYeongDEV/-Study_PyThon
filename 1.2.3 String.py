#문자열 인덱싱
#문자열에 있는 문자는 순서대로 배열처럼 사용할 수 있다
a = "Life is too short, You need Python"
a[3]  # e
a[12] # s
a[-1] # n  
a[-5] # y  마이너스는 젤 뒤에서부터 1씩 카운트해주면 된다. 0과 -0은 똑같기 때문

#문자열 슬라이싱
#인덱싱처럼 한 문자만 뽑아내는 것이 아닌 단어를 뽑을 수도 있다
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b  #'life

a[0:4] # 'life'  더 간단한 방법으로 슬라이싱하기
a[5:7] # 'short' 꼭 0부터 시작을 안 해도 된다.
a[:] #이렇게 한다면 문자열 전체를 출력한다.
a[19:-7] # 'you need'  마이너스 기호를 사용할 수 있다 

#슬라이싱으로 문자영 나누기 
#요즘 많이 사용하고 있는 기법 중 하나이다
a = "20010331Rainy"
year = a[:4] #0~4
day = a[4:8] #5~8
weather = a[8:] #9~끝까지
year
#'2001'
day
#'0331'
weather
#'Rainy'

#Pithon"이라는 문자열을 "Python"으로 바꾸려면?
a = "Pithon"
a[1]
#'i'
a[1] = 'y'