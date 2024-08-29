from django.urls import path

import school.views as school_views

urlpatterns = [
    path('', school_views.StudentsList.as_view(), name='students'),
]
