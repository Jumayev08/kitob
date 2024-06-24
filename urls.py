# library_project/library_app/urls.py
from django.urls import path
from .views import book_select_view

urlpatterns = [
    path('select-book/', book_select_view, name='select-book'),
]
