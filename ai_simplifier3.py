# import os
# os.environ["GRPC_VERBOSITY"] = "ERROR"
# os.environ["GLOG_minloglevel"] = "2"
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="GEMINI_API_KEY")

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
        # ✅ Use the available and stable model
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content([prompt])
        return response.text

    except Exception as e:
        print("⚠️ Flash model failed, trying Gemini Pro...")
        model = genai.GenerativeModel("models/gemini-2.5-pro")
        response = model.generate_content([prompt])
        return response.text