from django.urls import path


from . import views

app_name = 'apk'
urlpatterns = [
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
]