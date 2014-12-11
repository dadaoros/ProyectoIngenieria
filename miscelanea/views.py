from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import loader, Context, RequestContext
from miscelanea.models import Persona,Producto,Categoria,Proveedor,Canasta,DetalleVenta
from miscelanea.forms import LoginForm, PersonaForm, ProductoForm,BuscarProductoForm,CategoriaForm
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
    user=request.user
    result=user.is_authenticated()
    if result:
        response=HttpResponseRedirect('/')
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
                    c=Canasta()
                    c.save()
                    c.operario=user
                    c.save()
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
    diccionario={'newproduct_form':form}
    context = RequestContext(request,diccionario)
    response= render_to_response("nuevo_producto.html", context_instance=context)
    return response

def crear_producto(request):
    datos=ProductoForm(request.GET)
    error=None
    htmldoc="nuevo_producto.html"
    if datos.is_valid():
        try:
            datos.save()
        except IntegrityError, e:
            error="El producto que intenta ingresar ya existe!"                      
        else:

            htmldoc="operacion_exitosa.html"
    else:
        error="Revise que los datos ingresados sean correctos!"         
    diccionario={'error_message':error,"newproducto_form":datos}
    context = RequestContext(request,diccionario)
    response= render_to_response(htmldoc, context_instance=context)
    return response 
def buscar_productos(request):
    form = BuscarProductoForm(request.GET)
    diccionario={'buscarproducto_form':form}
    context = RequestContext(request,diccionario)
    response= render_to_response("buscar_producto.html", context_instance=context)
    return response

def listar_productos(request):
    form = BuscarProductoForm(request.GET)
    errors=""
    result=form.is_valid()
    if result:
        idProducto=form.cleaned_data['numeroReferencia']
        if idProducto is None:
            idProducto=""
        nombre=form.cleaned_data['nombreProducto']
        if nombre is None:
            nombre=""
        marca=form.cleaned_data['marca']
        if marca is None:
            marca=""
        try:
            productos=Producto.objects.filter(nombreProducto__contains=nombre,numeroReferencia__contains=idProducto,marca__contains=marca)
        except:
            errors="No se pudo obtener el listado de productos"
    else:
        errors=form.errors
    diccionario={'productos':productos,'errores':errors}                    
   
    context = RequestContext(request,diccionario)
    response= render_to_response("lista_productos.html", context_instance=context)
    return response
def gestionar_categorias(request):
    diccionario=listar_categorias()
    context = RequestContext(request,diccionario)
    response= render_to_response("gestion_categorias.html", context_instance=context)
    return response
def listar_categorias():
    errors=""
    try:
        categorias=Categoria.objects.all().order_by('pk')
    except:
        errors="No se pudo Obtener el listado de categorias!"
        categorias=None
    else:
        if not categorias:
            errors="No hay categorias actualmente"
    diccionario={'categorias':categorias,'errores':errors}
    return diccionario

def nueva_categoria(request):
    form = CategoriaForm()
    diccionario={'newcategory_form':form}
    context = RequestContext(request,diccionario)
    response= render_to_response("nueva_categoria.html", context_instance=context)
    return response

def crear_categoria(request):
    datos=CategoriaForm(request.GET)
    error=None
    htmldoc="nueva_categoria.html"
    if datos.is_valid():
        try:
            datos.save()
        except IntegrityError, e:
            error="La Categoria que intenta ingresar ya existe!"                      
        else:
            htmldoc="operacion_exitosa.html"
    else:
        error="Revise que los datos ingresados sean correctos!"         
    diccionario={'error_message':error,"newcategory_form":datos}
    context = RequestContext(request,diccionario)
    response= render_to_response(htmldoc, context_instance=context)
    return response

#Modulo Operarios

def gestionar_venta(request):
    diccionario=listar_productos_canasto(request)
    context = RequestContext(request,diccionario)
    response= render_to_response("gestion_ventas.html", context_instance=context)
    return response
def listar_productos_canasto(request):
    user=request.user
    try:
        canasto=Canasta.objects.filter(operario=user)
        productos=canasto[0].detalleventa_set.all()
        error=""
    except:
        error="No se pudo obtener el listado de productos"
        productos=""
    else:
        if not productos:
            error="No existen productos aun en el carro de compras"   
    total=0
    for p in productos:
        total+=p.cantidad*p.producto.precio

    diccionario={"productos":productos,"errores":error,"total":total}
    return diccionario
def remover_productos(request):
    items=request.GET.getlist('seleccion','')
    user=request.user
    for item in items:
        detalle=DetalleVenta.objects.filter(pk=item)
        detalle.delete()

    return HttpResponseRedirect('/')
    context = RequestContext(request,{'respuesta':seleccion})
    response= render_to_response("gestion_ventas.html", context_instance=context)
    return response
def finalizar_venta(request):
    diccionario=listar_productos_canasto(request)
    if diccionario['errores'] is not "":
        pass
    else:
        finalizado=reducir_inventario(diccionario)
        if finalizado is True:
            htmldoc="recibo_compra.html" 
        else:
            diccionario['errores']=finalizado
            htmldoc="gestion_ventas.html"
    context = RequestContext(request,diccionario)
    response= render_to_response(htmldoc, context_instance=context)
    return response

def reducir_inventario(diccionario):
    existencias=revisar_existencias(diccionario)
    if not existencias:
        return "No hay existencias suficientes"
    else:
        for detalle in diccionario['productos']:
            producto=detalle.producto
            e_actual=producto.existencias
            e_solicitada=detalle.cantidad
            producto.existencias=e_actual-e_solicitada
            producto.save()
        return True    
def revisar_existencias(diccionario):
    for p in diccionario['productos']:
        e_actual=p.producto.existencias
        e_solicitada=p.cantidad
        if e_actual<e_solicitada:
            return False
    return True
def buscar_producto(request):
    form = BuscarProductoForm(request.GET)
    diccionario={'buscarproducto_form':form}
    context = RequestContext(request,diccionario)
    response= render_to_response("buscar_producto_para_anadir.html", context_instance=context)
    return response
def listar_productos_b(request):
    form = BuscarProductoForm(request.GET)
    errors=""
    result=form.is_valid()
    if result:
        idProducto=form.cleaned_data['numeroReferencia']
        if idProducto is None:
            idProducto=""
        nombre=form.cleaned_data['nombreProducto']
        if nombre is None:
            nombre=""
        marca=form.cleaned_data['marca']
        if marca is None:
            marca=""
        try:
            productos=Producto.objects.filter(nombreProducto__contains=nombre,numeroReferencia__contains=idProducto,marca__contains=marca)
        except:
            errors="No se pudo obtener el listado de productos"
    else:
        errors=form.errors
    diccionario={'productos':productos,'errores':errors}                    
   
    context = RequestContext(request,diccionario)
    response= render_to_response("lista_productos+.html", context_instance=context)
    return response