# Задача "Вычисление площади круга"
# Используйте модуль math для получения значения числа π.
# Сгенерируйте случайный радиус круга с помощью модуля random.
# Вычислите площадь круга по формуле πr².

import math
from random import randint

r = randint(1, 20)
area = math.pi * r * r
print(area)
