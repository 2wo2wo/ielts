from django.urls import path,include
from . import views
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'apis', views.MatchingCollectionView)

urlpatterns = [
    # path('api/v1/', views.MatchingCollectionView.as_view({"get":"list"}), name='index'),
    # path('api/v1/<int:pk>/', views.MatchingCollectionView.as_view({"put":"update"})),
    path('api/v2/<int:pk>/',views.CollectionView.as_view()),
    # path('api/v1/books/<int:pk>/', views.BookView.as_view())


]
