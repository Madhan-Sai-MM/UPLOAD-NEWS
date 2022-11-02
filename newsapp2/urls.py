from django.urls import path
from . import views

urlpatterns = [
    path('', views.class1.as_view(), name='mm_list'),
    path('views/<int:pk>', views.class2.as_view(), name='mm_detail'),
    path('new', views.class3.as_view(), name='mm_new'),
    path('policy', views.policy, name='policy'),
    path('termsandconditions', views.termsandconditions, name='termsandconditions'),
    path('pageinpage', views.pageinpage, name='pageinpage')
]