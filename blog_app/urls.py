from django.urls import path
from django.conf.urls.static import static
from Blog_Go import settings

from . import views


urlpatterns = [
    path('', views.blog_list,name='blog_list'),
    path('add_blog/', views.add_blog,name='add_blog'),
    path('full_blog/<int:id>/', views.full_blog,name='full_blog'),
    path('edit/<int:id>/',views.edit_post,name="edit_post"),
    path('delete/<int:id>/',views.delete_post,name="delete_post")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

