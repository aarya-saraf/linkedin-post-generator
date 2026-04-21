import json
import re
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


# -----------------------------
# CLEAN TEXT (IMPORTANT)
# -----------------------------
def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.encode("utf-8", "ignore").decode("utf-8")
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove emojis/special chars
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# -----------------------------
# PROCESS POSTS
# -----------------------------
def process_posts(raw_file_path, processed_file_path):

    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)

    enriched_posts = []

    for post in posts:
        clean_post_text = clean_text(post["text"])

        metadata = extract_metadata(clean_post_text)

        post_with_metadata = post | metadata
        enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post.get("tags", [])
        post["tags"] = [
            unified_tags.get(tag, tag) for tag in current_tags
        ]

    with open(processed_file_path, mode="w", encoding="utf-8") as outfile:
        json.dump(enriched_posts, outfile, indent=4, ensure_ascii=False)


# -----------------------------
# EXTRACT METADATA (FIXED PROMPT)
# -----------------------------
def extract_metadata(post):

    template = """
You are given a LinkedIn post. Extract:

1. line_count (number of lines)
2. language (English or Hinglish)
3. tags (maximum 2 tags)

Return ONLY valid JSON in this format:

{{"line_count": 0, "language": "", "tags": []}}

Post:
{post}
"""

    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    try:
        response = chain.invoke({"post": post})
        json_parser = JsonOutputParser()
        return json_parser.parse(response.content)

    except OutputParserException:
        return {
            "line_count": 0,
            "language": "Unknown",
            "tags": []
        }


# -----------------------------
# UNIFY TAGS
# -----------------------------
def get_unified_tags(posts_with_metadata):

    unique_tags = set()

    for post in posts_with_metadata:
        unique_tags.update(post.get("tags", []))

    unique_tags_list = ", ".join(unique_tags)

    template = """
You are given a list of tags.

Task:
1. Merge similar tags into unified categories
2. Use Title Case
3. Return ONLY valid JSON mapping original -> unified tag

Example:
{{"Jobseekers": "Job Search", "Job Hunting": "Job Search"}}

Tags:
{tags}
"""

    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    response = chain.invoke({"tags": unique_tags_list})

    json_parser = JsonOutputParser()
    return json_parser.parse(response.content)



# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    process_posts("raw_posts.json", "processed_posts.json")
