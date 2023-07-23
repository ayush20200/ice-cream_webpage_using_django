from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Ayush Ice-Cream Admin"
admin.site.site_title = "Ayush Ice-Cream Admin Portal"
admin.site.index_title = "Welcome to Ayush Ice-Cream "

urlpatterns = [
    path('home/', views.index, name='home'),
    path("about/", views.about ,name="about"),
    path("services/", views.services ,name="services"),
    path("contacts/", views.contacts ,name="contacts"),


]
