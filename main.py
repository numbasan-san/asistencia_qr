
import qrcode
import pandas as pd
import numpy as np

'''
class Alumno:

	def __init__(self, nombre, matricula):
		self.nombre = nombre
		self.matricula = matricula
'''

excel = pd.read_excel('listado.xlsx')
nombres = excel['nombre']
matriculas = excel['matricula']

'''
nombres = ['JOSE', 'ANTONIO', 'JUAN', 'MANUEL', 'FRANCISCO', 'LUIS', 'JAVIER', 'MIGUEL', 'CARLOS', 'ANGEL', 'JESUS', 'DAVID', 'DANIEL', 'PEDRO', 'ALEJANDRO', 'MARIA', 'CARMEN', 'ANA', 'ISABEL', 'DOLORES', 'PILAR', 'TERESA', 'ROSA', 'JOSEFA', 'CRISTINA', 'ANGELES', 'LAURA', 'ANTONIA', 'ELENA', 'MARTA']
matriculas = ['23-0001', '23-0002', '23-0003', '23-0004', '23-0005', '23-0006', '23-0007', '23-0008', '23-0009', '23-0010', '23-0011', '23-0012', '23-0013', '23-0014', '23-0015', '23-0016', '23-0017', '23-0018', '23-0019', '23-0020', '23-0021', '23-0022', '23-0023', '23-0024', '23-0025', '23-0026', '23-0027', '23-0028', '23-0029', '23-0030']
'''
'''

"""

"""

data = {
	'nombre': nombres,
	'matricula': matriculas
}
df = pd.DataFrame(data)

df.to_excel('asistencia.xlsx')
# input('¿Funcionó? ')
'''


# print(nombres)
# print(matriculas)
# display(df)

'''
for i in range(len(alumnos)):
	sim = '0' if i < 9 else ''
	print(f'{sim}{i + 1}. Nombre: {alumnos[i].nombre}. Matrícula: {alumnos[i].matricula}.')
'''

# print(len(excel))


for i in range(len(excel)):
	obj = qrcode.make(f'{nombres[i], matriculas[i]}')
	img_qr = open(f'{nombres[i]} - {matriculas[i]}.png', 'wb')
	obj.save(img_qr)
	img_qr.close()

