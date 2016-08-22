import session_csrf

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


session_csrf.monkeypatch()


urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Auth0
    url(r'^auth/', include('django_auth0.urls')),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # Main landing page
    url(r'^', include('moderator.moderate.moderate_urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
