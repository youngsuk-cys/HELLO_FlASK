
class Calculator:

    def __init__(self):
        print('self')
        print(self)
        self.result = 0

    def add(self , num):
        self.result += num
        return self.result


cal1 = Calculator()
print( type(cal1) )

print ( cal1.add(4))
print ( cal1.add(55))


class FourCal:
    # 초기화(initialize) 메서드
    def __init__(self , f , s):
        self.first = f
        self.second = s

    def setdata(self, first, second):
        self.first = first
        self.second = second


fourCal1 = FourCal('Chae' , 'yougsuk')
print( fourCal1.first )