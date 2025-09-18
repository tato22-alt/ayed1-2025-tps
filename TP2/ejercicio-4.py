from typing import List

original = [32,54,76,1,22,5,87,43]
eliminar = [22, 544, 1]

def eliminar_valor(original: List[int], eliminar: List[int]) -> None:
    """pre: recibe dos listas de enteros
    post: modifica la lista original eliminando los valores que aparecen en eliminar"""
    print("Original:", original)
    print("Eliminar:", eliminar)

    for e in eliminar:
        i = 0
        while i < len(original):
            if original[i] == e:
                original.pop(i)
            else:
                i += 1

    print("Resultado:", original)



eliminar_valor(original, eliminar)
