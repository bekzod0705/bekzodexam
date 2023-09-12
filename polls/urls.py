from django.urls import path
from .views import getAllAuthors,getAllBooks,createAuthor,createBook,changeAuthor,changeBook,deleteAuthor,deleteBook,getAllAuthorbooks
urlpatterns=[
    path('getallauthors/',getAllAuthors.as_view()),
    path('getallbooks/',getAllBooks.as_view()),
    path('createauthor/',createAuthor.as_view()),
    path('createbook/',createBook.as_view()),
    path('changeauthor/<int:forid>/',changeAuthor.as_view()),
    path('changebook/<int:forid>/',changeBook.as_view()),
    path('deleteauthor/<int:forid>/',deleteAuthor.as_view()),
    path('deletebook/<int:forid>/',deleteBook.as_view()),
    path('getallauthorbooks/<int:forid>/',getAllAuthorbooks.as_view())

]