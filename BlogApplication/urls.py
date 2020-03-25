"""BlogApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from userStuff import views as user_views
from django.contrib.auth import views as auth_views
from blog import views as blog_view

# for handling media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',blog_view.home, name='home'),
    path('add-post/',blog_view.add_post, name='add_post'),
    path('search/',blog_view.search_users, name='search'),
    path('detail/<int:id>/',blog_view.show_details, name='detail'),
    path('edit/<int:id>/',blog_view.make_public, name='edit'),
    path('delete/<int:id>/',blog_view.delete_post, name='delete'),
    path('delete_comment/<int:comment_id>/<int:post_id>/', blog_view.delete_comment, name='delete_comment'),
    path('login/',user_views.login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('',user_views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)