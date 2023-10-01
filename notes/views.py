from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteForm


@login_required(login_url='login')
def note_view(request):
  notes = Note.objects.filter(user=request.user)
  
  context = {
    'notes': notes
  }
  
  return render(request, 'index.html', context)

 
@login_required(login_url='login')
def add_note(request):
  if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']
    
    note = Note.objects.create(title=title, content=content, user=request.user)
    
    response = {
      'success': True,
      'message': 'Note added Successfully',
      'noteId': note.id,
      'noteTitle': note.title,
      'noteContent': note.content,
      'noteCreated': note.created,
    }
    return JsonResponse(response)	


@login_required(login_url='login')
def note_detail(request, note_id):
	note = get_object_or_404(Note, id=note_id, user=request.user)
	title = note.title
	content = note.content

	context = {
		'title': title,
		'content': content,
	}
	
	return JsonResponse(context)


@login_required(login_url='login')
def delete_note(request, note_id):
	note = get_object_or_404(Note, id=note_id, user=request.user)
	
	note.delete()
	response = {
		'success': True,
		'message': 'Deleted Successfully',
	}
	return JsonResponse(response)


@login_required(login_url='login')
def edit_note(request, note_id):
	note = get_object_or_404(Note, id=note_id, user=request.user)
	
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


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		if User.objects.filter(username=username).exists():
			response = {
			  'success': False,
			  'mesaage': 'User Already Eaxists...'
			}
			return JsonResponse(response)
		else:
			user = User.objects.create_user(username=username, password=password)
			user.save()
			login(request, user)
			response = {
			  'success': True,
			  'message': 'Registration Successful'
			}
			return JsonResponse(response)
	return render(request, 'register.html')



def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			response = {
			  'success': True,
			  'message': f'welcome {username}!'
			}
			
			return JsonResponse(response)
		else:
			response = {
				'success': False,
				'message': 'Invalid Login...'
			}
			return JsonResponse(response)
	return render(request, 'login.html')


def logout_user(request):
  logout(request)
  return redirect('note-view')