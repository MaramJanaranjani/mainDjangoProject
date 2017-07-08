from django.conf.urls import url
from samapp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^home$', views.home, name = "home"),
    url(r'^det$', views.det, name = "det"),
    url(r'index$', views.index, name = "index"),
    url(r'^laundry_search/([0-9])/([0-9])$', views.laundry_search, name = "laundry_search"),
    url(r'^shop_view/([0-9])$', views.shop_view, name = "shop_view"),
    url(r'^count_clothes$', views.count_clothes, name = "count_clothes"),
    url(r'^fast_delivery$', views.fast_delivery, name = "fast_delivery"),
    url(r'^total_cost$', views.total_cost, name = "total_cost"),
    url(r'^register$', views.register, name = "register"),
    url(r'^success_message$', views.success_message, name = "success_message"),
    url(r'^ratings$', views.ratings, name = "ratings"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^logout/$', auth_views.logout, name = 'logout'),
    url(r'^$', views.index, name = "index"),
]
