from.import views
from django.urls import path

urlpatterns = [

    # path('',views.work,name='work'),
    path('',views.index,name='index')
]