from rest_framework.routers import DefaultRouter
from .views import ProductViewSet



# automatically create crud urls
router = DefaultRouter()
router.register("", ProductViewSet, basename="product") 
urlpatterns = router.urls