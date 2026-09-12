from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    RegistroView, DashboardView,
    ProyectoListView, ProyectoCreateView, ProyectoUpdateView, ProyectoDeleteView,
    TareaListView, TareaCreateView, TareaUpdateView, TareaDeleteView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('proyectos/', ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/nuevo/', ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', ProyectoDeleteView.as_view(), name='proyecto_delete'),

    path('proyectos/<int:proyecto_id>/tareas/', TareaListView.as_view(), name='tarea_list'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', TareaCreateView.as_view(), name='tarea_create'),
    path('tareas/<int:pk>/editar/', TareaUpdateView.as_view(), name='tarea_update'),
    path('tareas/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='tarea_delete'),
]