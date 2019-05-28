import sys

m = 0
grades = []
lines = []

try:
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    file.close()
except IndexError:
    print('[Error] Porfavor especifique un archivo con datos.')
    exit(1)
except IOError:
    print('[Error] No se ha posido leer el archivo especificado.')
    exit(2)

if len(lines) < 1:
    print('[Error] El archivo no contiene datos.')
    exit(3)

n = len(lines)

for line in lines:
    grade = sum([int(cell) for cell in line.strip().split()])
    m += grade
    grades.append(grade)

m /= 2

density = 2 * m / (n * (n - 1))

print('n: ' + str(n))
print('m: ' + str(m))
print('Density: ' + str(density))

for i in range(len(grades)):
    centralidad = grades[i] / (n - 1)
    print('Grado v' + str(i) + ': ' + str(grades[i]) + '. Centralidad: ' + str(centralidad))
