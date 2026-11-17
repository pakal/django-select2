from django.urls import re_path

from .views import AutoResponseView

urlpatterns = [
    re_path(r"^fields/auto.json$",
            AutoResponseView.as_view(), name="django_select2_central_json"),
]
