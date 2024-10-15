import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from radon.complexity import cc_visit

# Función para contar líneas de código (LOC)
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    loc = len([line for line in lines if line.strip()])  # Contar solo líneas no vacías
    return loc

# Función para contar comentarios
def count_comments(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    comments = len([line for line in lines if line.strip().startswith('#')])  # Contar líneas que son comentarios
    return comments

# Función para analizar la complejidad ciclomática
def analyze_code_complexity(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    complexity = cc_visit(code)
    return complexity

# Función para analizar un directorio de código
def analyze_directory(directory_path):
    metrics = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                loc = count_lines(file_path)
                comments = count_comments(file_path)
                complexity = analyze_code_complexity(file_path)
                for c in complexity:
                    metrics.append({
                        'file': file,
                        'complexity': c.complexity,
                        'loc': loc,
                        'comments': comments,
                        'functions': len(complexity)
                    })

    return pd.DataFrame(metrics)

# Función para visualizar las métricas
def visualize_metrics(metrics_df):
    # Visualización de complejidad ciclomática
    plt.figure(figsize=(12, 6))
    sns.histplot(metrics_df['complexity'], bins=20, kde=True)
    plt.title('Distribución de Complejidad Ciclomática')
    plt.xlabel('Complejidad Ciclomática')
    plt.ylabel('Frecuencia')
    plt.axvline(metrics_df['complexity'].mean(), color='r', linestyle='dashed', linewidth=1)
    plt.show()

    # Visualización de líneas de código (LOC)
    plt.figure(figsize=(12, 6))
    sns.histplot(metrics_df['loc'], bins=20, kde=True)
    plt.title('Distribución de Líneas de Código (LOC)')
    plt.xlabel('Líneas de Código (LOC)')
    plt.ylabel('Frecuencia')
    plt.axvline(metrics_df['loc'].mean(), color='r', linestyle='dashed', linewidth=1)
    plt.show()

    # Visualización de comentarios
    plt.figure(figsize=(12, 6))
    sns.histplot(metrics_df['comments'], bins=20, kde=True)
    plt.title('Distribución de Comentarios')
    plt.xlabel('Número de Comentarios')
    plt.ylabel('Frecuencia')
    plt.axvline(metrics_df['comments'].mean(), color='r', linestyle='dashed', linewidth=1)
    plt.show()

# Análisis del proyecto
project_path = 'C:/Users/afbm2/Downloads/Estadistica'  # Cambia esta ruta según tu directorio
project_metrics = analyze_directory(project_path)

# Comprobar si hay métricas válidas
if not project_metrics.empty:
    # Calcular estadísticas
    mean_complexity = project_metrics['complexity'].mean()
    mean_loc = project_metrics['loc'].mean()
    mean_comments = project_metrics['comments'].mean()
    
    print(f"Complejidad Ciclomática Promedio: {mean_complexity:.2f}")
    print(f"Líneas de Código Promedio: {mean_loc:.2f}")
    print(f"Número Promedio de Comentarios: {mean_comments:.2f}")

    # Visualización de métricas
    visualize_metrics(project_metrics)
else:
    print("No se encontraron métricas válidas en el directorio.")





Estadísticas que se Obtienen del Análisis de Código
Complejidad Ciclomática:

¿Qué es?: Es una medida que cuantifica la complejidad de un programa. Se basa en el número de caminos lógicos que se pueden seguir en el código.
¿Qué indica?: Una complejidad más alta puede sugerir que un fragmento de código es más difícil de entender, mantener y probar. En general, se busca que la complejidad sea baja, lo que indica que el código es más sencillo y predecible.
Líneas de Código (LOC):

¿Qué es?: Es simplemente la cantidad de líneas de código que componen un archivo o un proyecto.
¿Qué indica?: Un mayor número de líneas de código no siempre es mejor. Aunque puede sugerir que hay más funcionalidad, también puede indicar que el código es más complicado y difícil de manejar. Es útil tener un equilibrio, donde haya suficientes líneas para hacer el trabajo sin que el código se vuelva innecesariamente complejo.
Número de Funciones:

¿Qué es?: Este valor cuenta cuántas funciones hay en el código.
¿Qué indica?: Un número adecuado de funciones sugiere que el código está bien modularizado, lo que facilita su comprensión y mantenimiento. Sin embargo, si hay demasiadas funciones en un solo archivo, puede ser un signo de que el código necesita ser dividido en partes más pequeñas y manejables.
Proporción de Comentarios:

¿Qué es?: Esta estadística mide la cantidad de comentarios en comparación con el código real.
¿Qué indica?: Una buena proporción de comentarios sugiere que el código está bien documentado, lo que facilita la comprensión para otros desarrolladores (o para el mismo autor en el futuro). Sin embargo, demasiados comentarios pueden indicar que el código no es lo suficientemente claro y necesita ser simplificado.
¿Por qué son Importantes Estas Estadísticas?
Mantenibilidad: Un código que tiene una complejidad baja y está bien documentado es más fácil de mantener. Esto significa que si un desarrollador necesita hacer cambios, es menos probable que introduzca errores.

Facilidad de Comprensión: Las métricas nos ayudan a entender si el código es comprensible y si otros desarrolladores podrán trabajar con él sin mucha dificultad.

Identificación de Problemas: Si las métricas indican que hay demasiada complejidad o que hay un alto número de líneas de código en una sola función, esto puede señalar problemas que necesitan ser abordados para mejorar la calidad del software.

Mejora Continua: Al rastrear estas métricas a lo largo del tiempo, un equipo de desarrollo puede ver si su calidad de código está mejorando, lo que es vital para la evolución del proyecto.

Conclusión
En resumen, el análisis de métricas de código proporciona una visión cuantitativa de la calidad del software. Al entender y aplicar estas estadísticas, los equipos de desarrollo pueden tomar decisiones informadas para mejorar sus proyectos, reducir errores y facilitar la colaboración entre los desarrolladores.