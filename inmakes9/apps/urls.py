from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

app_name='apps'

urlpatterns = [
    path('',views.index,name='index'),
    path('Movies/<int:movie_id>',views.details,name='details'),
    path('add/',views.adding,name='adding'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]

