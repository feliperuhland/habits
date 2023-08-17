from django.contrib import admin

from record import models


class SymptomInline(admin.TabularInline):
    model = models.CheckInSymptom
    autocomplete_fields = ["symptom"]

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class BehaviorInline(admin.TabularInline):
    model = models.CheckInBehavior
    autocomplete_fields = ["behavior"]

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(models.CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ["id", "datetime", "feeling"]
    inlines = [SymptomInline, BehaviorInline]


@admin.register(models.Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["symptom"]


@admin.register(models.Behavior)
class BehaviorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["behavior"]
