from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse


from .formUsuario import RegistroUsuario, EditarPerfil, RegistroTipoUsuario, contraseñaForm

from django.contrib.auth.models import User


from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from gestionUsuarios.formUsuario import Login

def registrar_usuario(request):
    Publisher = False
    if User.objects.filter(id=request.user.id, tipousuario=2):
        Publisher = True
    formRegistro = RegistroUsuario(request.POST)
    formRegistroTipo = RegistroTipoUsuario(request.POST)
    if request.method == "POST":
        if formRegistro.is_valid() and formRegistroTipo.is_valid():
            formRegistro.save()
            username = User.objects.last()
            user = User.objects.get(username=username)
            idtipo = formRegistroTipo.cleaned_data.get("tipo", "")
            user.tipousuario_set.add(idtipo,user.id)
            return redirect('login')
    context = {'formRegistro': formRegistro,'formRegistroTipoUsuario':formRegistroTipo,}
    return render(request, "registrar_usuario.html", context)

def editar_usuario(request):
    Publisher = False
    if User.objects.filter(id=request.user.id, tipousuario=2):
        Publisher = True
    usuario = User.objects.get(id=request.user.id)
    formEditar = EditarPerfil(instance=usuario)
    if request.method == "POST":
        formEditar = EditarPerfil(request.POST, instance=usuario)
        if formEditar.is_valid():
            formEditar.save()
            return redirect('mostrarTarjeta')
    context = {'formEditar': formEditar,'Publisher':Publisher}
    return render(request, "editar_usuario.html", context)


def base_wiki(request):
    b = get_template('baseWiki.html')
    return HttpResponse(b.render({}))

#Para los errores
def error404(request, exception):
    return render(request,'error404.html')

def error403(request, exception):
    return render(request,'error403.html')

def error400(request, exception):
    return render(request,'error400.html')

def error500(request):
    return render(request,'error500.html')

def iniciar_sesion(request):
    loginForm = Login(request.POST)
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mostrarTarjeta')
            else:
                mensaje = "Usuario o contraseña incorrecta"
                return render(request, "login.html", {'loginForm': loginForm,'msg':mensaje})
    return render(request, "login.html", {'loginForm':loginForm})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def prueba(request):
    b = get_template('prueba.html')
    return HttpResponse(b.render({}))

def cambio_contraseña(request):
    Publisher = False
    if User.objects.filter(id=request.user.id, tipousuario=2):
        Publisher = True
    form = contraseñaForm(request.user)
    if request.method == 'POST':
        form = contraseñaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('editarU')
    return render(request, 'cambio_contraseña.html', {'form': form,'Publisher':Publisher})
