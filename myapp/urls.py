from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('domains/<int:domains_id>', views.domains_by_id, name='domains_by_id'),
]