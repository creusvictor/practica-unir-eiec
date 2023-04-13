"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = "desc"


def sort_list(items, order):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    if (order == "asc"):
        return sorted(items, reverse=(False))
    elif (order == "desc"):
        return sorted(items, reverse=(True))
    else:
        print("EL parámetro dado no es válido, se ordenaran las palabras en orden descendente")
        return sorted(items, reverse=(True))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    sort_order = DEFAULT_ORDER
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        sort_order = sys.argv[3]
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento indica el orden en el que se quiere ordenar las palabras, asc (ascendente) o desc (descendiente)")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, sort_order))
