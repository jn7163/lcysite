from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),

    url(r'^passages/(?P<passage_page>[0-9]+)',views.passages,name='passages'),
    url(r'^passage/(?P<passage_id>[0-9]+)',views.passage,name='passage'),

    url(r'^author/',views.author,name='author'),

    url(r'^newpassage/',views.newpassage,name='newpassage'),
    url(r'^passage/replys/(?P<passage_id>[0-9]+)',views.replys,name='replys'),
    url(r'^get_new_reply/(?P<passage_id>[0-9]+)',views.get_new_reply,name='get_new_reply'),
]