from django.shortcuts import render

def recta(request):
    inicio = None
    desplazamiento = None
    desplazamiento_abs = None
    resultado = None

    if request.method == 'POST':
        inicio = request.POST.get('inicio')
        desplazamiento = request.POST.get('desplazamiento')

        if inicio and desplazamiento:
            inicio = int(inicio)
            desplazamiento = int(desplazamiento)
            resultado = inicio + desplazamiento
            desplazamiento_abs = abs(desplazamiento)

    return render(request, "M_recta_numerica/recta.html", {
        'inicio': inicio,
        'desplazamiento': desplazamiento,
        'desplazamiento_abs': desplazamiento_abs,
        'resultado': resultado
    })