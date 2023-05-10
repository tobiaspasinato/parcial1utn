import json
import re

def imprimir(message):
    # va a obtener cualquier dato (mayormente str)
    # Imprime un mensaje
    print(message)

def normalizar_dato(lista:list):
    # obtiene una lista como parametro
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
    # obtiene el nombre del archivo como parametro
    with open(nombre_archivo, "r") as archivo:
        # buscamos el archivo Json
        data = json.load(archivo)
        # importamos la info del Json en una variable
        lista_copia = data["results"].copy()
        # copiamos la lista que contenia el Json
        return lista_copia
        # retornamos la lista ya copiada

def ordenar(lista:list, key:str):
    # va a obtener una lista y key como parametro
    opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()
    # le pedimos al usuario de la consola que escriba la forma de ordenar la lisata

    while not re.search("asc|desc", opcion) or opcion == "":
        opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()
        # verifica que el usuario ingrese una de las dos opciones dadas por el programa

    for i in range(len(lista)-1):
        # itera en la menos en el ultimo dato de esta
        for j in range(i+1,len(lista)):
            # itera en la lista una posicion adelante del primer for
            if opcion == "asc":
                # si la opcion elegida es la que busca el if entra en el
                if(lista[i][key] > lista[j][key]):
                    # compara si el elemoento de la lista i es mayor que el de la lista j
                    aux = lista[i]
                    # si ingreso al if porcede a guardar el elemento i en la variable auxiliar
                    lista[i] = lista[j]
                    # sobre escribe los datos de "lista[i]" por los de "lista[j]"
                    lista[j] = aux
                    # y usamos el aux para mover el valor que se sobrescribio anteriormente
            else:
                # este else lo que hace es mandar al usuario a la opcion que eligio (al ser solo 2 posibles rutas)
                if(lista[i][key] < lista[j][key]):
                    # compara si el elemoento de la lista i es mayor que el de la lista j
                    aux = lista[i]
                    # si ingreso al if porcede a guardar el elemento i en la variable auxiliar
                    lista[i] = lista[j]
                    # sobre escribe los datos de "lista[i]" por los de "lista[j]"
                    lista[j] = aux
                    # y usamos el aux para mover el valor que se sobrescribio anteriormente
    for personaje in lista:
        # con la lista ya ordenada como el usuario quiere iteramon en cada elemento de la lista
        personaje_ordenado = personaje[key]
        # guarda el dato del personaje que queremos mostrar
        personaje_ordenado_name = personaje["name"]
        # para no confundir al usuario guardamos el nombre del personaje del dato anterior
        imprimir(f"Personaje: {personaje_ordenado_name} | {personaje_ordenado}")
        # imprimimos los datos anteriores cada vez que el for itere en algun elemoento
    return lista
    # retornamos la lista ordenada para el uso de la exportacion al csv

def personaje_mas_alto(lista:list):
    # obtiene una lista como parametro
    mele_mas_alto = 0
    female_mas_alta = 0
    non_mas_alto = 0
    # inicializamos variables para que guarden el personaje mas alto que se va a ir dando

    for personaje in lista:
        # itera el for en cada elemento de la lista
        if personaje["gender"] == "male":
            # si el elemento de la lista posee el genero que busca el if entra en el
            if personaje["height"] > mele_mas_alto:
                # este if se encarga del comparar si el elemento que posee el mas alto es mas chico que el nueco dado por iterar en la lista
                mele_mas_alto = personaje["height"]
                # si entra al if guarda la altura del personaje mas alto hasta ahora para compararla en futuros casos
                nombre_mele = personaje["name"]
                # guarda el nombre del personaje para mostarlo despues por consola
        elif personaje["gender"] == "female":
            # si el elemento de la lista posee el genero que busca el if entra en el
            if personaje["height"] > female_mas_alta:
                # este if se encarga del comparar si el elemento que posee el mas alto es mas chico que el nueco dado por iterar en la lista
                female_mas_alta = personaje["height"]
                # si entra al if guarda la altura del personaje mas alto hasta ahora para compararla en futuros casos
                nombre_female = personaje["name"]
                # guarda el nombre del personaje para mostarlo despues por consola
        elif personaje["gender"] == "n/a":
            # si el elemento de la lista posee el genero que busca el if entra en el
            if personaje["height"] > non_mas_alto:
                # este if se encarga del comparar si el elemento que posee el mas alto es mas chico que el nueco dado por iterar en la lista
                non_mas_alto = personaje["height"]
                # si entra al if guarda la altura del personaje mas alto hasta ahora para compararla en futuros casos
                nombre_non = personaje["name"]
                # guarda el nombre del personaje para mostarlo despues por consola
    mensaje = (f"""Personaje masculino mas alto: {nombre_mele} | {mele_mas_alto}
    \nPersonaje femenino mas alto: {nombre_female} | {female_mas_alta}
    \nPersonaje N/A mas alto: {nombre_non} | {non_mas_alto}
    """)
    # creamos el mensaje que mustre lo que el usuario busca
    return mensaje
    # retornamos el mensaje para mostrarlo ejn consola despues

def buscar_personajes(lista:list, key:str):
    # va a obtener una lista y key como parametro
    buscar_personaje = input("Cual personaje quiere buscar? ")
    # le preguntamos al usuario de la consola el nombre del personaje que esta buscando

    for personaje in lista:
        # iteramos en cada elemento de la lista
        if re.search(buscar_personaje, personaje[key].lower()) != None:
            # y en cada elememento iterado buscamos coincidencias en lo qu eel usuario busco y en los elementos de cada diccionario
            nombre_personaje = personaje[key]
            # si entro guardamos cada dato de diccionario
            altura_personaje = personaje["height"]
            # si entro guardamos cada dato de diccionario
            peso_personaje = personaje["mass"]
            # si entro guardamos cada dato de diccionario
            genero_personaje = personaje["gender"]
            # si entro guardamos cada dato de diccionario
            break
            # salimos del for asi no sigue buscando algo que ya encontro
    mensaje = (f"""Nombre del personaje: {nombre_personaje}
    \nAltura del personaje: {altura_personaje}
    \nPeso del personaje: {peso_personaje}
    \nGenero del personaje: {genero_personaje}
    """)
    # creamos la variable mensaje para despues mostrar por consola los datos de la busqueda
    return mensaje
    # retornamos el mensaje ya listo

def crear_csv(lista:list, nombre_archivo:str):
    # va a obtener una lista y nombre del archivo como parametro
    with open(nombre_archivo, "w") as archivo:
        # abrimos un archivo mediante "w"(que sobreescribe o en el caso de no esncontrar el elemento lo crea)
        for personaje in lista:
            # iteramos en cada elemento de la lista
            dato_por_linea = "{0},{1},{2},{3}\n".format(personaje["name"],personaje["height"],personaje["mass"],personaje["gender"])
            # preparamos lo que queremos que guarde el archivo csv
            archivo.write(dato_por_linea)
            # hacemos que copie cada dato en el archivo csv

def opciones_menu() -> None:
    # sin parametros
    imprimir("""Opciones:
    \n1 - Lista de personajes(Ordenada por altura)
    \n2 - El personaje mas alto de cada genero
    \n3 - Lista de personajes(Ordenada por peso)
    \n4 - Buscador de personajes
    \n5 - Exportar a CSV
    \n0 - Salir
    """)
    # imprime el menu cada vez que llamamos a la funcion

def menu_app(lista_personajes:list):
    # va a obtener una lista como parametro
    lista_csv = []
    # creamos una lista vacia para que guarde la lista de la opcion 1
    bandera_csv = False
    # creamos esta bandera para verificar el ingreso a la opcion 1
    while True:
        # creamos el bucle que va a preguntar que opcion vamos a elegir infinitamente hasta que se rompa
        opciones_menu()
        # mostramos el menu de opciones
        opcion = input("Cual opcion va a elegir? ")
        # preguntamos que opcion va a elegir al usuario
        if re.search("[0-6]", opcion) != None:
            # verificamos que la opcion dada por el usuario coinsida con alguna
            opcion = int(opcion)
            # si entro al if convertimos el valor de la opcion que dio el usuario para el menu
            match opcion:
                # entramos en el match que va a bucar la opcion
                case 0:
                    imprimir("Fin del programa. Fue un placer servirle amo")
                    break
                    # en el caso de entrar en esta opcion sale del prgrama 
                case 1:
                    lista_csv = ordenar(lista_personajes, "height")
                    # "lista_csv" va a guardar el retorno de "ordenar" para mas adelante y ordenar va a funcionar con la lista dada en los parametros
                    bandera_csv = True
                    # se encarga de verificar el paso por esta opcion
                case 2:
                    imprimir(personaje_mas_alto(lista_personajes))
                    # imprime el mensaje que retorna la funcion, y parsonaje_mas_alto realiza su funcion con los datos de lista
                case 3:
                    ordenar(lista_personajes, "mass")
                    # cumple la funcion con los parametros dados
                case 4:
                    imprimir(buscar_personajes(lista_personajes, "name"))
                    # imprime y cumple la funcion con los parametros dados
                case 5:
                    if bandera_csv == False:
                        # en el caso de no tener el verificador entra al if
                        print("Usted no uso todavia la opcion 1")
                        # muestra el mensaje
                    else:
                        # en el caso de si tener el verificador entra al else
                        crear_csv(lista_csv, "data.csv")
                        # realiza la funcion con los parametros dados

def starwars_app(nombre_archivo:str):
    # le ingresamos el nombre del archivo como parametro
    lista = listar_personajes(nombre_archivo)
    # busca el archivo y lo exporta al programa
    lista = normalizar_dato(lista)
    # si hay algun dato en otro tipo al que queremos los modifica y ademas verifica que la lista no este vacia
    menu_app(lista)
    # hace arrancar las funciones del prog