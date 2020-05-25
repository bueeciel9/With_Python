# 클래스(Class) : 반복되는 불필요한 소스코드를 최소화 하면서
#                현실 세계의 사물을 컴퓨터 프로그래밍 상에서
#                 쉽게 표현할 수 있도록 해주는 프로그래밍 기술

# 인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수 : 클래스 내부에 포함되는 함수, 메소드라고 부른다.

# Setter 메소드
# 클래스 생성자, 소멸자! 소멸자까지 신경쓰기~ 이거

# 클래스의 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부모와 자식 관계가 존재한다.
# 자식 클래스 : 부모 클래스를 상속 받은 클래스

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attach(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력: ", self.power, "]")


unit = Unit("홍길동", 376)
unit.attach()


class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type


monster = Monster("슬라임", 10, "초급")
monster.attach()


class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name  # 클래스의 멤버
        self.color = color  # 클래스의 멤버

    # 클래스의 메소드

    def show_info(self):
        print("이름 : ", self.name, "/색상 : ", self.color)


car1 = Car("소나타", "빨간색")
car1.show_info()

car2 = Car("아반떼", "검은색")
car2.show_info()
print(car1.name, "을(를) 구매했습니다!")
