#함수란?
# f(x)= 2^2 : 이건 함수식이다 이를 파이썬으로 표현하면
def func(x):
    return 2**2
# 가 된다.

#미분이란? 지금 이 순간 얼마나 빨라지는지(순간 기울기, 변화율).
# f'(x)f≈(x+h)-f(x)/h : 미분식으로 순간 속도를 근사값으로 구하는 값이다.
def derivative(f, x, h=1e-5): #h=1e-5는 지수 표현으로 1 * 10^-5 = 0.00001
    return (f(x + h) - f(x)) / h

def f(x):
    return x**2

# x=3에서의 기울기 (즉 f'(3))
print(derivative(f, 3))

#적분이란? 쌓이고 쌓인 전체 양(넓이, 총합).
# ∫
def f(x):
    return x**2   # 함수 정의 (y = x^2)

# 적분 구하기
a, b = 0, 1       # 구간 [0,1]
n = 1000          # 네모를 몇 개로 쪼갤지 (많을수록 정확)
width = (b - a) / n  # 네모 하나의 가로 길이

area = 0
for i in range(n):
    x = a + i * width     # 네모의 왼쪽
    area += f(x) * width  # 세로 * 가로 = 네모 넓이

print("넓이 =", area)