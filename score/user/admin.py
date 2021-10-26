from django.contrib import admin

# Register your models here.
from django.core.paginator import Paginator
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin

from user.models import User


# 全部下载
class UserResources(ModelResource):
    class Meta:
        model = User
        fields = ("US_name", "US_equation_num", "US_right_radio")
        export_order = ["US_name", "US_equation_num", "US_right_radio"]


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resources_class = UserResources

    list_display = ["US_name", "US_equation_num", "US_right_radio"]

    search_fields = ["US_name"]

    list_filter = ['US_name']

    ordering = ("-US_equation_num", "-US_right_radio")

    list_per_page = 15
    paginator = Paginator
