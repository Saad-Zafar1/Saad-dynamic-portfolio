from django.core.exceptions import ValidationError
from django.db import models


class Experience(models.Model):
    class ExperienceType(models.TextChoices):
        PROFESSIONAL = "professional", "Professional"
        ACADEMIC = "academic", "Academic"
        INTERNSHIP = "internship", "Internship"
        COMPETITION = "competition", "Competition"
        VOLUNTEER = "volunteer", "Volunteer"

    title = models.CharField(
        max_length=150,
        help_text="For example: Cybersecurity Researcher or AI Techathon Participant.",
    )

    organization = models.CharField(
        max_length=180,
        help_text="Company, university, platform, or organization name.",
    )

    experience_type = models.CharField(
        max_length=20,
        choices=ExperienceType.choices,
        default=ExperienceType.ACADEMIC,
    )

    location = models.CharField(
        max_length=120,
        blank=True,
    )

    start_year = models.PositiveSmallIntegerField()

    end_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    is_current = models.BooleanField(
        default=False,
        help_text="Check this when the experience is still continuing.",
    )

    description = models.TextField(
        help_text="Explain your responsibilities, work, and achievements.",
    )

    technologies = models.CharField(
        max_length=250,
        blank=True,
        help_text="Separate technologies using commas.",
    )

    display_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Smaller numbers appear first.",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "display_order",
            "-start_year",
            "-id",
        ]

        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def clean(self):
        super().clean()

        if self.is_current and self.end_year:
            raise ValidationError(
                {
                    "end_year": (
                        "Leave the end year blank when this "
                        "experience is currently continuing."
                    )
                }
            )

        if not self.is_current and not self.end_year:
            raise ValidationError(
                {
                    "end_year": (
                        "Enter an end year or mark this "
                        "experience as current."
                    )
                }
            )

        if (
            self.start_year
            and self.end_year
            and self.end_year < self.start_year
        ):
            raise ValidationError(
                {
                    "end_year": (
                        "The end year cannot be earlier "
                        "than the start year."
                    )
                }
            )

    def __str__(self):
        return f"{self.title} — {self.organization}"