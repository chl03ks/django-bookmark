from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'djangomarcador.views.bookmark_user',
        name='djangomarcador_bookmark_user'),
    url(r'^$', 'djangomarcador.views.bookmark_list', name='djangomarcador_bookmark_list'),
]
