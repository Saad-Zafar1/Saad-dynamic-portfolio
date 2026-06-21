from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Skill(models.Model):
    class Category(models.TextChoices):
        CYBERSECURITY = "cybersecurity", "Cybersecurity"
        PROGRAMMING = "programming", "Programming"
        WEB_DEVELOPMENT = "web_development", "Web Development"
        DATABASE = "database", "Database"
        NETWORKING = "networking", "Networking"
        TOOLS = "tools", "Tools and Technologies"
        PROFESSIONAL = "professional", "Professional Skills"

    name = models.CharField(
        max_length=100,
        help_text="For example: Python, Nmap, Django, or Communication.",
    )

    category = models.CharField(
        max_length=30,
        choices=Category.choices,
        default=Category.TOOLS,
    )

    proficiency = models.PositiveSmallIntegerField(
        default=70,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ],
        help_text="Enter a proficiency value from 1 to 100.",
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        help_text="Optional short explanation of your experience.",
    )

    display_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Smaller numbers appear first.",
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Only active skills appear on the portfolio.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "category",
            "display_order",
            "name",
        ]

        verbose_name = "Skill"
        verbose_name_plural = "Skills"

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "category",
                ],
                name="unique_skill_per_category",
            )
        ]

    def __str__(self):
        return f"{self.name} — {self.get_category_display()}"