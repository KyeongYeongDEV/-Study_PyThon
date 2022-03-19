#메서드 오버라이딩 (Overriding 덮어쓰다)

class fourcal:
    def __init__(self,first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

# a = fourcal(4,0)
# a.div()
#위의 것을 실행시키면 값을 0으로 나누려 했기 때문에 오류가 발생한다.


class SafeFourCal(fourcal):
    def div(self):
        if(self.second == 0):
            return 0
        else:
            return self.first / self.second
# SafefourCal에서는 fourcal에 있는 div 메서드를 동일한 이름으로 다시 작성했다
# 이런 부모클래스의 메서드를 동일한 이름으로 다시 만드는 것을 
#메서드 오버라이딩(덮어쓰다)라고 한다.
#이렇게 하면 부모메서드를 호출하는 것이 아닌 오버라이딩한 메서드를 가져온다.
a = fourcal(4,0)
print(a.div()) 
