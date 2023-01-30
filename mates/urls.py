from rest_framework import routers
from .api import MateViewSet, TipoViewSet, ColorViewSet, PriceHistoryViewSet

# router is a variable that will be used in mateando\urls.py to register the routes of the API
router = routers.DefaultRouter()

# "api/mates" is the route of the API that will be used in mateando\urls.py to register the routes of the API
router.register("api/mates", MateViewSet, "mates")
router.register("api/tipos", TipoViewSet, "tipos")
router.register("api/colores", ColorViewSet, "colores")
router.register("api/pricehistory", PriceHistoryViewSet, "pricehistory")

urlpatterns = router.urls