import google.generativeai as genai

def generate_summary(report):
    prompt = f"""
    Given this raw data quality report:

    {report}

    Write a clean, human-readable summary:
    - Mention major data quality issues
    - Point out missing values, duplicates, datatype issues
    - Suggest 2–3 improvements
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text or "No summary generated"
