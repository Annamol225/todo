from . import views
from django.urls import path

urlpatterns = [
    path('',views.task,name='task'),
    # path('delete/<int:tid>',views.delete,name='delete'),
    # path('update/<int:id>',views.update,name='update'),
    # path('detail/<int:id>',views.detail,name='detail'),
    # path('lviews', views.lviews.as_view(), name='lviews'),
    path('dviews/<int:pk>', views.dviews.as_view(), name='dviews'),
    path('uviews/<int:pk>', views.uviews.as_view(), name='uviews'),
    path('delviews/<int:pk>', views.delviews.as_view(), name='delviews')


]
