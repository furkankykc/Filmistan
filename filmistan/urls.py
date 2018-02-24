from django.conf.urls import url

from . import views
from .views import FilmList, Filmcek,paginat
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^profile/$',views.Profile),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'index/$', views.Index),
    url(r'^$', views.rdrindx),
    url(r'^info/$', views.info),
    url(r'^register/$', views.kayit),
    url(r'^film/$', views.filmler),
    url(r'^fragmanlar/$', views.fragmanlar),
    url(r'^film/([\w-]+)/$', Filmcek.as_view()),
    url(r'^page/([\w-]+)/$', paginat.as_view()),
    url(r'^index/([\w-]+)/$', FilmList.as_view()),
    url(r'^accounts/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': '/accounts/password/reset/done/'},
        name='password_reset'),

    url(r'^accounts/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),

    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/accounts/password/done/'},
        name='password_reset_confirm'),

    url(r'^accounts/password/done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
]