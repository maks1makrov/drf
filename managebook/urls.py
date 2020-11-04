from django.urls import path

from managebook import views

urlpatterns = [
    path('list/<int:id>', views.ListBook.as_view(), name="detail"),
    path('list/', views.ListBook.as_view(), name="list"),
    path('create/', views.CreateBook.as_view(), name="create"),
    path('destroy/<int:id>', views.DestroyBook.as_view(), name="delete"),
    path('update/<int:id>', views.UpdateBook.as_view(), name="update"),
    path('list_comment', views.ListComment.as_view(), name="list-comment"),
]