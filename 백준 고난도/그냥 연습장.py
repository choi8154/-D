import matplotlib.pyplot as plt
import numpy as np

# 함수 정의
def f1(x):
    return x

def f2(x):
    return x**2

def f3(x):
    return 2*x + 3

# x 값 준비 (-10 ~ 10 범위에서 200개)
x = np.linspace(-10, 10, 200)

# 각 함수 값 계산
y1 = [f1(val) for val in x]
y2 = [f2(val) for val in x]
y3 = [f3(val) for val in x]

# 그래프 그리기
plt.plot(x, y1, label="f(x) = x")
plt.plot(x, y2, label="f(x) = x^2")
plt.plot(x, y3, label="f(x) = 2x + 3")

plt.axhline(0, color='black', linewidth=0.5)  # x축
plt.axvline(0, color='black', linewidth=0.5)  # y축
plt.legend()
plt.grid(True)
plt.show()