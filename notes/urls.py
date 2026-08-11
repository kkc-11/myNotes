from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
]