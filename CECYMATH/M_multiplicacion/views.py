from django.shortcuts import render

def multiplicacion(request):
    resultado = None

    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')

        if a and b:
            resultado = int(a) * int(b)

    return render(request, "M_multiplicacion/multiplicacion.html", {
        'resultado': resultado
    })