# 🚀 LinkedIn Post Generator (AI Powered)

An AI-powered application that generates high-quality LinkedIn posts using Large Language Models (LLMs) via Groq API. It supports multiple tones, languages, and post lengths with few-shot learning for better output quality.

## 📌 Features

- ✨ AI-powered LinkedIn post generation  
- 🔁 Multiple variations of posts  
- 🎯 Custom inputs:
  - Topic / Tag selection  
  - Length control (Short / Medium / Long)  
  - Language (English / Hinglish)  
  - Tone selection (Professional, Motivational, Funny, Storytelling)  
- 🧠 Few-shot learning for style-based generation  
- 🎨 Streamlit UI for interaction  
- ⚡ Fast responses using Groq API  

## 🧠 Tech Stack

- Python  
- Streamlit  
- LangChain  
- Groq API  
- Pandas  
- JSON  

## 📂 Project Structure

```
linkedin-post-generator/
├── main.py
├── post_generator.py
├── llm_helper.py
├── few_shot.py
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Create virtual environment (optional)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```
GROQ_API_KEY=your_api_key_here
```

### 5. Run project
```bash
streamlit run main.py
```

## 🧪 Example Output

Input:
Topic: Job Search  
Language: English  
Length: Medium  

Output:
Job searching can feel overwhelming, but every rejection teaches you something. Stay consistent, improve your skills, and keep moving forward. Your opportunity is coming.

## 🔐 Security

- `.env` file is ignored using `.gitignore`  
- API keys are never pushed to GitHub  
- Regenerate keys if exposed  

## 🚀 Future Improvements

- Viral score prediction  
- Post scheduling system  
- AI image generation for posts  
- Engagement prediction  

## 👨‍💻 Author

Aarya Saraf

## ⭐ Support

If you like this project:
- Star the repo ⭐  
- Fork it 🍴  
- Share it 🚀
