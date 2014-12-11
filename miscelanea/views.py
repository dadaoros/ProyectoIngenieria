from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import loader, Context, RequestContext
from miscelanea.models import Persona
from miscelanea.forms import LoginForm, PersonaForm, ProductoForm
from django.db import IntegrityError

@login_required(login_url='/login/')
def home(request):
    grupos=request.user.groups.all()
    grupo=grupos[0].name
    if grupo=="Administrador":
        htmldoc="admin_home.html"
    else:
        if grupo=="Operario":
            htmldoc="home.html"
        else:
            htmldoc="no_home.html"
    context = RequestContext(request)
    response= render_to_response(htmldoc, context_instance=context)
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
        response= render_to_response("login.html",context)
        return response

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
    context = RequestContext(request,{'newuser_form':form})
    response= render_to_response("nuevo_usuario.html", context_instance=context)
    return response

def crear_usuario(request):
    if request.POST:
        datos=PersonaForm(request.POST)
        error=None
        htmldoc="nuevo_usuario.html"
        if datos.is_valid():
            user=datos.cleaned_data['username']
            passw=datos.clean_password()
            if passw is None:
                error="Revise que las dos contrasenas coincidan!"
            else:
                user = User(username=user,password=passw)
                user.set_password(passw)
                try:
                    user.save()
                except IntegrityError, e:
                    error="Ya existe un nombre de usuario igual al ingresado!"            
                else:
                    grupo = Group.objects.get(name='Operario')
                    grupo.user_set.add(user)
                    persona=datos.save()
                    persona.user=user
                    persona.save()
                    htmldoc="operacion_exitosa.html"
        else:
            error="Revise que los datos ingresados sean correctos!"
        diccionario={'error_message':error,"newuser_form":datos}
        context = RequestContext(request,diccionario)
        response= render_to_response(htmldoc, context_instance=context)
        return response
    else:
        return HttpResponseRedirect('/')
        
def listar_usuarios(request):
    #No se pudo realizar la operacion
    try:
        usuarios=User.objects.all()
    except:
        usuarios=None
        error="No se pudo obtener el listado de usuarios"
    if usuarios is not None:        
        diccionario={'usuarios':usuarios}
        context = RequestContext(request,diccionario)        
    else:
        error="No hay Usuarios Registrados"
        diccionario={'error_message':error}
        context = RequestContext(request,diccionario)
    response= render_to_response("lista_usuarios.html", context_instance=context)
    return response

def gestionar_productos(request):
    context = RequestContext(request)
    response= render_to_response("gestion_productos.html", context_instance=context)
    return response

def nuevo_producto(request):
    form = ProductoForm()
    template = loader.get_template("nuevo_producto.html")
    context = RequestContext(request,{'newproduct_form':form})
    return HttpResponse({template.render(context)})