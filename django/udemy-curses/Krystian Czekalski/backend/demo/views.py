from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):

    book = Book.objects.filter(id=2)
    output = f"we have {book.title} book with Id {book.id} <br>"

    # for book in books:
    #     output += f"we have {book.title} book with Id {book.id} <br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First message from views')
