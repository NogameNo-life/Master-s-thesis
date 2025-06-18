import numpy as np
import matplotlib.pyplot as plt

# Создаем данные для прямой линии
x = np.linspace(-0.5, 1.5, 400)
y = -x + 1  # Уравнение прямой через точки (0,1) и (1,0)

# Настраиваем график
plt.figure(figsize=(8, 6))

# Рисуем саму прямую
plt.plot(x, y, color='#7f1ba6bf', linestyle='-')

# Закрашиваем область под кривой только где y >= 0
plt.fill_between(x, y, where=((y >=0) & (x>=0)), color='#7f1ba6bf', alpha=0.2)

# Настраиваем отображение
plt.axhline(0, color='black', linewidth=0.5)  # Ось X
plt.axvline(0, color='black', linewidth=0.5)  # Ось Y

plt.xlabel(r'$\mathbf{x1}$', color='black')
plt.ylabel(r'$\mathbf{x2}$', color='black')

chi_x, chi_y = 0.250, 0.200

plt.text(chi_x,   # X-координата текста
        chi_y+ 0.15,   # Y-координата текста 
        r'$ \chi $',               # Текст
        fontsize=12, 
        color='black',
        weight='bold')

# Показываем важные точки
plt.scatter([0, 1], [1, 0], color='#dc143c', zorder=5)
plt.annotate('(0,1)', (0, 1), textcoords="offset points", xytext=(7,-2))
plt.annotate('(1,0)', (1, 0), textcoords="offset points", xytext=(6,3))

plt.show()