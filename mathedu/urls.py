from django.urls import path, include

urlpatterns = [
    path('', include("secondary_math.urls")),
    path("", include("university_math.urls")),
]


# Custom error handlers
handler404 = 'university_math.views.custom_404_view'
handler500 = 'university_math.views.custom_500_view'