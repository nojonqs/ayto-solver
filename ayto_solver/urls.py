"""ayto_solver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import RedirectView

import frontend.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name="person_overview"), name="home"),
    path("person/", frontend.views.PersonOverview.as_view(), name="person_overview"),
    path(
        "person/create_male/",
        frontend.views.MaleCreateView.as_view(),
        name="male_create",
    ),
    path(
        "person/create_female/",
        frontend.views.FemaleCreateView.as_view(),
        name="female_create",
    ),
    path(
        "person/<int:pk>/delete/",
        frontend.views.PersonDeleteView.as_view(),
        name="person_delete",
    ),
    path("solve/", frontend.views.solve_matches, name="solve_matches"),
    path(
        "match/no_match/create/",
        frontend.views.NoMatchCreateView.as_view(),
        name="no_match_create",
    ),
    path(
        "match/perfect_match/create/",
        frontend.views.PerfectMatchCreateView.as_view(),
        name="perfect_match_create",
    ),
    path(
        "match/overview/", frontend.views.MatchOverview.as_view(), name="match_overview"
    ),
    path(
        "match/<int:pk>/delete/",
        frontend.views.MatchDeleteView.as_view(),
        name="match_delete",
    ),
    path(
        "reset/",
        frontend.views.reset,
        name="reset"
    )
]
