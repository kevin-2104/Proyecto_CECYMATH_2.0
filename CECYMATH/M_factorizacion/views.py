from django.shortcuts import render

def factorizacion(request):
    factores = []
    numero = ""

    if request.method == "POST":
        numero = request.POST.get("numero")

        try:
            n = int(numero)
            divisor = 2
            while n > 1:
                if n % divisor == 0:
                    factores.append(divisor)
                    n //= divisor
                else:
                    divisor += 1
        except (ValueError, TypeError):
            factores = ["Error"]

    return render(
        request,
        "M_factorizacion/factorizacion.html",
        {
            "factores": factores,
            "numero": numero
        }
    )