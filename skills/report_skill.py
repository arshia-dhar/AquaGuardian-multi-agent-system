from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from datetime import datetime
import os


def _add_section(story, title, text, styles):
    """Render a report section with automatic formatting."""

    story.append(Paragraph(title, styles["SectionHeading"]))
    story.append(Spacer(1, 0.12 * inch))

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        # Markdown heading
        if line.startswith("### "):
            story.append(
                Paragraph(
                    line[4:],
                    styles["SubHeading"]
                )
            )

        # Bullet list
        elif line.startswith("- "):
            story.append(
                Paragraph(
                    "• " + line[2:],
                    styles["Body"]
                )
            )

        # Numbered list
        elif (
            len(line) > 2
            and line[0].isdigit()
            and line[1] == "."
        ):
            story.append(
                Paragraph(
                    line,
                    styles["Body"]
                )
            )

        else:
            story.append(
                Paragraph(
                    line,
                    styles["Body"]
                )
            )

    story.append(Spacer(1, 0.22 * inch))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=HexColor("#CCCCCC")
        )
    )
    story.append(Spacer(1, 0.18 * inch))


def generate_mission_report(
    mission_name,
    vision_summary,
    telemetry_summary,
    research_summary,
):
    """
    Generate a professional AquaGuardian mission report.
    """

    try:

        os.makedirs("reports", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = (
            f"reports/{mission_name}_{timestamp}.pdf"
        )

        doc = SimpleDocTemplate(
            filename,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )

        styles = getSampleStyleSheet()

        styles.add(
            ParagraphStyle(
                name="TitleStyle",
                parent=styles["Title"],
                alignment=TA_CENTER,
                fontSize=24,
                spaceAfter=18,
                textColor=HexColor("#0B4F6C")
            )
        )

        styles.add(
            ParagraphStyle(
                name="SectionHeading",
                parent=styles["Heading2"],
                textColor=HexColor("#1565C0"),
                fontSize=16,
                spaceBefore=12,
                spaceAfter=8
            )
        )

        styles.add(
            ParagraphStyle(
                name="SubHeading",
                parent=styles["Heading3"],
                textColor=HexColor("#37474F"),
                fontSize=13
            )
        )

        styles.add(
            ParagraphStyle(
                name="Body",
                parent=styles["BodyText"],
                leading=18,
                spaceAfter=6,
                fontSize=10.5
            )
        )

        story = []

        # -------------------------------------------------
        # COVER
        # -------------------------------------------------

        story.append(
            Paragraph(
                "AquaGuardian",
                styles["TitleStyle"]
            )
        )

        story.append(
            Paragraph(
                "<b>Autonomous Underwater Mission Report</b>",
                styles["Heading1"]
            )
        )

        story.append(
            Spacer(1, 0.3 * inch)
        )

        story.append(
            Paragraph(
                f"<b>Mission:</b> {mission_name}",
                styles["Body"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y %H:%M:%S')}",
                styles["Body"]
            )
        )

        story.append(
            Spacer(1, 0.25 * inch)
        )

        story.append(
            HRFlowable(
                width="100%",
                thickness=2,
                color=HexColor("#1565C0")
            )
        )

        story.append(
            Spacer(1, 0.25 * inch)
        )

        # -------------------------------------------------
        # CONTENT
        # -------------------------------------------------

        _add_section(
            story,
            "Vision Analysis",
            vision_summary,
            styles
        )

        _add_section(
            story,
            "Telemetry Analysis",
            telemetry_summary,
            styles
        )

        _add_section(
            story,
            "Scientific Insights",
            research_summary,
            styles
        )

        story.append(
            Paragraph(
                "Recommendations",
                styles["SectionHeading"]
            )
        )

        recommendations = [
            "Review mission anomalies before deployment.",
            "Verify hazard detections with a human operator.",
            "Schedule a follow-up ecological survey if required.",
            "Archive mission data for future trend analysis."
        ]

        for rec in recommendations:
            story.append(
                Paragraph(
                    "• " + rec,
                    styles["Body"]
                )
            )

        story.append(
            Spacer(1, 0.35 * inch)
        )

        story.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=HexColor("#888888")
            )
        )

        story.append(
            Spacer(1, 0.12 * inch)
        )

        story.append(
            Paragraph(
                "<font color='#777777'>"
                "Generated automatically by AquaGuardian "
                "using a Google ADK multi-agent workflow."
                "</font>",
                styles["Body"]
            )
        )

        doc.build(story)

        return f"Mission report successfully generated: {filename}"

    except Exception as e:
        return f"Error generating report: {e}"