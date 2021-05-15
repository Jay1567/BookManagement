from django.urls import path
from .views import BookView

urlpatterns = [
    path('getBooks/', BookView.as_view()),
]