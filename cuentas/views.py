from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.warning(request, "¡Registro exitoso! Te doy la bienvenida a PF Gaming.")
            return redirect('home.index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cuentas/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'cuentas/login.html'

    def form_valid(self, form):
        messages.success(self.request, f"¡Hola {form.get_user().username}, has iniciado sesión!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al iniciar sesión. Verifica tus credenciales.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home.index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home.index')

    def post(self, request, *args, **kwargs):
        messages.info(request, "Has cerrado sesión correctamente.")
        return super().post(request, *args, **kwargs)
