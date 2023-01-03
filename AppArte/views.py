from django.shortcuts import render
from AppArte.models import *
from AppArte.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


#        VISTA DE PAGINA DE INICIO

def inicio(request):
    
    return render(request, 'AppArte/inicio.html')

#        VISTA DE DISCOS Y SUS OPCIONES

def discos(request):
    
    return render(request, 'AppArte/discos.html')

#       VISTA DE LIBROS Y SUS OPCIONES

def libros(request):
    
    return render(request, 'AppArte/libros.html')

#       VISTA DE PINTURAS Y SUS OPCIONES

def pinturas(request):
    
    return render(request, 'AppArte/pinturas.html')


#       VISTA DE INICIO DE SESION

def iniciarSesion(request):
    
    if request.method == "POST":
    
        formu= AuthenticationForm(request, data = request.POST)
        
        if formu.is_valid():
            
            usuario= formu.cleaned_data.get("username")
            contra= formu.cleaned_data.get("password")
            user= authenticate(username=usuario, password=contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "AppArte/inicio.html", {"mensaje":f"Bienvenido a mi blog, {user}."})
        else:
            
            return render(request, "AppArte/inicio.html", {"mensaje":"No se pudo iniciar sesión"})
        
    else:
        
        formu= AuthenticationForm()
        
    return render(request,  "AppArte/login.html", {"formulario": formu})
    

#       VISTA DE REGISTRO DE USUARIO

def registrar(request):
    
    if request.method == "POST":
        
        formu= registroUsuario(request.POST)
            
        if formu.is_valid():
                username = formu.cleaned_data["username"]
                formu.save()
                return render(request, "AppArte/inicio.html", {"mensaje":"Registrado correctamente"})
        
    else:
        
        formu= registroUsuario()
        
    return render(request, "AppArte/registro.html", {"formulario": formu})    

#       VISTA DE EDICION DE USUARIO

@login_required

def editarUsuario(request):
    
    usuario= request.user
    
    if request.method == "POST":
        
        formula = editarUserForm(request.POST)        
        
        if formula.is_valid():
            
            informa = formula.cleaned_data
            
            usuario.email = informa["email"]
            usuario.set_password = informa["password1"]
            usuario.first_name = informa["first_name"]
            usuario.last_name = informa["last_name"]
            
            usuario.save()
            
            return render(request, "AppArte/inicio.html")
    else:
        
        formula = editarUserForm(initial={"email": usuario.email,
                                        "first_name": usuario.first_name,
                                        "last_name": usuario.last_name,
                                        })
        
    return render(request, "AppArte/editarUsuario.html", {"formulario": formula, "usuario": usuario})       

#       VISTA DE AGREGAR FOTO DE PERFIL

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
        
        formu= avatarForm(request.POST, request.FILES)
            
        if formu.is_valid():
                
                usuarioActual= User.objects.get(username=request.user)
                avatar= Avatar(usuario = usuarioActual, imagen=formu.cleaned_data["imagen"])
                avatar.save()
                
                return render(request, "AppArte/inicio.html")
        
    else:
        
        formu= avatarForm()
        
    return render(request, "AppArte/agregarAvatar.html", {"formulario": formu})    


#        VISTA DE AGREGAR LIBRO

@login_required
def formularioLibros(request):
    
    if request.method == "POST":
    
        formulario1 = formLibros(request.POST, request.FILES)
    
        print(formulario1)
        
        if formulario1.is_valid:
            
            informacion = formulario1.cleaned_data
            
            libro = Libros(nombre=informacion['nombre'], autor=informacion['autor'], año=informacion['año'],
                        genero=informacion['genero'], puntaje=informacion['puntaje'], descripcion=informacion['descripcion'], 
                        usuarioBlog=request.user, portada=informacion['portada'])
            
            libro.save()
            
            formulario1 = formLibros()
            
            return render(request, "AppArte/librosformulario.html", {"formulario1": formulario1}  )
        
        
    else:
        
            formulario1 = formLibros()    
        
            return render(request, "AppArte/librosformulario.html", {"formulario1": formulario1} )

#        VISTA DE AGREGAR DISCO

@login_required

def formularioDiscos(request):
    
    if request.method == 'POST':
    
        formulario2 = formDiscos(request.POST, request.FILES)
    
        print(formulario2)
        
        if formulario2.is_valid():
            
            

            informacion2 = formulario2.cleaned_data
            
            disco = Discos(nombre=informacion2['nombre'], artista=informacion2['artista'], año=informacion2['año'], genero=informacion2['genero'], 
                            puntaje=informacion2['puntaje'], usuarioBlog=request.user, tapa=informacion2['tapa'])
            
            disco.save()
            
            formulario2 = formDiscos()
            
            return render(request, "AppArte/discosformulario.html", {"formulario2": formulario2}  )
        
        
    else:
        
            formulario2 = formDiscos()    
        
    return render(request, "AppArte/discosformulario.html", {"formulario2": formulario2} )

#       VISTA DE AGREGAR PINTURA

@login_required

def formularioPinturas(request):
    
    if request.method == "POST":
    
        formulario3 = formPinturas(request.POST, request.FILES)
    
        print(formulario3)
        
        if formulario3.is_valid:
            
            informacion3 = formulario3.cleaned_data
            
            pintura = Pinturas(nombre=informacion3['nombre'], artista=informacion3['artista'], año=informacion3['año'], 
                            descripcion=informacion3['descripcion'], usuarioBlog=request.user, foto=informacion3['foto'])
            
            pintura.save()
            
            formulario3 = formPinturas()
            
            return render(request, "AppArte/pinturasformulario.html", {"formulario3": formulario3}  )
        
        
    else:
        
            formulario3 = formPinturas()    
        
            return render(request, "AppArte/pinturasformulario.html", {"formulario3": formulario3} )
        

#        VISTAS DE BUSCAR DISCOS 

def busquedaDiscos(request):
    
    return render(request, "AppArte/busquedaDiscos.html")

def resultadosDiscos(request):
    
    if request.GET["nombre"]:
        
        nombreBusqueda= request.GET["nombre"]
        
        discoResultados= Discos.objects.filter(nombre__icontains=nombreBusqueda)
        
        print(discoResultados)
        
        
        info = {"discoResultados":discoResultados, "nombrebusqueda":nombreBusqueda}
        return render(request, "AppArte/resultadosDiscos.html", info)
    
    if request.GET['artista']:
        
        artistaBusqueda= request.GET["artista"]
        
        discoResultados2= Discos.objects.filter(artista__icontains=artistaBusqueda)
        
        print(discoResultados2)
        
        
        info2 = {"discoResultados2":discoResultados2, "artistabusqueda":artistaBusqueda}
        return render(request, "AppArte/resultadosDiscos.html", info2)
    
    

#       VISTA DE BUSCAR LIBROS

def busquedaLibros(request):
    
    return render(request, "AppArte/busquedaLibros.html")

def resultadosLibros(request):
    
    if request.GET["nombre"]:
        
        nombreBusqueda= request.GET["nombre"]
        
        libroResultados= Libros.objects.filter(nombre__icontains=nombreBusqueda)
        
        print(libroResultados)
        
        
        info = {"libroResultados":libroResultados, "nombrebusqueda":nombreBusqueda}
        return render(request, "AppArte/resultadosLibros.html", info)
    
    if request.GET['autor']:
        
        autorBusqueda= request.GET["autor"]
        
        libroResultados2= Libros.objects.filter(autor__icontains=autorBusqueda)
        
        print(libroResultados2)
        
        
        info2 = {"libroResultados2":libroResultados2, "autorbusqueda":autorBusqueda}
        return render(request, "AppArte/resultadosLibros.html", info2)
    
    

#       VISTAS DE BUSCAR PINTURAS

def busquedaPinturas(request):
    
    return render(request, "AppArte/busquedaPinturas.html")

def resultadosPinturas(request):
    
    if request.GET["nombre"]:
        
        nombreBusqueda= request.GET["nombre"]
        
        pinturaResultados= Pinturas.objects.filter(nombre__icontains=nombreBusqueda)
        
        print(pinturaResultados)
        
        
        info = {"pinturaResultados":pinturaResultados, "nombrebusqueda":nombreBusqueda}
        return render(request, "AppArte/resultadosPinturas.html", info)
    
    if request.GET['artista']:
        
        artistaBusqueda= request.GET["artista"]
        
        pinturaResultados2= Pinturas.objects.filter(artista__icontains=artistaBusqueda)
        
        print(pinturaResultados2)
        
        
        info2 = {"pinturaResultados2":pinturaResultados2, "artistabusqueda":artistaBusqueda}
        return render(request, "AppArte/resultadosPinturas.html", info2)
    

#        VISTA BASADA EN CLASE PARA MOSTRAR TODOS LOS DISCOS

class listaDiscos(ListView):
    model= Discos

#        VISTA BASADA EM CLASE PARA VER INFORMACION DE UN DISCO

class detalleDiscos(DetailView):
    
    model= Discos
    success_url= "AppArte/verDiscos/"
    fields = ["nombre", "artista", "año", "genero", "puntaje", "descripcion"]

#       VISTA BASADA EN CLASE PARA EDITAR UN DISCO

class actualizarDiscos(LoginRequiredMixin, UpdateView):
    
    model= Discos
    success_url= "/verDiscos/"
    fields = ["nombre", "artista", "año", "genero", "puntaje", "descripcion", "tapa"]
    
#        VISTA BASADA EN CLASE PARA BORRAR UN DISCO
    
class borrarDiscos(LoginRequiredMixin, DeleteView):
    
    model= Discos
    success_url= "/verDiscos/"
    

#       VISTA BASADA EN CLASE PARA MOSTRAR TODOS LOS LIBROS

class listaLibros(ListView):

    model= Libros

#       VISTA BASADA EM CLASE PARA VER INFORMACION DE UN LIBRO

class detalleLibros(DetailView):
    
    model= Libros
    success_url= "AppArte/verLibros/"
    fields = ["nombre", "autor", "año", "genero", "puntaje", "descripcion"]

#       VISTA BASADA EN CLASE PARA EDITAR UN LIBRO

class actualizarLibros(LoginRequiredMixin, UpdateView):
    
    model= Libros
    success_url= "/verLibros/"
    fields = ["nombre", "autor", "año", "genero", "puntaje", "descripcion", "portada"]

#       VISTA BASADA EN CLASE PARA BORRAR UN LIBRO
    
class borrarLibros(LoginRequiredMixin, DeleteView):
    
    model= Libros
    success_url= "/verLibros/"
    
#        VISTA BASADA EN CLASE PARA MOSTRAR TODAS LAS PINTURAS

class listaPinturas(ListView):
    
    model= Pinturas

#       VISTA BASADA EM CLASE PARA VER INFORMACION DE UNA PINTURA

class detallePinturas(DetailView):
    
    model= Pinturas
    success_url= "AppArte/verPinturas/"
    fields = ["nombre", "artista", "año", "descripcion"]

#       VISTA BASADA EN CLASE PARA EDITAR UNA PINTURA

class actualizarPinturas(LoginRequiredMixin, UpdateView):
    
    model= Pinturas
    success_url= "/verPinturas/"
    fields = ["nombre", "artista", "año", "descripcion", "foto"]

#       VISTA BASADA EN CLASE PARA BORRAR UNA PINTURA

class borrarPinturas(LoginRequiredMixin, DeleteView):
    
    model= Pinturas
    success_url= "/verPinturas/"

