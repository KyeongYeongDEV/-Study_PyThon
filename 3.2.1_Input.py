#사용자 입력
#input 사용
a = input()
#Life is too short, you need python 이렇게 입력을 하면
a
'Life is too short, you need python'

#프롬프트르르 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요: ")
"""숫자를 입력하세요:"""

#큰 따옴표로 둘어싸인 문자열은 +연산과 동일하다
print("life" "is" "too short") # ①
'''lifeistoo short'''
print("life"+"is"+"too short") # ②
'''lifeistoo short'''

#띄워쓰기는 콤마로 한다.
print("life", "is", "too short")
'''life is too short'''

#한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')

'''0 1 2 3 4 5 6 7 8 9'''
