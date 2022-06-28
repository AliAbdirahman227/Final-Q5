from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('order/', views.getNotes, name="order"),
    # path('order/create/', views.createNote, name="create-order1"),
    #path('order/<str:pk>/update/', views.updateNote, name="update-order1"),
    #path('order/<str:pk>/delete/', views.deleteNote, name="delete-order1"),

    path('order/<str:pk>/', views.getNote, name="order1"),
]
