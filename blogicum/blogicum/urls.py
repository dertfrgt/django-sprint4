from django.contrib import admin
from django.urls import include, path

from blog.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        RegisterView.as_view(),
        name='registration',
    ),
    path('', include('blog.urls', namespace='blog')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.csrf_failure'
