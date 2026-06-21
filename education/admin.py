from django.contrib import admin

from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "qualification",
        "institution",
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
        "is_current",
        "is_active",
        "start_year",
    )

    search_fields = (
        "qualification",
        "institution",
        "field_of_study",
        "location",
    )

    ordering = (
        "display_order",
        "-start_year",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Qualification Information",
            {
                "fields": (
                    "qualification",
                    "institution",
                    "field_of_study",
                    "location",
                )
            },
        ),
        (
            "Study Period",
            {
                "fields": (
                    "start_year",
                    "end_year",
                    "is_current",
                )
            },
        ),
        (
            "Academic Details",
            {
                "fields": (
                    "grade",
                    "description",
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