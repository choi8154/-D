from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    # 템플릿 메서드 알고리즘 뼈대 고정
    def perpare_recipe(self): 
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
        if self.customer_wants_ice(): #후크 사용
            self.add_ice()

    def boil_water(self): #중복되는 메서드를 상위 클래스에 캡슐화
        print("물을 끓인다.")

    #후크 메서드
    def customer_wants_ice(self):
        return True # pass를 하지 않고 디폴트 구현이 True라 굳이 재정의 하지 않아도 됨.

    def pour_in_cup(self): #중복되는 메서드를 상위 클래스에 캡슐화
        print("컵에 따른다")

    @abstractmethod #행위의 중복은 있지만 방식이 다를때 추상메서드로 두고 상속 할 때 오버라이딩함.
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self): #행위의 중복은 있지만 방식이 다를때 추상메서드로 두고 상속 할 때 오버라이딩함.
        pass
    
    @abstractmethod
    def add_ice(self):
        pass
