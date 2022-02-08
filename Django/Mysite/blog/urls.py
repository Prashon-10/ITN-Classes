
from django.urls import path, include
from.import views

urlpatterns = [

    path("", views.index, name="index"),
    path("delete/<id>", views.delete, name="delete"),
    path("edit/<id>", views.edit, name="edit"),
    path("about", views.about),
    path("contact", views.contact),
    # path("services", views.services),

]
