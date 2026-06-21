from django.contrib import admin

from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "experience_type",
        "start_year",
        "end_year",
        "is_current",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "experience_type",
        "is_current",
        "is_active",
        "start_year",
    )

    search_fields = (
        "title",
        "organization",
        "description",
        "technologies",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Main Information",
            {
                "fields": (
                    "title",
                    "organization",
                    "experience_type",
                    "location",
                )
            },
        ),
        (
            "Duration",
            {
                "fields": (
                    "start_year",
                    "end_year",
                    "is_current",
                )
            },
        ),
        (
            "Experience Details",
            {
                "fields": (
                    "description",
                    "technologies",
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