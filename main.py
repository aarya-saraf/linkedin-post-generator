import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# -----------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
tone_options = ["Professional", "Funny", "Motivational", "Storytelling"]


@st.cache_resource
def load_fs():
    return FewShotPosts()


def main():
    st.title("🚀 AI LinkedIn Post Generator")
    st.caption("Generate viral LinkedIn posts using AI in seconds")

    fs = load_fs()
    tags = fs.get_tags()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    with col4:
        selected_tone = st.selectbox("Tone", options=tone_options)

    # -----------------------------
    # GENERATE BUTTON
    # -----------------------------
    if st.button("Generate"):
        try:
            with st.spinner("Generating posts..."):
                posts = generate_post(
                    selected_length,
                    selected_language,
                    selected_tag,
                    selected_tone
                )

                for i, post in enumerate(posts):
                    st.markdown(f"### ✨ Variation {i + 1}")
                    st.code(post)   # ✅ CLEAN COPYABLE OUTPUT

                    # Regenerate button
                    if st.button(f"🔁 Regenerate Variation {i + 1}"):
                        new_post = generate_post(
                            selected_length,
                            selected_language,
                            selected_tag,
                            selected_tone
                        )[0]
                        st.success(new_post)

        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
