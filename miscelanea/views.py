from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import loader, Context, RequestContext
from miscelanea.models import Persona
from miscelanea.forms import LoginForm, PersonaForm

@login_required(login_url='/login/')
def home(request):    
    #cambia dependiendo de los permisos
    grupos=request.user.groups.filter(pk=1)
    context = RequestContext(request,{'grupos':grupos})
    response= render_to_response("admin_home.html", context_instance=context)
    return response
    
def log_in(request):
    if request.user.is_authenticated():
        response=HttpResponseRedirect('/')#falta en el diagrama de secuencia 1
        return response
    else:
        form = LoginForm()
        diccionario={'login_form':form}
        context = RequestContext(request,diccionario)
        token=csrf(request)
        context.update(token)
        return render_to_response("login.html",context)

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return render_to_response('logout.html', context_instance=RequestContext(request))

def validar_usuario(request):
    htmldoc=None
    if request.POST:
        datos=LoginForm(request.POST)
        result=datos.is_valid()
        if result:
            user=datos.cleaned_data['usuario']
            passw=datos.cleaned_data['password']
            usuario=authenticate(username=user,password=passw)
            if usuario is not None:
                login(request,usuario)
                return HttpResponseRedirect('/')
            else:
                htmldoc="login_error.html"
                #error usuario contrasena
        else:
            htmldoc="login.html"
            #error de formulario
    else:
        response=HttpResponseRedirect('/')
        return response
    context = RequestContext(request)
    response= render_to_response(htmldoc, context_instance=context)
    return response
    
def gestionar_usuarios(request):
    context = RequestContext(request)
    response= render_to_response("gestion_usuarios.html", context_instance=context)
    return response
    
def nuevo_usuario(request):
    form = PersonaForm()
    template = loader.get_template("nuevo_usuario.html")
    context = RequestContext(request,{'newuser_form':form})
    return HttpResponse({template.render(context)})

def crear_usuario(request):
    if request.POST:
        datos=PersonaForm(request.POST)
        if datos.is_valid():
            user=datos.cleaned_data['username']
            passw=datos.clean_password2()
            user = User(username=user,password=passw)
            user.set_password(passw)
            user.save()
            datos.user=user;
            datos.save();
            return HttpResponseRedirect('/')
        else:
            error=None
            template = loader.get_template("login_error.html")
            context = RequestContext(request,{'error_message':error})
            return HttpResponse({template.render(context)})
    else:
        return HttpResponseRedirect('/nuevo_usuario/')
        
def listar_usuarios(request):
    return Nonerequest
