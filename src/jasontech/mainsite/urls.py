from django.urls import path
from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('ministry/', views.ministry, name='ministry'),
    path('sermons/', views.sermons, name='sermons'),
    path('events/', views.events, name='events'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
