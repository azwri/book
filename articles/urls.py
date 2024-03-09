from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_id>/', views.article, name='article'),
    path('plans/', views.plans, name='plans'),
    path('subscribe/<paypal_subscription_id>/<plan>/', views.subscribe, name='subscribe'),
]