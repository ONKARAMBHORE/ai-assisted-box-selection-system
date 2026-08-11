from .views import BoxViewSet
from rest_framework.routers import DefaultRouter

# automatic CRUD 
router = DefaultRouter()
router.register("", BoxViewSet, basename="box")
urlpatterns = router.urls