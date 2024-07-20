from django.contrib import admin#???
from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentAPI.as_view()),
    path('books/', get_books),
    path('register/', RegisterUser.as_view()),
    # path('', home),
    # path('student',post_student),
    # path('update/<id>', update_student),
    # path('delete/', delete_student),
]

