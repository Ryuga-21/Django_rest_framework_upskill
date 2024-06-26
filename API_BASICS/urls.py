from django.urls import path,include
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('article/',article_list),
    path('article/',ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail)
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/<int:id>/',GenericAPIView.as_view()),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls))

]