from django.urls import path
from .import views
urlpatterns=[
    path('lr/',views.sample,name="sample"),
    path('rl/',views.sample2,name="sample2"),
    path('rl/add/',views.add,name="add"),
    path('rl/add/addrecord/',views.addrecord,name="addrecord"),
    path('rl/delete/<int:id>',views.delete,name="delete")

]