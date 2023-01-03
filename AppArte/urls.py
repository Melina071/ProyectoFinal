from django.urls import path
from AppArte.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
                
                #  Inicio e índice de navegación
                
                path('', inicio, name='Inicio'),
                path('discos/', discos, name='discos'),
                path('libros/', libros, name='libros'),
                path('pinturas/', pinturas, name='pinturas'),
                
                #  CRUD de discos:
                
                path('discos/añadir', formularioDiscos, name='formdedisco'),
                path('verDiscos/', listaDiscos.as_view(), name="listadiscos"),
                path('detalleDiscos/<int:pk>', detalleDiscos.as_view(), name= 'detallediscos'),
                path('actualizarDiscos/<int:pk>', actualizarDiscos.as_view(), name= 'actualizardiscos'),
                path('borrarDiscos/<int:pk>', borrarDiscos.as_view(), name= 'borrardiscos'),
                
                #  CRUD de libros:
                
                path('libros/añadir', formularioLibros, name='formdelibro'),
                path('verLibros/', listaLibros.as_view() , name="listalibros"),
                path('detalleLibros/<int:pk>', detalleLibros.as_view(), name= 'detallelibros'),
                path('actualizarLibros/<int:pk>', actualizarLibros.as_view(), name= 'actualizarlibros'),
                path('borrarLibros/<int:pk>', borrarLibros.as_view(), name= 'borrarlibros'),
                
                #  CRUD de pinturas:
                
                path('pinturas/añadir', formularioPinturas, name='formdepinturas'),
                path('verPinturas/', listaPinturas.as_view() , name="listapinturas"),
                path('detallePinturas/<int:pk>', detallePinturas.as_view(), name= 'detallepinturas'),
                path('actualizarPinturas/<int:pk>', actualizarPinturas.as_view(), name= 'actualizarpinturas'),
                path('borrarPinturas/<int:pk>', borrarPinturas.as_view(), name= 'borrarpinturas'),
                
                #   Búsqueda y resultados de libros, discos, pinturas
                
                path('busquedaDiscos', busquedaDiscos, name='busquedadiscos'),
                path('resultadosDiscos/', resultadosDiscos, name= 'resultadosdiscos'),
                path('busquedaLibros', busquedaLibros, name='busquedalibros'),
                path('resultadosLibros', resultadosLibros, name= 'resultadoslibros'),
                path('busquedaPinturas', busquedaPinturas, name='busquedapinturas'),
                path('resultadosPinturas', resultadosPinturas, name= 'resultadospinturas'),
                
                #   Crear user, editar user, login, logout 
                
                path('registro', registrar, name= "register"),
                path('iniciosesion', iniciarSesion, name= "login"),
                path("cerrarsesion", LogoutView.as_view(template_name="AppArte/logout.html"), name= "logout"),
                path('editarUsuario', editarUsuario, name= "editaruser"),
                path('agregarAvatar', agregarAvatar, name= "avatar"),

]
