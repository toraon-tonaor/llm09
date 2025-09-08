from litellm import completion
from config import PROVIDER_MODEL as MODEL

def summarize(text, length="brief"):
    lengths = {"brief":"in 1–2 sentences","medium":"in 3–4 sentences","detailed":"in 5–6 sentences with key points"}
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"You are an expert summarizer. Summarize {lengths.get(length,'in 2–3 sentences')}"},
            {"role":"user","content":text}
        ],
        temperature=0.3, max_tokens=180,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    sample = """Recent advances in AI… (paste any article here)"""
    print(summarize(sample, "brief"))