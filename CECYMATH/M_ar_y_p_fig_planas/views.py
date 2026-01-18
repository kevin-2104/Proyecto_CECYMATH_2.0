from django.shortcuts import render
import math

def figuras(request):
    figura = ""
    area = ""
    perimetro = ""

    if request.method == "POST":
        figura = request.POST.get("figura")

        try:
            if figura == "cuadrado":
                lado = float(request.POST.get("lado"))
                area = lado ** 2
                perimetro = 4 * lado

            elif figura == "rectangulo":
                base = float(request.POST.get("base"))
                altura = float(request.POST.get("altura"))
                area = base * altura
                perimetro = 2 * (base + altura)

            elif figura == "circulo":
                radio = float(request.POST.get("radio"))
                area = math.pi * radio ** 2
                perimetro = 2 * math.pi * radio

        except:
            area = "Datos inválidos"
            perimetro = ""

    return render(
        request,
        "M_ar_y_p_fig_planas/figuras.html",
        {
            "figura": figura,
            "area": area,
            "perimetro": perimetro
        }
    )