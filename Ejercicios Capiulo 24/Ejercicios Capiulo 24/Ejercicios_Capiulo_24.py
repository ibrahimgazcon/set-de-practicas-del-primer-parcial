#41
colores = input('Introduce tu color favorito:\n')
tupla_colores = ('naranja', 'azul', 'blanco', 'amarillo')

if colores in tupla_colores[0]:
	print('El color naranja está admitido')
elif colores in tupla_colores[1]:
	print('El color azul está admitido')
elif colores in tupla_colores[2]:
	print('El color blanco está admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo está admitido')
else:
	print('Color no admitido')
