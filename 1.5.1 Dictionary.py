#딕셔너리(Dictionary)
#단어 그대로 사전 느낌이다
# "이름"(key) = "홍길동"(value)  "생일" = "몇월며칠"
#key를 통해서 value를 얻는다


#딕셔너리 생성
from re import A


dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

a = {1: 'hi'} #key로 정수 값 1, value로 문자열 'hi'를 사용
a = { 'a': [1,2,3]} #value에 리스트도 넣을 수 있다


#딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b' #이렇게 입력을 하면 key =2, value = 'b'인 딕셔너리 쌍이 추가된다.
a
{1: 'a', 2: 'b'}

a['name'] = 'pey'
a
{1: 'a', 2: 'b', 'name': 'pey'} #key = 'name' , value = 'pey'가 추가가 됐다

a[3] = [1,2,3]
a
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]} #key = 3, value = [1,2,3]인 딕셔너리가 추가됐다


#딕셔너리 요소 삭제
del a[1]
a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]} #key = 1, value = 'a'가 삭제가 됐다


#딕셔너리에 key 사용해 value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']
10
grade['julliet']
99
#key와 value를 얻기 위해서는
#딕셔너리변수이름[key]를 사용한다

#딕셔너리의 a[1]과 튜플,리스트에서 사용되느 a[1]은 전혀 다르다
#딕셔너리의 1은 두번째 요소를 뜻하는 것이 아닌 ㅏ됴에 해당하는 1을 나타낸다


#딕셔너리를 만들 떄 주의할 점
a = {1:'a', 1:'b'}
a
{1: 'b'}  #key를 중복되게 설정하면 하나를 제외한 나머지는 모두 무시된다.

a = {[1,2] : 'hi'} #이런 경우도 두 개의 key에 하나의 값을 넣었기 때문에 오류가 발생한다.


#key 리스트 만들기 (keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
dict_values(['name', 'phone', 'birth'])
list(a.keys()) #위의 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
['name', 'phone', 'birth']

for k in a.keys():  #이렇게도 사용가능
    print(k)
#리스트를 사용하는 것과 차이가 없지만,
#리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.


#value 리스트 만들기(values)
a.values()
dict_values(['pey', '0119993323', '1118'])
#key를 얻는 것과 마찬가지 방법으로 value만 얻고 싶다면 
#value함수를 사용하면 된다.


#key, value 쌍 얻기(items)
a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
#items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

#Key: Value 쌍 모두 지우기(clear)
a.clear()
{}  #딕셔너리의 모든 요소를 삭제한다.

#Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')
'pey'
a.get('phone')
'0119993323'
#결과는 똑같지만 
#오류 발생시 a[]는 오류를 발생하지만
#a.get()은 None을 반환한다.

a.get('foo', 'bar')
'bar'  #딕셔너리 안에 찾으려는 Key 값이 없을 경우
#미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는
# get(x, '디폴트 값')을 사용하면 편리하다.


#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
'name' in a
True
'email' in a
False
#참반으로 츨려된다.