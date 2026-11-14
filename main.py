from pyscript import document, when

@when("submit", "#form")
def manejar_clic(event):
    event.preventDefault()
    
    primer_dato = document.querySelector("#primer-dato").value
    segundo_dato = document.querySelector("#segundo-dato").value
    
    
    if primer_dato and segundo_dato:
        document.querySelector("#result").innerHTML = f"{int(primer_dato) + int(segundo_dato)}"
    else:
        document.querySelector("#result").innerHTML = "Ingrese ambos valores."