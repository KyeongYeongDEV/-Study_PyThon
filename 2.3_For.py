#반복문 for

#전형적인 for문
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

#다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
# a 리스트의 요솟값이 튜플이기 때문에
#  각각의 요소가 자동으로 (first, last) 변수에 대입된다.

#다양한 응용
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

#for문과 continue
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)


#range함수
a = range(1, 11) #1~10  #range함수를 통해 범위를 미리 지정을 해준다음
add = 0 
for i in a:   #굳이 변수를 안 만들고 바로 range(1,11)을 넣어도 상관없다
    add = add + i 
print(add)
55
#다른 예
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

#리스트 내포 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
[3, 6, 9, 12]

#위의 문장을 내포를 사용하면
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
[3, 6, 9, 12] 
#더 간단하게 표현이 가능하다

#민약 짝수만 3을곱하여 담고 싶으면 #[표현식 for 항목 in 반복가능객체 if 조건문]
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
[6, 12]

#이중 for문도 가능하다
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
