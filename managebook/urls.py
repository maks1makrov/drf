from django.urls import path

from managebook import views

urlpatterns = [
    path('list/<int:id>', views.ListBook.as_view()),
    path('list/', views.ListBook.as_view()),
    path('create/', views.CreateBook.as_view()),
    path('destroy/<int:id>', views.DestroyBook.as_view()),
]