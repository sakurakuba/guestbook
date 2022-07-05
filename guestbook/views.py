from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from guestbook.forms import BookForm
from guestbook.models import Book


def index_view(request):
    notes = Book.objects.order_by('-created_at').filter(status='active')
    context = {'notes': notes}
    return render(request, 'index.html', context)

def add_note(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'add_note.html', {'form': form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            new_note = Book.objects.create(author=author, email=email, content=content)
            return redirect('index')
        return render(request, 'add_note.html', {'form': form})


def update_note(request, pk):
    note = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={
            "author": note.author,
            "email": note.email,
            "content": note.content
        })
        return render(request, 'update.html', {"form": form, "note": note})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            note.author = form.cleaned_data.get('author')
            note.email = form.cleaned_data.get('email')
            note.content = form.cleaned_data.get('content')
            note.save()
            return redirect('index')
        return render(request, 'update.html', {"form": form, "note": note})


def delete_note(request, pk):
    note = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'note': note})
    else:
        note.delete()
        return redirect('index')
