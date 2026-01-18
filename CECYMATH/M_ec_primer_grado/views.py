from django.shortcuts import render

def ec_primer(request):
    a = b = ""
    resultado = ""

    if request.method == "POST":
        try:
            a = float(request.POST.get("a"))
            b = float(request.POST.get("b"))

            if a == 0:
                resultado = "No es una ecuación de primer grado"
            else:
                x = -b / a
                resultado = f"x = {x}"
        except:
            resultado = "Datos inválidos"

    return render(
        request,
        "M_ec_primer_grado/ec_primer.html",
        {
            "a": a,
            "b": b,
            "resultado": resultado
        }
    )