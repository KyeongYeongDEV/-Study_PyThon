#문자열이란, 문자, 단어 등으로 구성된 집합
# ex) "Hello Wolrd", "1234", "a"
#공통점은 모두 큰따옴표 "" 안에 들어가있다
#문자열을 만드는 데 사용되는 방법은 총 4가지가 있다.

#문자열 안에 작은따옴표 ' 를 포함하고 싶다면
#문자열 전체를 큰따옴표로 묶고 그안에 작은 따옴표를 넣으면 들어가진다.
food = "python's favorite food is perl"

#문자열 안에 큰따옴표를 포함하고 싶다면 반대로 하면 된다.
say = '"pyton is very easy." he says'

#다른 방법으로는 백슬래쉬 \ 를 이용하면 된다.
food2 = 'python\'s favorite food is perl'
sat2 = "\"pyton is very easy.\" he says"

#줄 바꾸기 
#1번 \n 삽입
multiline =  "Life is too short\nYou need python"

#2번
#연속된 큰,작은 따옴표 사용하기 '''   """
multiline2 = '''
 Life is too short
 You need python
'''

multiline3 = """
 Life is too short
 You need python
"""
print(multiline)
print(multiline2) #프린트를 통해 비교해보자  똑같을 것이다.
