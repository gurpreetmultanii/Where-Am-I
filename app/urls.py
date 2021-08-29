from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "view_closest_territory",
        views.view_closest_territory,
        name="view_closest_territory",
    ),
    path("ajax_filter/", views.ajax_filter, name="ajax_filter"),
    path("view_result/", views.view_result, name="view_result"),
]