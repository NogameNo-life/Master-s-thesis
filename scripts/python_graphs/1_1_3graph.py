import numpy as np
import matplotlib.pyplot as plt

# Создаем данные для графика y = x
x = np.linspace(0, 5, 400)
y = x

# Настройка графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='#00ffff')

# Добавляем вертикальную линию x=1
plt.axvline(x=1, color='black', linestyle='-')

# Выделяем точку пересечения
plt.scatter(1, 1, color='#dc143c', zorder=5)
plt.annotate('(1,1)', (1, 1), xytext=(10, -10),
             textcoords='offset points',
             color='black',
             fontsize=10)

plt.xlabel(r'$\mathbf{x}$', color='black')
plt.ylabel(r'$\mathbf{f(x)}$', color='black')

plt.show()