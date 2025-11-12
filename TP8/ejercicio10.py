from typing import List

diccionario = {"a": 1,
               "b": 2,
               "c": 3,
               "d": 4,
               "e": 5,
               "f": 6
               }

a_eliminar = ["c","a","f"]

def eliminar_claves(diccionario: dict[str,int], a_eliminar: List[int])-> dict[int,str]:
    """pre: Recibe un diccionario con varios elementos
    post: Elimina del diccionario las claves previamente cargadas en una lista"""
    eliminadas = 0
    for clave in a_eliminar:
        if clave in diccionario:
            diccionario.pop(clave)
            eliminadas += 1
    print("Diccionario actualizado:", diccionario)
    print("Claves eliminadas:", eliminadas)
        
    


eliminar_claves(diccionario, a_eliminar)