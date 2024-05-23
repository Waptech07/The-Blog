from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path("register/", views.register, name="register"),
        path("login/", views.login, name="login"),
        path("logout/", views.logout, name="logout"),
        path("add_post/", views.add_post, name="add_post"),
        path("<int:id>/<slug>/", views.read, name="read"),
        path("profile/", views.view_profile, name="view_profile"),
        path("about/", views.about, name="about"),
        path("projects/", views.projects, name="projects"),
        path("newsletter/", views.newsletter, name="newsletter"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
