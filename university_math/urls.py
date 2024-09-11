from . import views
from django.contrib import admin
from django.urls import path
# from django.conf.urls import handler403, handler404

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("trans-eqn/", views.find_roots, name="trans_eqn"),
    
]