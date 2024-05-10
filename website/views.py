from django.shortcuts import render
from django.http import HttpResponse
from .mongo import get_mongo_collection

# Create your views here.

def my_first_view(request):
    collection = get_mongo_collection()
    data = list(collection.find({}))

    return render(request, 'index.html', {'data': data})