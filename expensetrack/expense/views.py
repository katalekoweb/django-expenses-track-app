from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'expense/index.html')

def form (request):
    return render(request, 'expense/form.html')