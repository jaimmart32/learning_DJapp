from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Registra un nuevo usuario."""

    if request.method != 'POST':
        # Muestra un formulario de registro en blanco.
        form = UserCreationForm()
    else:
        # Procesa un formulario cumplimentado.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Inicia la sesión del usuario y lo redirige a la pagina de inicio.
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)