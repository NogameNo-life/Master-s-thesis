import numpy as np
import matplotlib.pyplot as plt

# Создаем данные для прямой линии
x = np.linspace(-0.5, 1.5, 400)
y = -x + 1  # Уравнение прямой через точки (0,1) и (1,0)

# Настраиваем график
plt.figure(figsize=(8, 6))

# Рисуем саму прямую
plt.plot(x, y, 'b-')

# Закрашиваем область под кривой только где y >= 0
plt.fill_between(x, y, where=((y >=0) & (x>=0)), color='blue', alpha=0.2)

# Настраиваем отображение
plt.axhline(0, color='black', linewidth=0.5)  # Ось X
plt.axvline(0, color='black', linewidth=0.5)  # Ось Y
#plt.grid(True, linestyle='--', alpha=0.7)
#plt.xlim(-0.5, 1.5)
#plt.ylim(-1, 1.5)
#plt.title('График прямой с закрашенной положительной областью')
plt.xlabel('x1', color='blue')
plt.ylabel('x2', color='blue')
#plt.legend()

chi_x, chi_y = 0.250, 0.200

plt.text(chi_x,   # X-координата текста
        chi_y+ 0.15,   # Y-координата текста 
        r'$ \chi $',               # Текст
        fontsize=12, 
        color='black',
        weight='bold')

# Показываем важные точки
plt.scatter([0, 1], [1, 0], color='red', zorder=5)
plt.annotate('(0,1)', (0, 1), textcoords="offset points", xytext=(5,-5))
plt.annotate('(1,0)', (1, 0), textcoords="offset points", xytext=(5,-5))

plt.show()