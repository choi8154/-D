from abc import ABC, abstractmethod

# 기본 카드 구조 (Product 계층)
class Minion(ABC):
    def __init__(self, name, attack, tribe):
        self.name = name
        self.attack = attack
        self.tribe = tribe

    def __str__(self):
        return f"{self.tribe} {self.name} (공격력 {self.attack})"

# 구체 하수인
class DemonMinion(Minion):
    def __init__(self, name="악마병사"):
        super().__init__(name, 5, "악마")

class BeastMinion(Minion):
    def __init__(self, name="야생늑대"):
        super().__init__(name, 3, "야생")

# 추상 Buff Factory
class BuffFactory(ABC):
    @abstractmethod
    def apply_buff(self, minion: Minion):
        pass

# 구체 BuffFactory
class DemonBuffFactory(BuffFactory):
    def apply_buff(self, minion: Minion):
        if minion.tribe == "악마":
            minion.attack += 10
            print(f"{minion.name}의 공격력이 10 증가.")
        else:
            print(f"{minion.name}은 악마가 아니라 버프 적용 안 됨.")

class BeastBuffFactory(BuffFactory):
    def apply_buff(self, minion: Minion):
        if minion.tribe == "야생":
            print(f"{minion.name}에게 돌진을 부여.")
        else:
            print(f"{minion.name}은 야생이 아니라 돌진 불가.")


def apply_tribe_effect(factory: BuffFactory, minions: list[Minion]):
    for m in minions:
        factory.apply_buff(m)
        print(m)


# 테스트
minions = [DemonMinion(), BeastMinion()]

print("=== 악마 버프 적용 ===")
apply_tribe_effect(DemonBuffFactory(), minions)

print("\n=== 야생 버프 적용 ===")
apply_tribe_effect(BeastBuffFactory(), minions)