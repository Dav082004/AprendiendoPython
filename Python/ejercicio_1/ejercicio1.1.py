#promedio de cursos
otros_cursos_min= 2.5
otros_cursos_max= 7
otros_cursos_prom= 4
este_curso= 1.5

#diferencias entre cursos
diferencias_con_min = 100 - este_curso/otros_cursos_min * 100
diferencias_con_max = 100 - este_curso * 1000 // otros_cursos_max / 10
diferencias_con_prom = 100 - este_curso/otros_cursos_prom * 100

print(f'este curso dura un {diferencias_con_min}% menos que el más rapido')
print(f'este curso dura un {diferencias_con_max}% menos que el más lento')
print(f'este curso dura un {diferencias_con_prom}% menos que el promedio')