from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Admin site
    path('', include('members.urls')), # URLs for the members app
    path('azure/', include('hello_azure.urls')),         # Root URL redirects to the members app

]
