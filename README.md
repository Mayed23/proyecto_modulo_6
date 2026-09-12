# proyecto_modulo_6
django_web_app
Aplicación web desarrollada con Django, que permite a los usuarios registrarse
autenticarse y gestionar proyectos y tareas de forma segura y dinámica.

## CARACTERISITCAS

- Registro y autenticación de usuarios (django.contrib.auth)
- Crear, Listar, Editar y Eliminar
- Asociar Tareas a proyectos y usuarios
- Los usuarios pueden ver modificar sus proyectos y tareas
- Panel de Administración
- CSS con Bootstrap
- Validacion de datos (fecha de limiti no puede ser menor a la fecha del registro)

## REQUISITOS PREVIOS

- Python
- pip djnago
- entorno virtual

## Estructura del Proyecto

django_web_app/
├── manage.py
├── django_web_app/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                    # App principal
    ├── models.py            # Modelos Proyecto y Tarea
    ├── forms.py             # ProyectoForm, TareaForm, RegistroForm
    ├── views.py             # Vistas basadas en clase 
    ├── urls.py              # Rutas de la app
    ├── admin.py             # Configuración del panel admin
    ├── static/core/css/     # Estilos personalizados
    └── templates/core/      # Plantillas HTML (con herencia de base.html)


## Crea y activa un entorno virtual:
    
   python3 -m venv venv
   source venv/bin/activate      # Linux 

## Instala las dependencias:

  python manage.py migrate

## Inicia el servidor de desarrollo:

     http://127.0.0.1:8000/  

## Uso

# Ruta	                        #Descripción

/registro/	                  Crear una cuenta nueva
/login/	                      Iniciar sesión
/logout/	                    Cerrar sesión
/	Dashboard                   con resumen de proyectos
/proyectos/	                  Listado de proyectos del usuario
/proyectos/nuevo/	            Crear un nuevo proyecto
/proyectos/<id>/editar/	      Editar un proyecto
/proyectos/<id>/eliminar/	    Eliminar un proyecto
/proyectos/<id>/tareas/	      Listado de tareas de un proyecto
/proyectos/<id>/tareas/nueva/	Crear una nueva tarea
/tareas/<id>/editar/	        Editar una tarea
/tareas/<id>/eliminar/	      Eliminar una tarea
/admin/	                      Panel de administración de Django

## Credenciales de prueba

Para revisar el panel de administración sin crear un usuario nuevo, puede usar el siguiente superusuario de prueba:

          Usuario: admin
          Contraseña: 123456

Acceda desde http://127.0.0.1:8000/admin/.




