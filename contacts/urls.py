from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnquiryViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'enquiries', EnquiryViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
