import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline  # Для интерполяции

x = [0,   0.7,  2,  3.5, 4.5, 5.481, 7.5, 8, 8.5]
y = [4.5, 2.5, 4.5, 3.5, 4.2,  3.638, 4,  4, 5]

# Создаем гладкую интерполяцию
x_new = np.linspace(min(x), max(x), 300)  # 300 точек для плавности
cs = CubicSpline(x, y)  # Кубический сплайн
y_smooth = cs(x_new)

plt.rcParams.update({
    'mathtext.default': 'regular'  # Используем встроенный рендеринг MathText
})
# Рисуем график
plt.plot(x_new, y_smooth, 
         linestyle='-', 
         color='#00ffff', 
         linewidth=2)

#plt.plot(x, y, 'ro', markersize=8)
plt.plot(0.709, 2.5, 'ro', markersize=8, markerfacecolor='#dc143c')
plt.plot(3.5, 3.5, 'ro', markersize=8, markerfacecolor='#dc143c')
plt.plot(6, 3.548, 'ro', markersize=8, markerfacecolor='#dc143c')
plt.plot(8, 4, 'ro', markersize=8, markerfacecolor='#dc143c')

plt.text(1,   # X-координата текста
        2.5,   # Y-координата текста 
        'Глобальный минимум', 
        fontsize=12, 
        color='black')

plt.text(2.2,   # X-координата текста
        3.3,   # Y-координата текста 
        'Слабый локальный минимум',
        fontsize=12, 
        color='black')

plt.text(5,   # X-координата текста
        3.2,   # Y-координата текста 
        'Сильный локальный минимум', # Текст
        fontsize=12, 
        color='black')

plt.text(7.018,   # X-координата текста
        4.084,   # Y-координата текста 
        'Перегиб', # Текст
        fontsize=12, 
        color='black')


chi_x, chi_y = 1.197, 2.215

plt.xlabel(r'$\mathbf{x}$', color='black')
plt.ylabel(r'$\mathbf{f(x)}$', color='black')

plt.show()