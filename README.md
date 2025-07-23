# 🎬 YouTube Video Summarizer using Google Gemini & Streamlit

This project is a modern AI-powered Streamlit web application that allows users to **generate summaries** of any public YouTube video. It extracts the video's transcript and summarizes it using **Google's Gemini (Generative AI)** model.

---

## 🚀 Features

- ✅ Enter any valid YouTube video URL
- ✅ Automatically extracts transcript using `youtube-transcript-api`
- ✅ Summarizes the transcript using **Gemini 2.0 Flash** via `google-generativeai`
- ✅ Beautiful UI built with **Streamlit**
- ✅ Clear error handling and progress indicators

---

## 📸 Demo

> 📷 **Screenshot Preview of the App**
> <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/652b69ec-6e81-41d6-a049-894794b08f72" />



---

## 🔧 Tech Stack

| Tool               | Purpose                                   |
|--------------------|-------------------------------------------|
| `Streamlit`        | Frontend UI for user interaction          |
| `Google Generative AI` | To summarize extracted transcript via Gemini |
| `YouTube Transcript API` | Extract transcript from YouTube videos     |
| `Python-dotenv`    | Securely load Google API key              |
| `Regex`            | Extract video ID from any URL format      |

---

## 🛠️ How It Works

1. **User enters YouTube URL**
2. Application extracts `video_id` using regex
3. `youtube-transcript-api` fetches the full transcript
4. `Gemini 2.0 Flash` model summarizes the transcript
5. Summary is shown to the user in a clean format

---

## 💻 How to Run Locally

## 1. Clone this repository:

   ```bash
   git clone https://github.com/RajaSuhashKesari/Youtube-Video-Summarize-Application-using-Gemini.git
   cd Youtube-Video-Summarize-Application-using-Gemini
```
## 2. Create and activate your Conda environment:

   ```bash
conda create --name venvforgenai python=3.10
conda activate venvforgenai
```
## 3. Install dependencies:

   ```bash
pip install -r requirements.txt
```
## 4. Add your Google API Key in .env file:
   ```bash
GOOGEL_API_KEY=your_api_key_here
```
## 5. Run the Streamlit app:
   ```bash
streamlit run app.py
```
## **📄 Sample Output**
> <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/58722864-8168-40c6-8154-641663447b4c" />
📄 Summary
This video transcript outlines the five core skills a product data scientist needs to land their first job,
ranked on a three-star mastery scale. These skills are:
1. SQL: Extracting and manipulating data from databases. Mastery levels range from simple queries (1
star) to complex, optimized code with window functions (3 stars). The key is practice using resources
like DataLemur or StrataScratch.
2. Python: For data manipulation and statistical calculations, especially in experimentation (A/B testing).
Focus on fundamentals like objects and functions before diving into Kaggle to analyze and understand
others' code. Mastery progresses from basic data frame operations (1 star) to error-free code and the
ability to fully explain statistical metrics in A/B testing (3 stars).
3. Statistics: Understanding core statistical concepts like mean, standard deviation, and, mostimportantly, how to conduct and interpret A/B tests. StatQuest on YouTube is recommended. Masteryranges from knowing basic definitions (1 star) to designing experiments, drawing insights andcommunicating them effectively (3 stars).
4. Data Visualization: Creating clear and self-explanatory charts and dashboards using tools likeTableau, Looker, or Metabase. Focus on answering specific product questions with visuals. Masterygrows from creating default dashboards (1 star) to designing clean, self-explanatory dashboards (3stars).
5. Product Sense:Understanding product metrics and how data influences product strategy. Practicesolving product cases and get feedback from senior mentors. Mastery evolves from knowing coremetrics (1 star) to deeply understanding relevant metrics for specific domains (3 stars).
The video also mentions a "secret sixth skill": basic knowledge of machine learning algorithms,specifically linear and logistic regression. The key takeaways are to focus on practical application,especially through platforms like Kaggle, to understand others' code and seek mentorship to acceleratelearning and product sense. The speaker emphasizes that mastering these skills will position aspiring datascientists for success in securing their first role.

🧪 Example YouTube URLs
[https://www.youtube.com/watch?v=O2gerCxEXvc](https://youtu.be/h0JWKpN1Gro?si=AiG6elnSO9Ce3-9Q)

All valid YouTube formats are supported.

## 📁 File Structure
  ```bash
📦 youtube-summarizer-gemini
│
├── app.py                  # Streamlit application
├── .env                    # API key (not uploaded to GitHub)
├── requirements.txt        # All Python dependencies
└── README.md               # Project documentation
```

## 🛡️ Security
Your Google API key is stored securely using .env file and python-dotenv
.env is excluded from Git tracking via .gitignore
