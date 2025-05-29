from django.urls import path, include




urlpatterns = [
    path('users/', include('apps.users.urls')), 
    path('books/', include('apps.books.urls')),
    path('reviews/',include('apps.reviews.urls'))
]