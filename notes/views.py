from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Note
from .forms import NoteForm



def note_view(request):
  if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']
    
    note = Note.objects.create(title=title, content=content)
    
    response = {
      'success': True,
      'message': 'Note added Successfully',
      'noteId': note.id,
      'noteTitle': note.title,
      'noteContent': note.content,
      'noteCreated': note.created,
    }
    return JsonResponse(response)
  notes = Note.objects.all()
  
  context = {
    'notes': notes
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
		updated_title = request.POST['updated_title']
		updated_content = request.POST['updated_content']
		
		note.title = updated_title
		note.content = updated_content
		
		note.save()
		
		response = {
		  'success': True,
		  'message': 'Edited Successfully'
		}
		return JsonResponse(response)