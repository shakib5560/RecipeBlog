
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('blog/', views.blog, name='blog'),
      path('allrecipe/', include([
        path('', views.allrecipe, name='allrecipe'),
        path('delectitem/<int:id>', views.delectitem, name='delectitem'),
        path('edititem/<int:id>', views.edititem, name='edititem'),
    ])),
  path('contect/', views.contect, name='contect'),
  path('about/', views.about, name='about'),
  path('delectitem/<int:id>', views.delectitem, name='delectitem'),
  path('edititem/<int:id>', views.edititem, name='edititem'),
  path('signup/', views.signup, name='signup'),
  path('signin/', views.signin, name='signin'),
]
