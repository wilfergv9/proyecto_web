from django.urls import path
from . import views

URLPATTERNS = [
    path('', views.lista_objetos, name='lista_objetos'),
    path('<int:pk>/', views.detalle_objeto, name='detalle_objeto'),
    path('nuevo/', views.crear_objeto, name='crear_objeto'),
    path('<int:pk>/editar/', views.editar_objeto, name='editar_objeto'),
    path('<int:pk>/eliminar/', views.eliminar_objeto, name='eliminar_objeto'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]