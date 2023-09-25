from django.urls import path
from . import views


urlpatterns = [
	path('', views.note_view, name='note-view'),
	path('detail/<int:note_id>/', views.note_detail, name='note-detail'),
	path('delete/<int:note_id>/', views.delete_note, name='delete-note'),
	path('edit/<int:note_id>/', views.edit_note, name='edit-note'),
	
]