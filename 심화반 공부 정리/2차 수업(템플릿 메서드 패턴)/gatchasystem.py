class CaffeineBeverage:
    def prepareRecipe(self):
        self.boilWater()
        self.I_wnat_decaffeine()
        self.brew()
        self.pourInCup()
        self.addCondiments()
        return "음료가 나왔습니다."

    def boilWater(self):
        print("물 끓이는 중")

    def brew(self):
        raise NotImplementedError

    def pourInCup(self):
        print("컵에 따르는 중")

    def addCondiments(self):
        raise NotImplementedError

    def I_wnat_decaffeine(self):
        pass

class coffee(CaffeineBeverage):
    def addCondiments(self):
        print("설탕과 우유를 넣는 중..")

    def brew(self):
        print("커피를 내리는 중")

    def I_wnat_decaffeine(self):
        print("카페인을 제거한 원두를 사용한다.")

decaffein_coffee = coffee()
print(decaffein_coffee.prepareRecipe())