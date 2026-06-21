from django.contrib import admin

from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "proficiency",
        "display_order",
        "is_active",
    )

    list_editable = (
        "proficiency",
        "display_order",
        "is_active",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "category",
        "display_order",
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Skill Information",
            {
                "fields": (
                    "name",
                    "category",
                    "description",
                )
            },
        ),
        (
            "Proficiency",
            {
                "fields": (
                    "proficiency",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )