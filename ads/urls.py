from django.urls import path

from ads.views import CategoryView, ADSView, CategoryDetailsView, ADSDetailsView, index

urlpatterns = [
    path('', index),
    path('cat/', CategoryView.as_view()),
    path('ad/', ADSView.as_view()),
    path('cat/<int:pk>/', CategoryDetailsView.as_view()),
    path('ad/<int:pk>/', ADSDetailsView.as_view()),
]
