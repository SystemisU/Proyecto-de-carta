from pyscript import document, window

a = window.prompt("Primer dato:")
b = window.prompt("Segundo dato:")

primer_dato = document.querySelector("#primer-dato")
segundo_dato = document.querySelector("#segundo-dato")
result = document.querySelector("#result")

primer_dato.value = a
segundo_dato.value = b

if a is None or b is None:
    result.innerHTML = "Ingrese ambos valores"
elif a.strip().isdigit() and b.strip().isdigit():
    a = int(a)
    b = int(b)
    result.innerHTML = f"{a + b}"
else:
    result.innerHTML = "Ingrese numeros no palabras"

primer_dato.disabled = True
segundo_dato.disabled = True