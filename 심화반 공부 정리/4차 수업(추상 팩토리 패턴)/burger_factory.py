# 피자 만들기 프로젝트
from abc import ABC, abstractmethod

# 추상 product
class Bread(ABC):
    @abstractmethod
    def bread_type(self):
        pass

class Patty(ABC):
    @abstractmethod
    def patty_type(self):
        pass

class Source(ABC):
    @abstractmethod
    def source_type(slef):
        pass

# 구체 product
class CornBread(Bread):
    def bread_type(self):
        return "옥수수빵"

class SesameBread(Bread):
    def bread_type(self):
        return "참깨빵"
    
class WheatBread(Bread):
    def bread_type(self):
        return "밀빵"
    

class PorkPatty(Patty):
    def patty_type(self):
        return "돼지고기패티"
    
class BeefPatty(Patty):
    def patty_type(self):
        return "소고기패티"
    
class ShrimpPatty(Patty):
    def patty_type(self):
        return "새우패티"


class HotSource(Source):
    def source_type(slef):
        return "매운 소스"

class SweetSource(Source):
    def source_type(self):
        return "달콤한 소스"
    

# 추상 Factory
class BurgerFactory(ABC):
    @abstractmethod
    def bread(self)->Bread:
        pass

    @abstractmethod
    def patty(self)->Patty:
        pass

    @abstractmethod
    def source(self)->Source:
        pass

# 구체 Factory
class HotBeefCornBurger(BurgerFactory):
    def bread(self)->Bread:
        return CornBread()
    
    def patty(self)->Patty:
        return BeefPatty()
    
    def source(self)->Source:
        return HotSource()

class SweetPorkSesameBurger(BurgerFactory):
    def bread(self)->Bread:
        return SesameBread()
    
    def patty(self)->Patty:
        return PorkPatty()
    
    def source(self)->Source:
        return SweetSource()
    

# 클라이언트
def burger_maker(burger:BurgerFactory):
    bread = burger.bread()
    beef = burger.patty()
    source = burger.source()

    print(f"빵 : {bread.bread_type()}\n페티 : {beef.patty_type()}\n소스 : {source.source_type()}")
    print("주문 접수 완료!")

user_choice = input("어떤 햄버거를 주문하시겠습니까? : ")
if user_choice == "핫비프버거":
    burger_maker(HotBeefCornBurger())
elif user_choice == "스윗포크버거":
    burger_maker(SweetPorkSesameBurger())