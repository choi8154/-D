from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass


class MargheritaPizza(Pizza):
    def prepare(self):
        return "토마토, 모짜렐라, 바질로 만든 마르게리따 피자"
    
class PepperoniPizza(Pizza):
    def prepare(self):
        return "페퍼로니 듬뿍 들어간 피자"
    
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type:str) -> Pizza:
        if pizza_type == "margherita":
            return MargheritaPizza