
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler500

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include("secondary_math.urls")),
    path("", include("university_math.urls")),

]


# Custom 404 handler
handler404 = 'university_math.views.custom_404_view'
handler500 = 'university_math.views.custom_500_view'