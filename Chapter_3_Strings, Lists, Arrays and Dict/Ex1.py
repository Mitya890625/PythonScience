#arange - 3 аргумент: задаваемый интервал, например arange(1,10,1) выдаст 10 чисел, а linspace(1,10,1) выдаст 1 число
#linspace - 3 аргумент: количество элементов в заданном интервале
#%precision - кол-во знаков после запятой
import numpy as np
b = np.linspace(0, 29, 9)
b **= 2
print(b) 
b = np.linspace(0, 29, 9)
b += b
print(b)
b = np.linspace(0, 29, 9)
b *= 2
print(b)