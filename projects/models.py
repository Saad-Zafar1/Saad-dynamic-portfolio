from django.core.exceptions import ValidationError
from django.db import models


class Project(models.Model):
    class ProjectType(models.TextChoices):
        MACHINE_LEARNING = "machine_learning", "Machine Learning"
        AI_CHATBOT = "ai_chatbot", "AI Chatbot"
        AI_AGENT = "ai_agent", "AI Agent"
        CYBERSECURITY = "cybersecurity", "Cybersecurity"
        OPERATING_SYSTEMS = "operating_systems", "Operating Systems"
        WEB_DEVELOPMENT = "web_development", "Web Development"
        OTHER = "other", "Other"

    class RepositoryStatus(models.TextChoices):
        PUBLIC = "public", "Public Repository"
        PRIVATE = "private", "Private Repository"
        NO_REPOSITORY = "no_repository", "No Public Repository"

    title = models.CharField(
        max_length=160,
        help_text="Enter the project title.",
    )

    project_type = models.CharField(
        max_length=30,
        choices=ProjectType.choices,
        default=ProjectType.OTHER,
    )

    short_description = models.CharField(
        max_length=280,
        help_text="A short description displayed prominently on the card.",
    )

    description = models.TextField(
        help_text="Explain the project, its purpose, and your contribution.",
    )

    technologies = models.CharField(
        max_length=300,
        help_text="Separate technologies using commas.",
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Optional project screenshot or image.",
    )

    repository_status = models.CharField(
        max_length=20,
        choices=RepositoryStatus.choices,
        default=RepositoryStatus.NO_REPOSITORY,
    )

    github_url = models.URLField(
        blank=True,
        help_text="Required only when the repository is public.",
    )

    live_url = models.URLField(
        blank=True,
        help_text="Optional deployed project or demonstration link.",
    )

    is_featured = models.BooleanField(
        default=False,
        help_text="Mark important projects as featured.",
    )

    display_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Smaller numbers appear first.",
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Only active projects appear on the website.",
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
            "title",
        ]

        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def clean(self):
        super().clean()

        if (
            self.repository_status == self.RepositoryStatus.PUBLIC
            and not self.github_url
        ):
            raise ValidationError(
                {
                    "github_url": (
                        "Enter a GitHub URL when repository "
                        "status is Public Repository."
                    )
                }
            )

    def __str__(self):
        return self.title