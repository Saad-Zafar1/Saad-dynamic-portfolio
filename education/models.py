from django.core.exceptions import ValidationError
from django.db import models


class Education(models.Model):
    qualification = models.CharField(
        max_length=150,
        help_text="For example: BS Computer Science or Intermediate.",
    )

    institution = models.CharField(
        max_length=200,
        help_text="Enter the school, college, or university name.",
    )

    field_of_study = models.CharField(
        max_length=150,
        blank=True,
        help_text="For example: Computer Science.",
    )

    location = models.CharField(
        max_length=120,
        blank=True,
        help_text="For example: Lahore, Pakistan.",
    )

    start_year = models.PositiveSmallIntegerField(
        help_text="Enter the year in which this qualification started.",
    )

    end_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text="Leave blank if this qualification is currently in progress.",
    )

    is_current = models.BooleanField(
        default=False,
        help_text="Select this if you are currently studying here.",
    )

    grade = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional: CGPA, percentage, grade, or division.",
    )

    description = models.TextField(
        blank=True,
        help_text="Add relevant academic details or achievements.",
    )

    display_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Smaller numbers appear first.",
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Only active records are displayed on the portfolio.",
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
        verbose_name = "Education Record"
        verbose_name_plural = "Education Records"

    def clean(self):
        """
        Validate the relationship between education dates
        and the current-study status.
        """
        super().clean()

        if self.is_current and self.end_year:
            raise ValidationError(
                {
                    "end_year": (
                        "Leave the end year blank when the "
                        "qualification is currently in progress."
                    )
                }
            )

        if not self.is_current and not self.end_year:
            raise ValidationError(
                {
                    "end_year": (
                        "Enter an end year or mark this "
                        "qualification as currently in progress."
                    )
                }
            )

        if (
            self.end_year
            and self.start_year
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
        return f"{self.qualification} — {self.institution}"