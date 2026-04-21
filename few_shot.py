import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    # -----------------------------
    # LOAD + CLEAN DATA
    # -----------------------------
    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

        self.df = pd.json_normalize(posts)

        # Ensure line_count is numeric
        self.df['line_count'] = self.df['line_count'].astype(int)

        # Create length category
        self.df['length'] = self.df['line_count'].apply(self.categorize_length)

        # Clean language (remove spaces + normalize case)
        self.df['language'] = self.df['language'].astype(str).str.strip()

        # FIX: Ensure tags are always lists
        self.df['tags'] = self.df['tags'].apply(
            lambda x: x if isinstance(x, list) else []
        )

        # Collect unique tags safely
        all_tags = sum(self.df['tags'], [])
        self.unique_tags = list(set(all_tags))

    # -----------------------------
    # FILTER POSTS
    # -----------------------------
    def get_filtered_posts(self, length, language, tag):

        df_filtered = self.df[
            (self.df['length'] == length) &
            (self.df['language'].str.strip().str.lower() == language.lower()) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]

        return df_filtered.to_dict(orient='records')

    # -----------------------------
    # LENGTH CATEGORY
    # -----------------------------
    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    # -----------------------------
    # GET ALL TAGS
    # -----------------------------
    def get_tags(self):
        return self.unique_tags


# -----------------------------
# MAIN TEST
# -----------------------------
if __name__ == "__main__":
    fs = FewShotPosts()

    # Debug (IMPORTANT)
    print("Available tags:", fs.get_tags())
    print("Available languages:", fs.df['language'].unique())
    print("Available lengths:", fs.df['length'].unique())

    # TEST FILTER
    posts = fs.get_filtered_posts("Short", "English", "Job Search")

    print("\nFiltered Posts Count:", len(posts))
    print(posts)
