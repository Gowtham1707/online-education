import imp
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from .models import *
from django.http import HttpResponse

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('onlineeducation:profile-list')
        return render(request, 'index.html')

method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        
        profiles = request.user.profiles.all()

        context = {
            'profiles':profiles
        }
        # change something
        return render(request, 'profilelist.html', context)

method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
            'form':form
        }
        return render(request, 'profilecreate.html', context)

    def post(self, request, *args, **kwargs):
        # form = ProfileForm(request.POST or None)
        # if form.is_valid():
        #     profile = Profile.objects.create(**form.cleaned_data)
        #     if profile:
        #         request.user.profiles.add(profile)
        #         return redirect('onlineeducation:profile-list')
        # context = {
        #     'form':form
        # }
        # return render(request, 'profilecreate.html', context)
        name = request.POST.get('name')
        age_limit = request.POST.get('age_limit')
        if name and age_limit:
            profile = Profile.objects.create(name=name, standard=age_limit)
            if profile:
                request.user.profiles.add(profile)
                return redirect('onlineeducation:profile-list')
        return render(request, 'profilecreate.html')
       

method_decorator(login_required, name='dispatch')
class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Topic.objects.filter(standard=profile.standard)
            if profile not in request.user.profiles.all():
                return redirect('onlineeducation:profile-list')

            context = {
            'movies':movies,
            'name':profile.name,
            'standard':profile.standard,
            # 
            'profile_id':profile_id,
            }

            return render(request, 'dashboard.html', context)
        except Profile.DoesNotExist:
            return redirect('onlineeducation:profile-list')

method_decorator(login_required, name='dispatch')
class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Topic.objects.get(uuid=movie_id)
            
            context = {
                'movie':movie
            }

            return render(request, 'video.html', context)
        except Topic.DoesNotExist:
            return redirect('onlineeducation:profile-list')

method_decorator(login_required, name='dispatch')
class MovieLanguage(View):
        
    def post(self, request,*args, **kwargs):
        
        language = request.POST.get('language')
        if language != "all":
            movies = Topic.objects.filter(language=language)

            context = {
                'movies':movies,
            }
            return render(request, 'video.html', context)
        return render(request, 'video.html')


method_decorator(login_required, name='dispatch')
class PlayMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Topic.objects.get(uuid=movie_id)
            movie = movie.video.values()
            
            context = {
                'movie':list(movie)
            }

            return render(request, 'playmovie.html', context)
        except Topic.DoesNotExist:
            return redirect('onlineeducation:profile-list')
    
def totalinternalreflection(request):
    return render(request,'quiztir.html')

def emf(request):
    return render(request,'quizemf.html')