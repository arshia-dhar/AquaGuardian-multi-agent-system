import json
from pathlib import Path

DATA_DIR = Path("data")


def load_text_file(filename: str) -> str:
    """Load a text/markdown knowledge file."""

    path = DATA_DIR / filename

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")


def load_json(filename: str) -> dict:
    """Load a JSON knowledge base."""

    path = DATA_DIR / filename

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_ecological_insights(observation: str) -> str:
    """
    Provide ecological insights using the local knowledge base.

    Args:
        observation: Vision agent output or detected observations.

    Returns:
        Ecological insights relevant to the observations.
    """

    observation = observation.lower()

    ecological_text = load_text_file("ecological_knowledge.md")
    species_db = load_json("marine_species.json")
    coral_db = load_json("coral_species.json")
    hazards_db = load_json("hazards.json")
    guidelines_db = load_json("conservation_guidelines.json")

    insights = []

    # -------- Marine Species --------

    for species, info in species_db.items():
        if species in observation:
            insights.append(
                f"Species: {species.title()}\n"
                f"Importance: {info['importance']}\n"
                f"{info['description']}"
            )

    # -------- Coral Types --------

    for coral, info in coral_db.items():
        if coral in observation:
            insights.append(
                f"Coral: {coral.title()}\n"
                f"{info['importance']}"
            )

    # -------- Hazards --------

    for hazard, info in hazards_db.items():
        if hazard.replace("_", " ") in observation:
            insights.append(
                f"Hazard: {hazard.replace('_', ' ').title()}\n"
                f"Severity: {info['severity'].title()}\n"
                f"Recommendation: {info['recommendation']}"
            )

    # -------- Conservation Guidelines --------

    if "healthy" in observation and "reef" in observation:
        insights.extend(guidelines_db.get("healthy_reef", []))

    if (
        "bleaching" in observation
        or "degraded" in observation
        or "dead coral" in observation
    ):
        insights.extend(guidelines_db.get("degraded_reef", []))

    if (
        "plastic" in observation
        or "debris" in observation
    ):
        insights.extend(guidelines_db.get("marine_debris", []))

    # -------- Fallback --------

    if not insights:
        insights.append(
            "No specific match found in the structured knowledge base."
        )

        if ecological_text:
            insights.append(
                "\nGeneral Ecological Reference:\n"
                + ecological_text[:800] + "..."
            )

    return "\n\n".join(insights)