"""res URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from register.views import register, login_view, forgot_password, reset_password , movie_details  , edit_review, vote_review, search_movies, profile, update_profile, login_success
from register import views
from django.conf import settings
from django.conf.urls.static import static
from register.views import rate_movie_popup, recommend, itemtoitem
from register.views import watchlist, add_to_watchlist, favlist, add_to_favlist

from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_dashboard.urls')),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/', reset_password, name='reset-password'),
    path('movies/', views.movies, name='movies'),
    path('profile/', views.profile, name='profile'),
    path('login_success/', views.login_success, name='login_success'),

    path('movie_details/<str:imdb_id>/', views.movie_details, name='movie_details'),
    path('rate_movie/<str:imdb_id>/', views.rate_movie, name='rate_movie'),
    path('rate_movie_popup/<str:imdb_id>/', rate_movie_popup, name='rate_movie_popup'),
    path('watchlist/', watchlist, name='watchlist'),
    path('add-to-watchlist/<str:movie_title>/', add_to_watchlist , name='add_to_watchlist'),
    path('favlist/', favlist, name='favlist'),
    path('add-to-favlist/<str:movie_title>/', add_to_favlist, name='add_to_favlist'),
    path('add_review/', views.movie_details, name='add_review'),
    path('edit_review/<str:imdb_id>/', views.edit_review, name='edit_review'),
    path('vote_review/<str:imdb_id>/', views.vote_review, name='vote_review'),
    path('search_movies/', views.search_movies, name='search_movies'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('genre/<str:genre>/', views.genre_categorize, name='genre_categorize'),

    path('delete_review/<str:imdb_id>/', views.delete_review, name='delete_review'),

    path('recommend/<str:imdb_id>/', views.recommend, name='recommend'),
    path('itemtoitem/', views.itemtoitem, name='itemtoitem'),


    path('top10/', views.top_10_movies, name='top_10_movies'),






    

    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
