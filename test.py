class JSS:
    def __init__(self):
        self.name = input("이름: ")
        self.age = input("나이: ")
    
    def show(self):
        print("나의 이름은 {}. 나이는 {}세 입니다.".format(self.name, self.age))

a = JSS()
a.name
a.age
a.show()

b = JSS()
b.name
b.age
b.show()

print(b.age)