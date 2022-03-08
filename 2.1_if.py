#조건문(if)

money = True
if money:
     print("택시를 타고 가라")
else:
     print("걸어 가라")
#택시를 타고 가라
#money가 '참'이므로 if문이 실행되어 위에 것이 출력되었다

#들여쓰기
"""
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
"""
#들여쓰기를 다음과 같이 제대로 하지않으면 오류가 발생한다.
"""
money = True
if money:
    print("택시를")
    print("타고")
        print("가라")
"""
#비교 연산자 == != < > <= >= 

#and, or, not


#
"""
in	        not in
x in 리스트	x not in 리스트
x in 튜플	x not in 튜플
x in 문자열	x not in 문자열
"""
#in ~안에
1 in [1, 2, 3]
True
1 not in [1, 2, 3]
False

'a' in ('a', 'b', 'c')
True
'j' not in 'python'
True
#응용
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
   print("걸어가라")
#택시를 타고 가라

# continue == pass
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")

#다양한 조건을 나타내는 elif  == else if
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")
#택시를 타고가라
