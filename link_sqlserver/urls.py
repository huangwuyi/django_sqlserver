from django.contrib import admin
from django.urls import path, include
import link_sqlserver.views as lk_views

urlpatterns = [
    path('childrenlist', lk_views.ChildrenListView.as_view(), name='childrenlist'),
    path('childrencreate', lk_views.ChildrenCreateView.as_view(), name='childrencreate'),
    path('childrendetail/<int:pk>/', lk_views.ChildrenDetailView.as_view(), name='childrendetail'),
    path('childrendelete/<int:pk>/', lk_views.ChildrenDeleteView.as_view(), name='childrendelete'),
    path('childrenupdate/<int:pk>/', lk_views.ChildrenUpdateView.as_view(), name='childrenupdate'),
    path('mac', lk_views.MacAndIP, name='macandip'),
]
