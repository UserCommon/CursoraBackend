from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.authtoken.views import obtain_auth_token

# TODO: Update, Destroy urls add

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
#    path('auth/token/', obtain_auth_token, name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profiles/', ProfileViewList.as_view()),
    path('profiles/<int:pk>/', ProfileRetrieveView.as_view()),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view()),
    path('users/', UserViewList.as_view()),
    path('users/register/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveView.as_view()),
#    path('users/activate/<str:uid>/<str:jwt>', UserActivate.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/logout/', UserLogoutView.as_view()),
    path('profile/info/', ProfileInfoView.as_view()),
    path('video/', VideoListView.as_view()),
    path('video/<int:pk>/', VideoRetrieveView.as_view()),
    path('course/', CourseListView.as_view()),
    path('course/create/', CourseCreateView.as_view()),
    path('course/<int:pk>/', CourseRetrieveView.as_view()),
    path('course/<int:pk>/update/', CourseUpdateView.as_view()),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view()),
    path('course/<int:pk>/video/', CourseVideoListView.as_view(), name='course_videos'),
    path('course/<int:pk>/video/create/', CourseVideoCreateView.as_view(), name='create_video'),
    path('course/<int:pk>/video/<int:video_pk>/', CourseVideoRetrieveView.as_view(), name='show_video'),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryRetrieveView.as_view()),
    path('commentary/', CommentaryListView.as_view(), name='all_commentaries')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
