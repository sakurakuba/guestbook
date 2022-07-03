from django.shortcuts import render

# Create your views here.
from guestbook.models import Book


def index_view(request):
    notes = Book.objects.order_by('-created_at').filter(status='active')
    context = {'notes': notes}
    return render(request, 'index.html', context)
