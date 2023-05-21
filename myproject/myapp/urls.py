from django.urls import path 
from . import views
from .views import login_view

urlpatterns = [
    path('',views.home, name='home'),
    path('upload/<int:id>',views.upload_document, name='upload_docs'),
    path('homeAdmin/',views.Adminhome, name='success'),
    path('login/', login_view, name='login'),
    path('AllFaculté/', views.allFaculté, name='faculté'),
    path('AllCretiers/', views.allCri, name='critiers'),
]