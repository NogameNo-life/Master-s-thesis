import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline  # Для интерполяции

x = [0, 0.987, 3, 4, 6]
y = [5, 3.251, 4, 2, 6]

# Создаем гладкую интерполяцию
x_new = np.linspace(min(x), max(x), 300)  # 300 точек для плавности
cs = CubicSpline(x, y)  # Кубический сплайн
y_smooth = cs(x_new)

# Рисуем график
plt.plot(x_new, y_smooth, 
         linestyle='-', 
         color='blue', 
         linewidth=2)

# Оставляем оригинальные точки с маркерами
#plt.plot(x, y, 'ro', markersize=8, markerfacecolor='red')
plt.plot(0.987, 3.251, 'ro', markersize=8, markerfacecolor='red')

plt.text(0.987,   # X-координата текста
        3.251 + 0.15,   # Y-координата текста 
        'x',               # Текст
        fontsize=12, 
        color='black',
        weight='bold')

y_horizontal = 2  # Высота горизонтального отрезка
y_vertical_bottom, y_vertical_top = 1.7, 2.3  # Границы вертикалей
x_horizontal_start, x_horizontal_end = 0.5, 2.0  # Границы горизонтали

# Горизонтальный отрезок (фиолетовый пунктир)
plt.hlines(y=y_horizontal, 
          xmin=x_horizontal_start, 
          xmax=x_horizontal_end,
          colors='purple', 
          linestyles='-', 
          linewidth=2,
          alpha=0.7,
          label='Горизонтальный отрезок')

# Вертикальные отрезки по бокам (синие сплошные)
plt.vlines(x=[x_horizontal_start, x_horizontal_end], 
          ymin=y_vertical_bottom, 
          ymax=y_vertical_top,
          colors='purple',
          linestyles='-', 
          linewidth=1.5,
          alpha=0.7,
          label='Вертикальные ограничители')


chi_x, chi_y = 1.197, 2.215

plt.text(chi_x,   # X-координата текста
        chi_y+ 0.15,   # Y-координата текста 
        r'$ \chi $',               # Текст
        fontsize=12, 
        color='black',
        weight='bold')

plt.title("Задача одномерной оптимизации")
plt.grid(True)
plt.show()