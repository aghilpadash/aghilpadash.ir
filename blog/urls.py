from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),

    url(r'^article/$', views.SingleArticleAPIView.as_view(), name='single_article'),
    url(r'^article/all/$', views.AllArticleAPIView.as_view(), name='all_articles'),
]