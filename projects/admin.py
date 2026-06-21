from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project_type",
        "repository_status",
        "is_featured",
        "display_order",
        "is_active",
    )

    list_editable = (
        "is_featured",
        "display_order",
        "is_active",
    )

    list_filter = (
        "project_type",
        "repository_status",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "technologies",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "project_type",
                    "short_description",
                    "description",
                    "technologies",
                    "image",
                )
            },
        ),
        (
            "Repository and Links",
            {
                "fields": (
                    "repository_status",
                    "github_url",
                    "live_url",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "is_featured",
                    "display_order",
                    "is_active",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )