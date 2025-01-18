from django.urls import path
from .views import AboutView, RulesView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('rules/', RulesView.as_view(), name='rules'),
]


# from django.urls import path
#
# from . import views
#
#
# app_name = 'pages'
#
# urlpatterns = [
#     path('about/', views.about, name='about'),
#     path('rules/', views.rules, name='rules'),
# ]
