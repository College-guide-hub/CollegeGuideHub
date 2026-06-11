def check_resume(text):

    tips = []

    if "Projects" not in text:
        tips.append(
            "Add Projects Section"
        )

    if "Skills" not in text:
        tips.append(
            "Add Skills Section"
        )

    return tips
