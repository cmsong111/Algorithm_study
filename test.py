class JSS:
    def __init__(self):
        self.name = input("이름: ")
        self.age = input("나이: ")

class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.sex = input("성별: ")

    def show(self):
        print("나의 이름은 {}. 나이는 {}세 입니다.".format(self.name, self.age))
        print("성별은 {} 입니다.".format(self.sex))



a = JSS2()

print(a.sex)
print(a.age)