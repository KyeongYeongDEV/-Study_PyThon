#문자열 포매팅

#1. 숫자 바로 대입
"I eat %d apples." % 3
#'I eat 3 apples.'

#2. 문자열 바로 대입
"I eat %s apples." % "five"
#'I eat five apples.'

#숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number
#'I eat 3 apples.'

#2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
#'I ate 10 apples. so I was sick for three days.'


# %s	문자열(String)  보통 이걸 많이 쓴다
#  문자열에서는 정수형이든 실수형이든 알아서 변환해 대입하기 때문

# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수

#정렬과 공백
"%10s" % "hi"
#'        hi'
# 10s는 10칸의 공백을 주어라라는 의미이다.

#반대쪽은 -10s
"%-10sjane." % 'hi'
#'hi        jane.'

#소수점 표현
"%0.4f" % 3.42134234
'3.4213'
#%0.x   x의 수만큼의 소수점을 표현해라
