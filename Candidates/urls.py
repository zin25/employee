from django.contrib import admin
from django.urls import path, include
from App import views
from Candidates import settings
from django.conf.urls.static import static

# Admin Panel
admin.site.site_header = "HR Admin"
admin.site.index_title = "Table Candidates"

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    #Frontend
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', include('django.contrib.auth.urls')),
    # Backend
    path('backend', views.backend, name='backend'),
    path('<int:id>/', views.candidate, name='candidate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
