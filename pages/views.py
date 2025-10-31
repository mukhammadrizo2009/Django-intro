from django.http import HttpResponse

def home_view(x):
    return HttpResponse('<h1> Home </h1>')

def about_view(x):
    return HttpResponse('<h1> About </h1>')

def contact_view(x):
    return HttpResponse('<h1> +992 97 652 2727 </h1>')

def login_view(x):
    return HttpResponse('<h1> Hello World </h1>')

def register_view(x):
    return HttpResponse('<h1> Have a good day...! </h1>')

def profile_view(x):
    return HttpResponse("<h1> I don't have any profile!")