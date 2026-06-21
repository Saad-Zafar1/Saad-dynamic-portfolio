from django.shortcuts import render

from bio.models import Bio
from education.models import Education
from experience.models import Experience
from projects.models import Project
from skills.models import Skill


def home(request):
    bio = (
        Bio.objects
        .filter(is_active=True)
        .order_by("-updated_at")
        .first()
    )

    educations = Education.objects.filter(
        is_active=True,
    )

    skills = Skill.objects.filter(
        is_active=True,
    )

    experiences = Experience.objects.filter(
        is_active=True,
    )

    projects = Project.objects.filter(
        is_active=True,
    )

    context = {
        "bio": bio,
        "educations": educations,
        "skills": skills,
        "experiences": experiences,
        "projects": projects,
    }

    return render(
        request,
        "core/home.html",
        context,
    )