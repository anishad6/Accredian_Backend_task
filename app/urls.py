from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import ReferralListapis

router = DefaultRouter()
router.register(r'crud',ReferralListapis)

urlpatterns = [
   path('',include(router.urls))
]
