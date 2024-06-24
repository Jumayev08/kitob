# library_project/library_app/views.py
from django.shortcuts import render
from .forms import BookForm

def book_select_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            selected_book = form.cleaned_data['book']
            return render(request, 'book_detail.html', {'book': selected_book})
    else:
        form = BookForm()
    
    return render(request, 'book_select.html', {'form': form})
