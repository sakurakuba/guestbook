from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from guestbook.models import Book, STATUS_CHOICES


def index_view(request):
    notes = Book.objects.order_by('-created_at').filter(status='active')
    context = {'notes': notes}
    return render(request, 'index.html', context)

def add_note(request):
    if request.method == 'GET':
        return render(request, 'add_note.html')
    else:
        author = request.POST.get('author')
        email = request.POST.get('email')
        content = request.POST.get('content')
        new_note = Book.objects.create(author=author, email=email, content=content)
        context = {'notes': new_note}
        return redirect('index')


def update_note(request, pk):
    note = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', {'note': note})
    else:
        note.author = request.POST.get('author')
        note.email = request.POST.get('email')
        note.content = request.POST.get('content')
        note.save()
        return redirect('index')


def delete_note(request, pk):
    #pk = kwargs.get("pk")
    note = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'note': note})
    else:
        note.delete()
        return redirect('index')
