from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from security.validation import validate_file

def analyze_underwater_image(image_path: str) -> str:
    validate_file(image_path)
    """
    Analyze an underwater image and provide mission-relevant insights.

    Args:
        image_path: Path to the underwater image.

    Returns:
        Analysis summary.
    """

    load_dotenv()

    try:
        client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        img = open(image_path, "rb")
        try:
            image_bytes = img.read()
        finally:
            img.close()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/jpeg"
                ),
                """
                Analyze this underwater image for an AUV mission.

                Provide:
                1. Marine species detected.
                2. Coral reef observations.
                3. Marine debris or pollution.
                4. Obstacles or hazards.
                5. Overall scene summary.

                Keep the response concise and scientific.
                """
            ]
        )

        return response.text

    except FileNotFoundError:
        return f"Image not found: {image_path}"

    except Exception as e:
        return f"Error analyzing image: {str(e)}"