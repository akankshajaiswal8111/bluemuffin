from django.urls import path
from . import views
from .views import SignUp
#from .views import Upload

urlpatterns = [
    path('', views.get, name='list_old'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='edit'),
    path('upload/', views.post, name='model_form_upload'),
#    path('signup/', SignUp.as_view(), name='signup'),
    path('list/', views.list, name='list')
]
