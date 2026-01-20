from django.shortcuts import render

def sume(request):
    resultado = None

    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')

        if a and b:
            resultado = int(a) + int(b)

    return render(request, "M_suma/suma.html", {
        'resultado': resultado
    })