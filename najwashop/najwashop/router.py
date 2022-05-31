from najwashop_app.viewsets import ClientViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Client',ClientViewset)