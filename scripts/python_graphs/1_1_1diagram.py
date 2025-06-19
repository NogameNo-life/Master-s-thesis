from graphviz import Digraph

dot = Digraph(comment='Блок-схема проекта', graph_attr={'rankdir': 'LR'})

# Добавим блоки
dot.node('A', 'начало', shape='oval')
dot.node('B', 'Техническое\nзадание', shape='note')
dot.node('C', 'Начальный\nпроект', shape='oval')
dot.node('D', 'Оценка\nэффективности', shape='oval')
dot.node('E', 'Хорошо?', shape='diamond')
dot.node('F', 'Окончательный\nпроект', shape='note')
dot.node('G', 'Изменение\nпроекта', shape='oval')

# Добавим стрелки
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F', label='да')
dot.edge('E', 'G', label='нет')
dot.edge('G', 'D')

# Сохраняем
dot.render('diagram', format='pdf')  # можно также 'png', 'svg'
