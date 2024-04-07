from django.contrib import admin

from . import models as recipe_models


class WongnokRecipeAdmin(admin.ModelAdmin):
    pass

class RatingLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(recipe_models.WongnokRecipe, WongnokRecipeAdmin)
admin.site.register(recipe_models.RatingLog, RatingLogAdmin)
