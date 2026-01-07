from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1
)

def generate_ai_content(review):
    prompt = f"""
Review:
{review}

Return JSON only:
{{"response":"...", "summary":"...", "action":"..."}}

JSON:
"""
    output = generator(prompt, max_new_tokens=80, do_sample=False)
    return output[0]["generated_text"]

