from rest_framework import routers
from .views import TodoAPI

router = routers.DefaultRouter()
router.register('Todo',TodoAPI )