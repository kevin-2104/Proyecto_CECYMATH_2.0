from django.shortcuts import render

def jerarquia(request):
    resultado = None
    error = None
    expresion = ""

    if request.method == 'POST':
        expresion = request.POST.get('expresion')

        try:
          
            resultado = eval(expresion)
        except:
            error = "Expresión no válida"

    return render(request, "M_jer_operaciones/jerarquia.html", {
        'resultado': resultado,
        'error': error,
        'expresion': expresion
    })