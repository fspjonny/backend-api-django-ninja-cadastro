from django.shortcuts import redirect, render


def initial(request):
    return render(request, 'persons/index.html')

def handler404(request, exception=None):
    return redirect('persons:initial')
