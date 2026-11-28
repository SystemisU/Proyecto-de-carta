import asyncio
from pyscript import document

datos = ""

pantalla = document.querySelector("#pantalla")
botones = document.querySelectorAll("#number")
operaciones = document.querySelectorAll("#operator")
borrar = document.querySelector("#delete")
regresar = document.querySelector("#reverse")
resultado = document.querySelector("#result")

while True:
    for i in botones:
        if i.matches(":active"):
            datos = datos + i.innerHTML.strip()
            pantalla.innerHTML = datos
            await asyncio.sleep(0.1)
    
    for i in operaciones:
        if i.matches(":active") and len(datos) > 0:
            if datos[-1].isdigit():
                datos = datos + i.innerHTML.strip()
                pantalla.innerHTML = datos
                await asyncio.sleep(0.1)
    
    if regresar.matches(":active"):
        datos = datos[:-1]
        pantalla.innerHTML = datos
        await asyncio.sleep(0.1)
    
    if borrar.matches(":active"):
        datos = ""
        pantalla.innerHTML = datos
        await asyncio.sleep(0.1)
    
    if resultado.matches(":active"):
        lista = []
        dato = ""
        
        for i, item in enumerate(datos):
            if item not in ("+", "×", "÷", "-"):
                dato += item 
                if i != len(datos) - 1:
                    continue

            lista.append(dato)
            lista.append(item)
            dato = ""

        lista = lista[:-1]
        
        i = 0
        while i < len(lista):
            if lista[i] in ('×', '÷'):
                izq = float(lista[i - 1])
                der = float(lista[i + 1])
                res = izq * der if lista[i] == '×' else izq / der if der != 0 else "No se puede dividir entre cero"
                
                lista[i - 1 : i + 2] = [res]
                i -= 1
            i += 1
        
        respuesta = lista[0]
        datos = ""
        if respuesta != "No se puede dividir entre cero":
            respuesta = float(lista[0])
            i = 1
            while i < len(lista):
                operador = lista[i]
                siguiente_num = float(lista[i + 1])
                
                if operador == '+':
                    respuesta += siguiente_num
                elif operador == '-':
                    respuesta -= siguiente_num
                i += 2
            datos = str(respuesta)
        pantalla.innerHTML = respuesta
        await asyncio.sleep(0.1)
    
    await asyncio.sleep(0.01)