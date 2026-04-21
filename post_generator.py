from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


# -----------------------------
# LENGTH MAPPING
# -----------------------------
def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


# -----------------------------
# MAIN GENERATOR
# -----------------------------
def generate_post(length, language, tag, tone, n=3):
    prompt = get_prompt(length, language, tag, tone)

    posts = []
    for _ in range(n):
        response = llm.invoke(prompt)
        posts.append(response.content)

    return posts


# -----------------------------
# PROMPT BUILDER
# -----------------------------
def get_prompt(length, language, tag, tone):
    length_str = get_length_str(length)

    prompt = f"""
    You are an expert LinkedIn content writer.

    Generate a structured LinkedIn post.

    STRUCTURE MUST BE:

    1. 🔥 Hook (attention grabbing first line)
    2. 📖 Story / Context
    3. 💡 Insight / Lesson
    4. 🚀 Call to Action (CTA)

    RULES:
    - Topic: {tag}
    - Length: {length_str}
    - Language: {language}
    - Tone: {tone}
    - No explanations outside post
    - Only output the final structured post
    """

    # Few-shot examples
    examples = few_shot.get_filtered_posts(length, language, tag)

    if examples and len(examples) > 0:
        prompt += "\n\nFollow this writing style:\n"

        for i, post in enumerate(examples[:2]):
            prompt += f"\nExample {i+1}:\n{post['text']}\n"

    return prompt


# -----------------------------
# TEST RUN
# -----------------------------
if __name__ == "__main__":
    print(generate_post("Medium", "English", "Job Search"))
