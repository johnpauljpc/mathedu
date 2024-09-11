from django.urls import path 
from . import views

urlpatterns = [
    path('', view=views.index_view, name="index"),
    path('simple-interest/', views.simple_interest_view, name="simple_interest"),
    path('compound-interest/', views.compound_interest_view, name="compound_interest"),
    path('quadratic/', views.quadratic_view, name="quadratic"),
    path('dda/', view=views.dda_line_generation, name="dda")
]