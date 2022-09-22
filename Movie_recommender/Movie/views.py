import pickle
import gzip
import numpy as np
from django.shortcuts import render
from .models import Movies
from .forms import Moviesform

# Create your views here.

def index(request):
    movies = Moviesform()
    context = {'movie':movies}
    return render(request,'Movie/index.html',context)


def output(request):
    with gzip.open('cosine_sim.pklz', 'rb') as file:
        cosine_sim = pickle.load(file)
    if request.method=='POST':
        title = request.POST['movieslist']
        index = list(Movies.objects.filter(Movie_Title=title).values_list('movie_id',flat=True))
        for no in index:
            results=list(enumerate(cosine_sim[no]))
            sorted_result = sorted(results,key=lambda x: x[1],reverse=True)
            sorted_result = sorted_result[1:11]
            no = [n[0] for n in sorted_result]
            sim_movies = [Movies.objects.get(movie_id=l) for l in no]
            context = {'movies':sim_movies}
            return render(request, 'Movie/output.html',context)

