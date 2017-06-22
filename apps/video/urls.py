from django.conf.urls import url
from views import video_list, video_detail

urlpatterns = [
    url(r'^video/$', video_list),
    url(r'^video/(?P<pk>[0-9]+)/$', video_detail),
]