from django.shortcuts import render
import math

def ec_segundo(request):
    a = b = c = ""
    resultado = ""

    if request.method == "POST":
        try:
            a = float(request.POST.get("a"))
            b = float(request.POST.get("b"))
            c = float(request.POST.get("c"))

            if a == 0:
                resultado = "No es ecuación de segundo grado"
            else:
                discriminante = b**2 - 4*a*c

                if discriminante > 0:
                    x1 = (-b + math.sqrt(discriminante)) / (2*a)
                    x2 = (-b - math.sqrt(discriminante)) / (2*a)
                    resultado = f"x₁ = {x1}, x₂ = {x2}"
                elif discriminante == 0:
                    x = -b / (2*a)
                    resultado = f"x = {x}"
                else:
                    resultado = "No tiene soluciones reales"

        except:
            resultado = "Datos inválidos"

    return render(
        request,
        "M_ec_segundo_grado/ec_segundo.html",
        {
            "a": a,
            "b": b,
            "c": c,
            "resultado": resultado
        }
    )