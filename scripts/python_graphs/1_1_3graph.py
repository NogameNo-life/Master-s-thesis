import numpy as np
import matplotlib.pyplot as plt

# Создаем данные для графика y = x
x = np.linspace(0, 5, 400)
y = x

# Настройка графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue')

# Добавляем вертикальную линию x=1
plt.axvline(x=1, color='black', linestyle='-')

# Выделяем точку пересечения
plt.scatter(1, 1, color='green', zorder=5)
plt.annotate('(1,1)', (1, 1), xytext=(10, -10),
             textcoords='offset points',
             color='green',
             fontsize=10)

# Настройка отображения
#plt.axhline(0, color='black', linewidth=0.5)  # Ось X
#plt.axvline(0, color='black', linewidth=0.5)  # Ось Y
#plt.grid(True, linestyle='--', alpha=0.7)
#plt.xlim(-2, 3)
#plt.ylim(-2, 3)
#plt.title('График y = x с вертикальной линией x=1')
plt.xlabel('x', color='blue')
plt.ylabel('f(x)', color='blue')
plt.legend()

plt.show()