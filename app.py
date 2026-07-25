from google import genai
import streamlit as st
from dotenv import load_dotenv
import os


# Load API Key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# Gemini Client
client = genai.Client(api_key=api_key)


# Streamlit UI

st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    page_icon="📝"
)


st.title("📝 AI Meeting Minutes Generator Agent")

st.write(
    "Convert raw meeting transcripts into professional structured meeting minutes using AI."
)


# User Input

meeting_notes = st.text_area(
    "Paste your meeting transcript / notes here:",
    height=300,
    placeholder="Example: Team discussed project progress..."
)



# Generate Button

if st.button("Generate Meeting Minutes"):

    if meeting_notes:

        prompt = f"""
You are an AI Meeting Minutes Generator.

Convert the following meeting transcript into professional meeting minutes.

Generate the output in this format:

1. Meeting Summary:
- Provide a short overview.

2. Key Discussion Points:
- List important topics discussed.

3. Decisions Made:
- Mention final decisions.

4. Assigned Responsibilities:
- Mention person and assigned task.

5. Deadlines:
- Extract deadlines and dates.

6. Future Action Items:
- List upcoming tasks.

7. Next Meeting Details:
- Mention if available.

Meeting Transcript:

{meeting_notes}

Make the response clear, professional and easy to read.
"""


        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )


        st.subheader("Generated Meeting Minutes")

        st.write(response.text)


    else:

        st.warning(
            "Please enter meeting notes before generating."
        )