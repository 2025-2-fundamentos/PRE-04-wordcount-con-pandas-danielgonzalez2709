"""Taller evaluable"""

import os
import re
import pandas as pd
from collections import Counter


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job(input_directory, output_directory):
    """Job que cuenta la frecuencia de palabras en archivos de texto usando Pandas (optimizado)"""

    # Crear el directorio de salida si no existe
    os.makedirs(output_directory, exist_ok=True)

    # Usar Counter para contar palabras de manera más eficiente
    word_counter = Counter()

    # Leer todos los archivos del directorio de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_directory, filename)

            # Leer el contenido del archivo
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Convertir a minúsculas y extraer palabras (solo letras)
                words = re.findall(r'[a-zA-Z]+', content.lower())

                # Actualizar el contador directamente (más eficiente)
                word_counter.update(words)

    # Crear DataFrame directamente desde el Counter (más eficiente)
    df = pd.DataFrame(list(word_counter.items()), columns=['word', 'count'])

    # Ordenar alfabéticamente por palabra
    df = df.sort_values('word')

    # Guardar el resultado en el archivo part-00000
    output_file = os.path.join(output_directory, 'part-00000')
    df.to_csv(output_file, sep='\t', header=False, index=False)

    # Crear el archivo _SUCCESS para indicar que el proceso terminó exitosamente
    success_file = os.path.join(output_directory, '_SUCCESS')
    with open(success_file, 'w') as f:
        f.write('')

if __name__ == "__main__":

    run_job(
        "files/input",
        "files/output",
    )
