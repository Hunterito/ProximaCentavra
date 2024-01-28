"""
URL configuration for ProximaCentavra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from The_Endless_Universe.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("The_Endless_Universe.urls")),
    # Маршрут главной страницы, чтобы не было ошибки 404
    # Первый аргумент будет добавляться в URL адреса представлений из файла The_Endless_Universe.urls.py
    # Вызов include, передавая в качестве аргументов все маршруты представлений
    # path('stars/', views.categories)  # Первый аргумент - суффикс URL, вторым аргументом - представление
]

# handler для несуществующей страницы
handler404 = page_not_found