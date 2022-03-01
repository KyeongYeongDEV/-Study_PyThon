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

#왼쪽 정렬
"{0:<10}".format("hi")
#'hi        '