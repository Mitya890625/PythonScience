import numpy as np
import pandas as pd

planets = pd.read_table('Planet.txt', sep='\s+', index_col='planet') # чтение из текстового файла
density = []
earth_mass = 5.97*(10**24)
earth_diameter = 12742000
earth_density = 5511.4123692861485
#
for i in range(9):
    temp = (planets['mass'][i]*earth_mass)/((1/6) * np.pi* ((planets['diameter'][i]*earth_diameter)**3))
    relative_density = temp/earth_density
    relative_density = float('{:.2f}'.format(relative_density)) # уменьшение чисел после запятой
    density.append(relative_density)
planets['density'] = density # добавление в датафрейм нового столбца
print(planets)
sorted_planets = planets.sort_values(by=['diameter'], ascending=False)
print(sorted_planets)
print(planets[planets['mass']> 1].sort_values(by=['mass']))
