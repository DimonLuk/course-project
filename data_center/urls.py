from django.urls import re_path
from .views import ComponentsByWarrantyViewSet, ProcessRawSqlAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(
    r'components_by_warranty',
    ComponentsByWarrantyViewSet,
    basename='components_by_warranty')
urlpatterns = [
    re_path(r'^raw_sql/', ProcessRawSqlAPIView.as_view()),
    *router.urls
]
