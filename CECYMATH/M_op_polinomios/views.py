from django.shortcuts import render

def polinomios(request):
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            coef1 = int(request.POST.get('coef1'))
            coef2 = int(request.POST.get('coef2'))
            operacion = request.POST.get('operacion')

            if operacion == 'suma':
                resultado = coef1 + coef2
            elif operacion == 'resta':
                resultado = coef1 - coef2
        except (TypeError, ValueError):
            error = "Ingresa valores válidos"

    return render(request, "M_op_polinomios/polinomios.html", {
        'resultado': resultado,
        'error': error
    })