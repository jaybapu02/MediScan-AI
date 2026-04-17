from google import genai
import os

# Initialize client using environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def simplify_text(report_summary):
    """
    Takes analyzed report text and returns a simple, user-friendly explanation.
    """

    prompt = (
        "You are a friendly medical assistant. "
        "Explain this report in simple, human language so that anyone can understand it:\n\n"
        f"{report_summary}"
    )

    try:
        # ✅ Fast and cost-efficient model
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        print("⚠️ Flash model failed, trying Pro...")

        try:
            response = client.models.generate_content(
                model="gemini-1.5-pro",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return "❌ Error generating explanation. Please try again."