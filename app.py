import streamlit as st
from dotenv import load_dotenv
import os
import re
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGEL_API_KEY")

# Configure Google Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Prompt for summarization
prompt = """Please summarize this video transcript:\n\n"""

# Extract YouTube video ID from URL
def extract_youtube_video_id(url):
    regex = r"(?:v=|\/|be\/)([0-9A-Za-z_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None

# Get transcript from YouTube
def extract_transcript_details(video_url):
    video_id = extract_youtube_video_id(video_url)
    if not video_id:
        raise ValueError("Could not extract video ID from the URL.")
    
    yt_api = YouTubeTranscriptApi()
    full_text = " ".join([t.text for t in yt_api.fetch(video_id)])
    return full_text


# Generate summary using Gemini
def generate_gemini_summary(transcript):
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt + transcript)
    return response.text

# -------------------- Streamlit UI ----------------------

st.set_page_config(page_title="YouTube Video Summarizer", layout="centered")

st.title("🎬 YouTube Video Summarizer using Gemini AI")

video_url = st.text_input("Enter YouTube video URL:")

if st.button("Summarize Video"):
    if not video_url:
        st.warning("⚠️ Please enter a YouTube video URL.")
    else:
        try:
            with st.spinner("Fetching transcript and generating summary..."):
                transcript = extract_transcript_details(video_url)
                summary = generate_gemini_summary(transcript)
                st.success("✅ Summary generated successfully!")
                st.subheader("📄 Summary")
                st.write(summary)
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

