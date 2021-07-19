from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:article_id>/', views.detail ,name='detail'),
    path('<int:article_id>/leave_coment', views.leave_coment ,name='leave_coment'),
    path('<int:comment_id>/delete_comment', views.delete_comment ,name='delete_comment'),
    path('new_article', views.add_article,name='add_article'),
    path('<int:article_id>/delete', views.delete_article ,name='delete_article'),
    path('<int:article_id>/update', views.update_article ,name='update_article'),
]