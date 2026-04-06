"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from movies import views
from movies import api

from rest_framework.urlpatterns import format_suffix_patterns # allow us to .json in browser to see json formatted responses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    # Render
    path('movies/', views.movies),
    path('movies/add', views.add),
    path('movies/<int:id>', views.detail),
    path('movies/edit/<int:id>', views.edit),
    path('movies/delete/<int:id>', views.delete),
    path('movies/<int:movie_id>/reviews/add', views.add_review),    # form to add a review
    path('movies/<int:movie_id>/reviews/delete/<int:review_id>', views.delete_review),
    
    # Pure CRUD rest_framework
    path('api/movies/', api.movies_list),
    path('api/movies/<int:movie_id>', api.movie_detail),
    # path('api/movies/<int:movie_id>/reviews/', api.review_list),
    # path('api/movies/<int:movie_id>/reviews/<int:review_id>', api.review_detail)
    
]

urlpatterns = format_suffix_patterns(urlpatterns) # allow us to .json in browser to see json formatted responses
