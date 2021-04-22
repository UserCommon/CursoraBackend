from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission
from rest_framework.views import APIView

from .serializers import *


class IsObjectOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author.user


class IsProfileOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUserOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return User == request.user


class UserConfirm(APIView):

    def get(self, request):
        pass


class UserViewList(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserListSerializer
    queryset = User.objects.all().order_by('-date_joined')


class UserRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsUserOwner, ]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class ProfileViewList(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer


class ProfileRetrieveView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()


class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsProfileOwner, ]
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()


class UserLogoutView(APIView):
    def get(self, request):
        pass


class ProfileInfoView(APIView):
    def get(self, request):
        pass


class CourseListView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CourseEasySerializer
    queryset = Course.objects.all()


class CourseRetrieveView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser, ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile_user)


# NOTE: Обновляем через patch запрос, да
class CourseUpdateView(generics.UpdateAPIView):
    permission_classes = [IsObjectOwner, IsAdminUser, ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_update(self, serializer, **kwargs):
        serializer.save(video_author=self.request.user.profile_user)


# NOTE: Delete метод единственный разрешённый для этого класса
class CourseDeleteView(generics.DestroyAPIView):
    permission_classes = [IsObjectOwner, IsAdminUser, ]
    serializer_class = VideoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Course.objects.filter(pk=pk)


class CourseVideoListView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = VideoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Video.objects.filter(course__pk=pk)


class CourseVideoCreateView(generics.CreateAPIView):
    permission_classes = [IsUserOwner, IsAdminUser, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def perform_create(self, serializer, **kwargs):
        serializer.save(video_author=self.request.user.profile_user, course_id=self.kwargs['pk'])


class CourseVideoRetrieveView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializers = VideoSerializer

    def get_queryset(self):
        video_pk = self.kwargs['video_pk']
        return Video.objects.filter(id=video_pk)


class CourseVideoUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUserOwner, IsAdminUser, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def perform_update(self, serializer, **kwargs):
        serializer.save(video_author=self.request.user.profile_user, course_id=self.kwargs['pk'])


class CourseVideoDeleteView(generics.DestroyAPIView):
    permission_classes = [IsUserOwner, IsAdminUser, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class VideoRetrieveView(generics.RetrieveAPIView):
    permissions_classes = [AllowAny, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class VideoListView(generics.ListAPIView):
    premission_classes = [IsAdminUser, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class CommentaryListView(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()


class CommentaryDetailView(generics.RetrieveAPIView):
    permissions_classes = [AllowAny, ]
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()


class CategoryListView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()