import json
import re

def imprimir(message):
    # Imprime un mensaje
    print(message)

def normalizar_dato(lista:list):
    modificaciones = False
    # busca si la lista esta vacia
    if len(lista) == 0:
        print("Error, la lista esta vacia")
    else:
        # si no esta vacia recorre la lista buscando que normalizar
        for personaje in lista:
            if type(personaje["height"]) == str:
                # en este if buscamos si el dato esta en otro tipo para cambiarlo al tipo que queremos
                altura = int(personaje["height"])
                personaje["height"] = altura
                modificaciones = True
            
            if type(personaje["mass"]) == str:
                # en este if buscamos si el dato esta en otro tipo para cambiarlo al tipo que queremos
                peso = int(personaje["mass"])
                personaje["mass"] = peso
                modificaciones = True
        return lista
    # retornamos la lista modificada
    
    if modificaciones:
        # notificamos que se actualizaron los datos
        print("Datos normalizados")

def listar_personajes(nombre_archivo:str):
    with open(nombre_archivo, "r") as archivo:
        # buscamos el archivo Json
        data = json.load(archivo)
        # importamos la info del Json en una variable
        lista_copia = data["results"].copy()
        # copiamos la lista que contenia el Json
        return lista_copia
        # retornamos la lista ya copiada

def ordenar(lista:list, key:str):
    opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()

    while not re.search("asc|desc", opcion) or opcion == "":
        opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()

    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if opcion == "asc":
                if(lista[i][key] > lista[j][key]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if(lista[i][key] < lista[j][key]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    for personaje in lista:
        personaje_altura = personaje[key]
        personaje_altura_name = personaje["name"]
        imprimir(f"Personaje: {personaje_altura_name} | {personaje_altura}")
    return lista

def personaje_mas_alto(lista:list):
    mele_mas_alto = 0
    female_mas_alta = 0
    non_mas_alto = 0

    for personaje in lista:
        if personaje["gender"] == "male":
            if personaje["height"] > mele_mas_alto:
                mele_mas_alto = personaje["height"]
                nombre_mele = personaje["name"]
        elif personaje["gender"] == "female":
            if personaje["height"] > female_mas_alta:
                female_mas_alta = personaje["height"]
                nombre_female = personaje["name"]
        elif personaje["gender"] == "n/a":
            if personaje["height"] > non_mas_alto:
                non_mas_alto = personaje["height"]
                nombre_non = personaje["name"]
    mensaje = (f"""Personaje masculino mas alto: {nombre_mele} | {mele_mas_alto}
    \nPersonaje femenino mas alto: {nombre_female} | {female_mas_alta}
    \nPersonaje N/A mas alto: {nombre_non} | {non_mas_alto}
    """)
    return mensaje

def buscar_personajes(lista:list, key:str):
    buscar_personaje = input("Cual personaje quiere buscar? ")

    for personaje in lista:
        if re.search(buscar_personaje, personaje[key].lower()) != None:
            nombre_personaje = personaje[key]
            altura_personaje = personaje["height"]
            peso_personaje = personaje["mass"]
            genero_personaje = personaje["gender"]
            break
    mensaje = (f"""Nombre del personaje: {nombre_personaje}
    \nAltura del personaje: {altura_personaje}
    \nPeso del personaje: {peso_personaje}
    \nGenero del personaje: {genero_personaje}
    """)
    return mensaje

def opciones_menu():
    imprimir("""Opciones:
    \n1 - Lista de personajes(Ordenada por altura)
    \n2 - El personaje mas alto de cada genero
    \n3 - Lista de personajes(Ordenada por peso)
    \n4 - Buscador de personajes
    \n5 - Exportar a CSV
    \n0 - Salir
    """)

def menu_app(lista_personajes:list):
    while True:
        opciones_menu()
        opcion = input("Cual opcion va a elegir? ")
        if re.search("[0-6]", opcion) != None:
            opcion = int(opcion)
            match opcion:
                case 0:
                    break
                case 1:
                    imprimir(ordenar(lista_personajes, "height"))
                case 2:
                    imprimir(personaje_mas_alto(lista_personajes))
                case 3:
                    imprimir(ordenar(lista_personajes, "mass"))
                case 4:
                    imprimir(buscar_personajes(lista_personajes, "name"))
    
def starwars_app(nombre_archivo:str):
    lista = listar_personajes(nombre_archivo)
    lista = normalizar_dato(lista)
    menu_app(lista)