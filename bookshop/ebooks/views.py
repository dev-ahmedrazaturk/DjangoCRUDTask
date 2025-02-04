from django.shortcuts import render, redirect, get_object_or_404
from .models import MyBook
from .forms import MyBookForm

# Read (List Books)
def book_list(request):
    books = MyBook.objects.all()
    return render(request, 'index.html', {'books': books})

# Create a new Book
def add_book(request):
    if request.method == 'POST':
        form = MyBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after saving
    else:
        form = MyBookForm()
    return render(request, 'add_book.html', {'form': form})

# Update a Book
def edit_book(request, book_id):
    book = get_object_or_404(MyBook, id=book_id)
    if request.method == 'POST':
        form = MyBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = MyBookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# Delete a Book
def delete_book(request, book_id):
    book = get_object_or_404(MyBook, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})
