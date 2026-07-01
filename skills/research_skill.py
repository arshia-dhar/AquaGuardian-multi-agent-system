def get_ecological_insights(observation: str) -> str:
    """
    Provide ecological insights for underwater observations.

    Args:
        observation: Species or observation detected during mission.

    Returns:
        Ecological significance and conservation insights.
    """

    knowledge_base = {
        "shark":
            "Sharks are apex predators and play a crucial role in maintaining marine ecosystem balance.",

        "coral":
            "Coral reefs support approximately 25% of all marine species and are highly sensitive to environmental changes.",

        "plastic":
            "Plastic pollution can damage coral reefs and pose serious threats to marine organisms through ingestion and entanglement.",

        "fish":
            "Fish diversity is often used as an indicator of reef ecosystem health.",

        "sea turtle":
            "Sea turtles are considered indicator species and are vulnerable to marine debris and habitat degradation."
    }

    insights = []

    observation = observation.lower()

    for key, value in knowledge_base.items():
        if key in observation:
            insights.append(f"{key.title()}: {value}")

    if not insights:
        insights.append(
            "No specific ecological information available for the provided observation."
        )

    return "\n".join(insights)