from django.shortcuts import render, HttpResponse

def index(request):
    print "*" * 100
    print "Hello World"
    print "*" * 100

    return render(request, "hello_world/index.html")
def show(request):
    return render(request, "hello_world/show_users.html")

def third(request):
    return render(request, "hello_world/third.html")
