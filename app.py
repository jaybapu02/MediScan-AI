import streamlit as st
from analyser import analyze_report
from ai_simplifier3 import simplify_text
from ocr_reader import extract_text_from_image
from pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="🩺 Medical Report Simplifier", page_icon="💊")

st.title("🩺 AI Medical Report Simplifier (Gemini-Powered)")
st.write("Upload your report (PDF or image) or paste results manually 👇")

# --- File Upload Section ---
uploaded_file = st.file_uploader("📁 Upload a medical report", type=["png", "jpg", "jpeg", "pdf"])

extracted_text = ""

if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        # Save temporarily
        with open("temp_report.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        extracted_text = extract_text_from_pdf("temp_report.pdf")
        st.subheader("📄 Extracted Text from PDF:")
        st.text(extracted_text)

    else:
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        extracted_text = extract_text_from_image("temp_image.png")
        st.subheader("🧾 Extracted Text from Image:")
        st.text(extracted_text)

    st.info("You can edit or clean the extracted text below before analysis 👇")

# --- Manual Input Section ---
report_text = st.text_area("Enter or edit your report values:", extracted_text)

if st.button("Analyze"):
    try:
        report_lines = [line.strip() for line in report_text.split(",") if ":" in line]
        report_dict = {}
        for line in report_lines:
            # Split only on the first colon
            parts = line.split(":", 1)
            if len(parts) == 2:
                key, val = parts
                try:
                    report_dict[key.strip()] = float(val.strip())
                except ValueError:
                    st.warning(f"Skipping invalid entry: {line}")
            else:
                st.warning(f"Ignoring line (no valid key:value format): {line}")


        output = analyze_report(report_dict)
        st.subheader("📊 Report Analysis:")
        for line in output:
            st.write(line)

        ai_summary = simplify_text("\n".join(output))
        st.subheader("💬 AI Simplified Explanation:")
        st.write(ai_summary)

    except Exception as e:
        st.error(f"Error: {e}")
