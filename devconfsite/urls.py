from django.urls import path, include

urlpatterns = [
    path('', include('devconf.urls')),
]
