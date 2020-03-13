from django.conf.urls import url
from django.contrib.auth.views import *

from filmistan.views import FilmList, Filmcek, paginat
from . import views

urlpatterns = [
    url(r'^profile/$', views.Profile),
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
        PasswordResetView.as_view(), {'redirect': 'accounts/password/reset/done/'},
        name='password_reset'),

    url(r'^accounts/password/reset/done/$',
        PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(), {'post_reset_redirect': '/accounts/password/done/'},
        name='password_reset_confirm'),

    url(r'^accounts/password/done/$',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
