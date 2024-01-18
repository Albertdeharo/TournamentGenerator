from django.urls import path
from .views import CompanyView
from .views import TournamentListView

urlpatterns=[
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
    path('tournaments/', TournamentListView.as_view(), name='tournaments_list'),
]