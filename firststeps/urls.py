from django.urls import path
from . import views
urlpatterns = [
    path('terms/',views.terms,name='terms'),
    path('bank/',views.bank,name='bank'),
    path('card/',views.card,name='card'),
    path('bank/ajax-autocomplete/<str:model>/', views.ajax, name='ajax-autocomplete'),
]