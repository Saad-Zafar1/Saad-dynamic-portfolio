from django.db import models


class Bio(models.Model):
    full_name = models.CharField(
        max_length=100,
        help_text="Enter your complete professional name.",
    )

    job_title = models.CharField(
        max_length=150,
        help_text="For example: Cybersecurity Student or Python Developer.",
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
        help_text="Upload a professional profile picture.",
    )

    professional_description = models.TextField(
        help_text="Write a short professional introduction.",
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    location = models.CharField(
        max_length=100,
        blank=True,
    )

    github_url = models.URLField(
        blank=True,
    )

    linkedin_url = models.URLField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Only active Bio records can appear on the portfolio.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.full_name