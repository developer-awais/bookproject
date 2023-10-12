from django.urls import path
from .views import CreateBook, GetBooks, DeleteBook, UpdateBook, GetBookByID

urlpatterns = [
    path('books/', GetBooks.as_view(), name='get-books'),
    path('books/create/', CreateBook.as_view(), name='create-book'),
    path('books/<int:book_id>/', GetBookByID.as_view(), name='get-book-by-id'),
    path('books/<int:book_id>/delete/', DeleteBook.as_view(), name='delete-book'),
    path('books/<int:book_id>/update/', UpdateBook.as_view(), name='update-book'),
]