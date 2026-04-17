from openai import OpenAI
import os
# Initialize client (replace with your actual API key)
client = OpenAI(api_key="OPENAI_API_KEY")

def simplify_text(report_summary):
    """
    Takes analyzed report text and returns a human-friendly explanation.
    """
    prompt = (
        "Explain this medical report in simple, friendly language for a non-medical person:\n"
        f"{report_summary}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
