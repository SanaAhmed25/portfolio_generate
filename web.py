import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import zipfile
import os
from pypdf import PdfReader

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_icon="@", page_title="Website Creator")

st.title(":rainbow[Website Creator]")

# ---------------- PDF UPLOADER ----------------
uploaded_pdf = st.file_uploader(
    "Upload a PDF (optional – content will be used for website generation)",
    type=["pdf"]
)

def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

pdf_text = ""
if uploaded_pdf:
    pdf_text = read_pdf(uploaded_pdf)
    st.success("PDF uploaded and read successfully!")

# ---------------- USER PROMPT ----------------
prompt = st.text_area("Enter detail for your website")

# ---------------- GENERATE ----------------
if st.button("Generate"):
    with st.spinner("Generating... Please wait"):

        final_prompt = f"""
USER WEBSITE REQUIREMENTS:
{prompt}

PDF CONTENT (USE THIS AS REFERENCE IF PROVIDED):
{pdf_text}
"""

        message = [(
            "system",
            """
You are a Senior Frontend Engineer with 10+ years experience.
Your task: Generate a complete mini-website from the user's description.

OUTPUT FORMAT (must follow exactly):

--html--
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Generated Website</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<!-- HTML CONTENT HERE -->

<script src="script.js"></script>
</body>
</html>
--html--

--css--
/* CSS CODE ONLY */
--css--

--js--
// JavaScript CODE ONLY
--js--

RULES (VERY STRICT):
1. NEVER mix HTML, CSS, and JS.
2. NEVER output Markdown.
3. ALWAYS include CSS & JS links.
4. NO text outside the 3 blocks.
5. Clean, responsive, modern UI.
            """
        )]

        message.append(("user", final_prompt))

        brain = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=1
        )

        response = brain.invoke(message)

        def part(text, key):
            return text.split(f"--{key}--")[1].strip()

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(part(response.content, "html"))

        with open("style.css", "w", encoding="utf-8") as f:
            f.write(part(response.content, "css"))

        with open("script.js", "w", encoding="utf-8") as f:
            f.write(part(response.content, "js"))

        with zipfile.ZipFile("website.zip", "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

        st.download_button(
            "⬇ Download Website ZIP",
            data=open("website.zip", "rb"),
            file_name="website.zip"
        )

        st.success("Website generated successfully 🚀")
