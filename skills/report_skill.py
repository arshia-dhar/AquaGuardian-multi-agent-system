from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os
from datetime import datetime


def generate_mission_report(
    mission_name: str,
    vision_summary: str,
    telemetry_summary: str,
    research_summary: str
) -> str:
    """
    Generate a PDF mission report.

    Args:
        mission_name: Name of the mission.
        vision_summary: Output from Vision Agent.
        telemetry_summary: Output from Telemetry Agent.
        research_summary: Output from Research Agent.

    Returns:
        Path to generated PDF report.
    """

    try:
        # Create reports directory if it doesn't exist
        os.makedirs("reports", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = (
            f"reports/{mission_name}_{timestamp}.pdf"
        )

        doc = SimpleDocTemplate(
            filename,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )

        styles = getSampleStyleSheet()
        story = []

        # Title
        title = Paragraph(
            f"AquaGuardian Mission Report: {mission_name}",
            styles['Title']
        )
        story.append(title)
        story.append(Spacer(1, 0.2 * inch))

        # Timestamp
        generated_time = Paragraph(
            f"Generated on: {datetime.now()}",
            styles['Normal']
        )

        story.append(generated_time)
        story.append(Spacer(1, 0.3 * inch))

        # Vision Section
        story.append(
            Paragraph(
                "Vision Analysis",
                styles['Heading2']
            )
        )

        story.append(
            Paragraph(
                vision_summary.replace("\n", "<br/>"),
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 0.2 * inch))

        # Telemetry Section
        story.append(
            Paragraph(
                "Telemetry Analysis",
                styles['Heading2']
            )
        )

        story.append(
            Paragraph(
                telemetry_summary.replace("\n", "<br/>"),
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 0.2 * inch))

        # Research Section
        story.append(
            Paragraph(
                "Scientific Insights",
                styles['Heading2']
            )
        )

        story.append(
            Paragraph(
                research_summary.replace("\n", "<br/>"),
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 0.3 * inch))

        # Recommendations Section
        story.append(
            Paragraph(
                "Recommendations",
                styles['Heading2']
            )
        )

        recommendations = """
        • Review mission anomalies identified in telemetry.<br/>
        • Investigate detected debris or hazards.<br/>
        • Validate species detections with marine experts.<br/>
        • Consider follow-up surveys for ecological monitoring.
        """

        story.append(
            Paragraph(
                recommendations,
                styles['BodyText']
            )
        )

        # Build PDF
        doc.build(story)

        return (
            f"Mission report successfully generated: "
            f"{filename}"
        )

    except Exception as e:
        return (
            f"Error generating report: {str(e)}"
        )