from django.contrib import admin
from django.urls import path, include
from API.views import PostView, PostCreateView, PostListCreateView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', PostView.as_view(), name='test_view'),
    path('create/', PostCreateView.as_view(), name='create_view'),
    path('createlist/', PostListCreateView.as_view(), name='post_list'),
    path('api-token-auth/', obtain_auth_token),
    path('rest-auth/', include('rest_auth.urls'))

]