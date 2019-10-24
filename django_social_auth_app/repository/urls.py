from django.urls import path
from . import views

urlpatterns = [
    path(r'get_repositories', views.get_repositories, name='get_repositories'),
    path(r'edit_repository_tags/<repository_id>',views.edit_repository_tags, name='edit_repository_tags'),
    path(r'new_tag/<repository_id>',views.new_tag, name='new_tag'),
    path(r'update_repository/<repository_id>',views.update_repository, name='update_repository'),
    path(r'remove_repository/<repository_id>', views.remove_repository, name='remove_repository'),

]