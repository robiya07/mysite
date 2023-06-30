from django.urls import path, include
from django.conf.urls.static import static
from main.views import contactView, successView, download_cv_view
from mysite.settings import STATIC_URL, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # path('', index_view),
    path("", contactView, name="contact"),
    path("success/", successView, name="success"),
    path("pdf/", download_cv_view, name="pdf"),
]
