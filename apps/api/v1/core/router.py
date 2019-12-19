from rest_framework import routers

from .views import TableViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register(r'tables', TableViewSet, )
router.register(r'orders', OrderViewSet)
urlpatterns = router.urls
