from django.contrib import admin

from .models import Bio


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "job_title",
        "email",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "full_name",
        "job_title",
        "email",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "full_name",
                    "job_title",
                    "profile_picture",
                    "professional_description",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "location",
                )
            },
        ),
        (
            "Professional Links",
            {
                "fields": (
                    "github_url",
                    "linkedin_url",
                )
            },
        ),
        (
            "Record Settings",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )