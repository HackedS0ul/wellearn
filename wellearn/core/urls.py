from django.urls import path

from .views import home, courses

urlpatterns =[
    path('', home, name='home'),
    path('kursai/', courses, name='courses'),
]