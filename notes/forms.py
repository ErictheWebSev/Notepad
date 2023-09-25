from django import forms
from ckeditor.fields import CKEditorWidget
from .models import Note


class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title', 'content']
		
		widgets = {
			'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter A Task'}),
			'content': CKEditorWidget()
		}