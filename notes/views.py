from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Note
from .forms import NoteForm



def note_view(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			note = Note.objects.create(title=title, content=content)
			response = {
				'success': True,
				'message': 'Note added Successfully',
			}
			return JsonResponse(response)
	notes = Note.objects.all()
	form = NoteForm()
	
	context = {
		'notes': notes,
		'form': form,
	}
	return render(request, 'index.html', context)


def note_detail(request, note_id):
	note = get_object_or_404(Note, id=note_id)
	title = note.title
	content = note.content

	context = {
		'title': title,
		'content': content,
	}
	
	return JsonResponse(context)


def delete_note(request, note_id):
	note = get_object_or_404(Note, id=note_id)
	
	note.delete()
	response = {
		'success': True,
		'message': 'Deleted Successfully',
	}
	return JsonResponse(response)



def edit_note(request, note_id):
	note = get_object_or_404(Note, id=note_id)
	
	if request.method == 'POST':
		form_edit = NoteForm(request.POST, instance=note)
		
		if form_edit.is_valid():
			form_edit.save()
			
			return JsonResponse({'success': True, 'message': 'Edited Successfully'})
	else:
		form_edit = NoteForm(instance=note)
		context = {
			'form2': form_edit
		}
		
		return render(request, 'index.html')