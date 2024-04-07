from django.contrib import admin

from . import models as base_models


class WongnokUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(base_models.WongnokUser, WongnokUserAdmin)
