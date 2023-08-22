from django.urls import path
from contact import views
app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    #Crud
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/create/', views.create, name='create'),
]
