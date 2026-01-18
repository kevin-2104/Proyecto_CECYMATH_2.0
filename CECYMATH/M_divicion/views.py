from django.shortcuts import render

def divicion(request):
    dividendo = ""
    divisor = ""
    resultado = ""

    if request.method == "POST":
        try:
            dividendo = float(request.POST.get("dividendo"))
            divisor = float(request.POST.get("divisor"))

            if divisor == 0:
                resultado = "No se puede dividir entre cero"
            else:
                resultado = dividendo / divisor
        except:
            resultado = "Datos inválidos"

    return render(
        request,
        "M_divicion/divicion.html",
        {
            "dividendo": dividendo,
            "divisor": divisor,
            "resultado": resultado
        }
    )