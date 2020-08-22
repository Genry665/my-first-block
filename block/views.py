from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'block/post_list.html', {})
