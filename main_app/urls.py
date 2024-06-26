from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path for finches index (see all of them)
    path('finches/', views.finches_index, name='index'),
    #path for detailed view
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('shiny_objects/', views.ShinyObjectList.as_view(), name='shiny_objects_index'),
    path('shiny_objects/<int:pk>/', views.ShinyObjectDetail.as_view(), name='shiny_objects_detail'),
     path('shiny_objects/create/', views.ShinyObjectCreate.as_view(), name='shiny_objects_create'),
    path('shiny_objects/<int:pk>/update/', views.ShinyObjectUpdate.as_view(), name='shiny_objects_update'),
    path('shiny_objects/<int:pk>/delete/', views.ShinyObjectDelete.as_view(), name='shiny_objects_delete'),
]