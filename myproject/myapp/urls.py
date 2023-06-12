from django.urls import path 
from . import views
from .views import login_view
from .views import *

urlpatterns = [
    path('',views.home_principle, name='home_general'),
    path('home/',views.home, name='home'),
    #path('upload/<int:id>',views.upload_document, name='upload_docs'),
    path('homeAdmin/',views.Adminhome, name='success'),
    path('homeAdmin/Add/<int:pk>/', views.addCommission, name='add'),
    path('homeAdmin/Vu/<str:pk>/', views.voirCommission, name='voir'),
    path('login/', login_view, name='login'),
    path('AllFaculté/', views.allFaculté, name='faculté'),
    path('AjoutéFaculté/', views.uploadFaculté, name='addfaculté'),
    path('AllCretiers/', views.allCri, name='critiers'),
    path('Ajoutécritérs/', views.uploadcritérs, name='addcritiers'),
    path('AllFaculté/update/<int:pk>/', FacultéUpdateView.as_view(), name='updatefaculté'),
    path('AllFaculté/delete/<int:pk>/', views.delete, name='deletefaculté'),
    path('AllCretiers/update/<int:pk>/', CritéresUpdateView.as_view(), name='updatecreters'),
    path('AllCretiers/delete/<int:pk>/', views.deleteCre, name='deletecreters'),
   # path('upload-docs/', upload_docs, name='upload_docs'),
    path('add-docs/<int:id>', upload_doc, name='upload_docs'),
    path('logout/', logout_view, name='logout'),
    path('home-admin/', Homeadmin, name='homeadd'),
    path('show_details/<str:name>/', show_details, name='show_details'),




]


