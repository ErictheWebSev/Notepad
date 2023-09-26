from django import forms
from ckeditor.fields import CKEditorWidget
from .models import Note

input_class = 'bg-gray-700  h-10 w-80 text-lg px-4 py-3 text-gray-600'

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title', 'content']
		
		widgets = {
			'title': forms.TextInput(attrs={'class': input_class, 
			'placeholder': 'Enter A Task'}),
			'content': CKEditorWidget()
		}