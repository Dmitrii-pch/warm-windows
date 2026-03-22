from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from landing import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("technology/", views.technology, name="technology"),
    path("projects/", views.projects, name="projects"),
    path("reviews/", views.reviews, name="reviews"),
    path("faq/", views.faq, name="faq"),
    path("contacts/", views.contacts, name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







