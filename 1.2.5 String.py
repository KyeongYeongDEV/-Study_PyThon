#format 함수를 사용한 포매팅

#숫자 바로 대입하기
"I eat {0} apple".format(3)
#'I eat 3 apples'   문자열 증 {0}부븐이 3으로 바뀌었다

#문자열 바로 대입하기
"I eat {0} apples".format("five")
#'I eat five apples'  문자열 {0}항목이 five로 바뀌었다.

#숫자값을 가진 변수로 대입하기
number =3
"I eat {0} apples".format(number)
#'I eat 3 apples'

#2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
#'I ate 10 apples. so I was sick for three days.'

#이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
#'I ate 10 apples. so I was sick for 3 days.'

#인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
#'I ate 10 apples. so I was sick for 3 days.'
#위와 같이 인덱스 항목과 name = value 형태를 혼용하는 것도 가능하다.

#왼쪽 정렬
"{0:<10}".format("hi")
#'hi        '
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고
# 문자열의 총 자릿수를 10으로 맞출 수 있다.

#오른쪽 정렬
"{0:>10}".format("hi")
#'        hi'
#오른쪽 정렬은 :< 대신 :>를 사용하면 된다.
#화살표 방향을 생각하면 어느 쪽으로 정렬되는지 바로 알 수 있을 것이다.

#가운데 정렬
"{0:^10}".format("hi")
#'    hi    '
# :^ 기호를 사용하면 가운데 정렬도 가능하다.

#공백 채우기
"{0:=^10}".format("hi")
'====hi===='
"{0:!<10}".format("hi")
'hi!!!!!!!!'
#정렬할 때 공백 문자 대신에 지정한 문자 값으로 채워 넣는 것도 가능하다.

#소수점 표현하기
y=3.42134234
"0:0.4f".format(y)
'    3.4213'
#앞에서 살펴보았던 표현식 0.4f를 그대로 사영한 것을 알 수 있다.

# { 또는 } 문자 표현하기
"{{ and }}".format()
'{ and }'
#format 함수를 이용해 중광호 문자를 그대로 사용하고 싶으면
#{{}} 처럼 2개를 연속해서 사용하면 된다.




