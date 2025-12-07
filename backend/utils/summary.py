import google.generativeai as genai
def generate_summary(report):
    prompt=f"""Given this data quality raw report:\n{report}\nWrite a human-readable summary of
the data quality issues and suggest 2-3 improvements"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

    