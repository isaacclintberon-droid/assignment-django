from django.shortcuts import render
from .models import Book, Category

def library_home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, "library/home.html", {"books": books, "categories": categories})
