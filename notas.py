materias_y_notas = [
    ["DEFENSA INTEGRAL DE LA NACIÓN I", 17], 
    ["DIBUJO", 17], 
    ["EDUCACIÓN AMBIENTAL", 20], 
    ["GEOMETRÍA ANALÍTICA", 16],
    ["HOMBRE, SOCIEDAD, CIENCIA, Y TECNOLOGIA", 19], 
    ["INGLÉS I", 17], 
    ["MATEMÁTICA I", 20], 
    ["SEMINARIO I", 18], 
    ["FISICA I", 14], 
    ["QUÍMICA GENERAL", 14], 
    ["PROBABILIDADES Y ESTADÍSTICAS", 11], 
    ["ALGEBRA LINEAL", 13], 
    ["DEFENSA INTEGRAL DE LA NACIÓN II", 16], 
    ["INGLES II",15], 
    ["MATEMÁTICA II", 16], 
    ["SEMINARIO II", 14], 
    ["EDUCACIÓN FÍSICA Y DEPORTE", 18], 
    ["FISICA II",10], 
    ["MATEMATICA III", 16], 
]
    
print("--- Tus Materias y Notas ---")
for materia, nota in materias_y_notas:
    print(f"Materia: {materia}, Nota: {nota}")

if materias_y_notas:
    total_notas = sum(item[1] for item in materias_y_notas)
    cantidad_materias = len(materias_y_notas)
    promedio = total_notas / cantidad_materias
    print(f"\nTu promedio general es: {promedio:.2f}")
else:
    print("\nNo hay materias registradas.")





