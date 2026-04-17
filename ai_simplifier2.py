from transformers import pipeline

simplifier = pipeline("text2text-generation", model="t5-small")

def simplify_text(report_summary):
    prompt = f"Explain in simple health terms: {report_summary}"
    result = simplifier(prompt, max_length=100, do_sample=True)
    return result[0]['generated_text']
