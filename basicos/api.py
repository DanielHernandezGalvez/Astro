# Crear el entorno virtual
virtualenv venv
# Activar el ambiente virtual
source venv/bin/activate

# pip install django djangorestframework djangorestframework-simplejwt 
# django-model-utils

Django==3.0.8
djangorestframework==3.11.0
djangorestframework-simplejwt==4.4.0
django-model-utils==4.0.0

# pip install -r requirements.txt
# django-admin startproject project .

python manage.py runserver
python manage.py startapp api

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    **'api'**
]
4. Crear un modelo en la base de datos
Para crear un modelo vamos al archivo models.py, en este archivo crearemos el modelo que representará una tabla o varias tablas de la base de datos, para este ejemplo crearemos un modelo llamado post, aquí debemos anotar algo y es que usamos las clases TimeStampedModel y SoftDeletableModel estas nos permiten crear los campos de created y updated, e is_removed respectivamente, estas clases no vienen incluidas en Django por lo tanto debemos hacer la instalación de la librería django-model-utils para usarlas dentro de nuestro proyecto

from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
class Post(TimeStampedModel, SoftDeletableModel):
	title 				= models.CharField(max_length=50, null=False, blank=True)
	body 				= models.TextField(max_length=5000, null=False, blank=True)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 				= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.title
Cuando empecemos a manejar modelos o interacciones con la base de datos debemos crear un superusuario para acceder al admin de Django, esta tarea es sencilla, en la consola podemos ejecutar el siguiente comando:

python manage.py createsuperuser
Los siguientes pasos que realizaremos tienen que ver con la creación de las migraciones de nuestro proyecto, esto nos permitirá crear la tabla en nuestra base de datos y tener un control de cambios sobre ella, para realizar este proceso vamos a ejecutar los siguientes comandos:

# Crear una migración
python manage.py makemigrations
# Correr todas las migraciones
python manage.py migrate
Una de las grandes ventajas con las que viene Django es el dashboard-admin que nos permite interactuar con nuestros datos de manera sencilla, para poder registrar nuestros modelos en este dashboard debemos ir al archivo admin.py e incluir la siguiente linea de código

from django.contrib import admin
from .models import Post
admin.site.register(Post)
5. Instalación y configuración de Django REST Framework
Para instalar el Djago Rest Framework podemos ejecutar el siguiente comando en la consola, esto debemos hacerlo si no ejecutamos los primeros pasos de instalación, si no podemos omitir este paso

pip install djangorestframework
Después de instalar el framework debemos realizar la siguiente configuración, en el archivo settings.py vamos a agregar la aplicación rest_framework en la sección INSTALLED_APPS

INSTALLED_APPS = [
    ...
    'rest_framework',
]
Si tienes alguna duda del proceso de instalación puedes consultar la documentación oficial: https://www.django-rest-framework.org/

6. Serializar el modelo (serializers.py)
El siguiente paso es la creación de un serializador para nuestro modelo de post. Los serializadores permiten que datos complejos, como conjuntos de consultas e instancias de modelos, se conviertan en tipos de datos nativos de Python que luego se pueden representar fácilmente en JSON, XML u otros tipos de contenido. (Para más información sobre serializadores puedes consultar: https://www.django-rest-framework.org/api-guide/serializers/

from rest_framework import serializers
from api.models import Post
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']
7. Crear la vista (views.py)
En la vista crearemos los métodos necesarios para responder a las peticiones HTTP mediante dos URLs que crearemos en el siguiente paso, el primer método responderá a la petición GET que traera el listado de nuestros post y el método POST que permitirá guardar registros en la base de datos. La siguiente URL nos permitira hacer métodos referentes a un solo post de nuestro blog, métodos para consultar un solo post, editar o eliminar un post con un id determinado o una primary key

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializers
from .models import Post
from rest_framework import status
from django.http import Http404
    
class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
8. Crear las URLs
Finalmente crearemos dos URLs para consultar nuestros métodos, recordemos que podemos hacer la inlcusión de dos maneras una definiendolas en el archivo general de URLs o lo que hacemos aquí es crear un archivo url.py dentro de nuestrea app y luego usarlo desde nuestro archivo de url general.

from django.urls import path
from .views import *
app_name = 'api'
urlpatterns = [
    path('v1/post', Post_APIView.as_view()), 
    path('v1/post/<int:pk>/', Post_APIView_Detail.as_view()),
    
]
Si quieres mirar el proyecto completo no olvides visitar el repositorio

davidcasr/blog-api
A blog API in Django & Django Rest Framework. Contribute to davidcasr/blog-api development by creating an account on…
github.com

Django
API
Django Rest Framework

from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
class Post(TimeStampedModel, SoftDeletableModel):
	title 				= models.CharField(max_length=50, null=False, blank=True)
	body 				= models.TextField(max_length=5000, null=False, blank=True)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 				= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.title
    
    #python manage.py createsuperuser
# Crear una migración
python manage.py makemigrations
# Correr todas las migraciones
python manage.py migrate

from django.contrib import admin
from .models import Post
admin.site.register(Post)

# pip install djangorestframework

INSTALLED_APPS = [
    ...
    'rest_framework',
]

from rest_framework import serializers
from api.models import Post
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializers
from .models import Post
from rest_framework import status
from django.http import Http404
    
class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.urls import path
from .views import *
app_name = 'api'
urlpatterns = [
    path('v1/post', Post_APIView.as_view()), 
    path('v1/post/<int:pk>/', Post_APIView_Detail.as_view()),
    
]


