from .views import UserViewSet, TrackerViewSet, ProductViewSet, StatusViewSet, TrackersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'tracker/(?P<code>[^/]+)', TrackerViewSet, basename='tracker')
router.register(r'trackers', TrackersViewSet, basename='trackers')
router.register(r'product', ProductViewSet, basename="product")
router.register(r'status', StatusViewSet, basename='status')

urlpatterns = router.urls