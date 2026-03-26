from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static, serve
from landing import views
from pathlib import Path
from django.views.defaults import page_not_found

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("technology/", views.technology, name="technology"),
    path("projects/", views.projects, name="projects"),
    path("reviews/", views.reviews, name="reviews"),
    path("faq/", views.faq, name="faq"),
    path("contacts/", views.contacts, name="contacts"),
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': BASE_DIR}),
    path("privacy/", views.privacy, name="privacy"),
    path("thanks/", views.thanks, name="thanks"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'landing.views.custom_404'






