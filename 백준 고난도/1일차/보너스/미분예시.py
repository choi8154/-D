import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 원래 함수 f(x) = x^2
def f(x):
    return x**2

# 미분 근사 함수
def derivative(f, x, h=1e-5):
    return (f(x+h) - f(x)) / h

# x 값
x = np.linspace(-5, 5, 200)
y = f(x)

# 그래프 설정
fig, ax = plt.subplots()
line_func, = ax.plot(x, y, label="f(x)=x^2")
line_tangent, = ax.plot([], [], '--r', label="tangent")
point, = ax.plot([], [], 'ro')

ax.legend()
ax.grid(True)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 25)

# 애니메이션 초기화
def init():
    line_tangent.set_data([], [])
    point.set_data([], [])
    return line_tangent, point

# 프레임마다 업데이트
def update(frame):
    px = -4 + frame*0.1   # 접선 그릴 x 지점
    py = f(px)
    slope = derivative(f, px)
    tangent = slope*(x - px) + py

    line_tangent.set_data(x, tangent)
    point.set_data(px, py)
    return line_tangent, point

ani = FuncAnimation(fig, update, frames=100, init_func=init,
                    blit=True, interval=100, repeat=True)

plt.show()