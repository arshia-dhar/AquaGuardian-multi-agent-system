from skills.telemetry_skill import analyze_telemetry
from skills.vision_skill import analyze_underwater_image
from skills.research_skill import get_ecological_insights
from skills.report_skill import generate_mission_report


# Analyze telemetry
telemetry_summary = analyze_telemetry(
    "data/telemetry/sample_mission.csv"
)

# Analyze image
vision_summary = analyze_underwater_image(
    "data/images/test.jpg"
)

# Generate ecological insights
research_summary = get_ecological_insights(
    vision_summary
)

# Generate final report
report_path = generate_mission_report(
    mission_name="Coral_Reef_Survey",
    vision_summary=vision_summary,
    telemetry_summary=telemetry_summary,
    research_summary=research_summary
)

print("\n=== VISION ===")
print(vision_summary)

print("\n=== TELEMETRY ===")
print(telemetry_summary)

print("\n=== RESEARCH ===")
print(research_summary)

print("\n=== REPORT ===")
print(report_path)