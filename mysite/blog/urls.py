
from django.urls import path
import blog.views


urlpatterns = [
    path('blog/', blog.views.home, name='home'),
    path('blog/<int:blog_id>', blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name='create'),

]
