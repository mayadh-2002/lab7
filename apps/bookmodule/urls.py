import apps.bookmodule.views
from django.urls import path
from . import views
from .views import add_book, simple_query
from .views import  add_test_book , complex_query
"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import add_book
from .views import simple_query
urlpatterns = [
    path('', views.index, name="books.index"),  
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
   path('html5/links', views.links, name='book.links'),
   path('search/', views.search_books, name='search_books'),
   path('html5/text/formatting', views.text_formatting, name='text_formatting'),
path('html5/listing', views.listing, name='listing'),
path('html5/tables', views.tables, name='tables'),
path('add/', add_book),
path('simple/query', simple_query),
path('add/test/', add_test_book),
 path('complex/query', complex_query),
]
