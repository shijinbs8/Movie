from django.shortcuts import render, redirect
from .models import Movies
from .forms import Moviefrom
# Create your views here.
def index(request):
    movies=Movies.objects.all()
    context={'movie_list':movies}
    return render(request,'index.html',context)
def details(request,movie_id):
    movies=Movies.objects.get(id=movie_id)
    return render(request,'details.html',{'id':movies})
def adding(request):
    if request.method=='POST':
        name=request.POST.get('name')
        disc=request.POST.get('disc')
        year=request.POST.get('year')
        img=request.FILES['img']

        movies=Movies(name=name,disc=disc,year=year,img=img)
        movies.save()

    return render(request,'adding.html')
def update(request,id):
    movies=Movies.objects.get(id=id)
    forms=Moviefrom(request.POST or None,request.FILES,instance=movies)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':forms,'movies':movies})
def delete(request,id):
    if request.method=='POST':
        movies = Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')
