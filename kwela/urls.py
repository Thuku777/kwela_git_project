from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from contact.views import Contact
from malipo.views import Malipo



urlpatterns = [
    path('', include('pages.urls')),
    path('blog/',  include('blog.urls')),
    path('catalog/',  include('catalog.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', Contact, name="contact"),
    path('contact/', include('contact.urls')),
    path('malipo/', include('malipo.urls')),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile' ),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
