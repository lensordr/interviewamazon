import streamlit as st
import pandas as pd
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Interview STAR Tool", layout="wide", page_icon="🎯")

st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #ffffff;}
    .stApp {background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);}
    h1 {color: #00d4ff; font-weight: 300; letter-spacing: 2px;}
    h2, h3 {color: #00d4ff; font-weight: 300;}
    p, label, div, span, li {color: #e0e0e0 !important;}
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff 0%, #0099cc 100%);
        color: #000; border: none; padding: 12px 32px;
        font-weight: 600; border-radius: 8px; transition: all 0.3s;
    }
    .stButton>button:hover {transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,212,255,0.4);}
    div[data-testid="stFileUploader"] {background-color: #1a1a2e; border-radius: 8px; padding: 20px;}
    .stDataFrame {background-color: #1a1a2e; border-radius: 8px;}
    textarea {background-color: #1a1a2e !important; color: #ffffff !important; border: 1px solid #00d4ff !important; font-size: 16px !important;}
    .stSelectbox > div > div {background-color: #1a1a2e !important; color: #ffffff !important; border: 1px solid #00d4ff !important;}
    .star-answer {background-color: #1a1a2e; padding: 24px; border-radius: 8px; border-left: 4px solid #00d4ff; color: #ffffff !important; font-size: 16px; line-height: 1.8; white-space: pre-wrap;}
</style>
""", unsafe_allow_html=True)

st.title("🎯 INTERVIEW STAR TOOL")
st.markdown("<p style='color: #888; font-size: 14px;'>AI-Powered STAR Method Answers | Amazon Leadership Principles</p>", unsafe_allow_html=True)
st.markdown("---")

if 'data' not in st.session_state:
    st.session_state.data = None

with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>📁 UPLOAD</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Excel or CSV", type=['xlsx', 'xls', 'csv'], label_visibility="collapsed")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            df.columns = ['Process', 'Description'] + list(df.columns[2:]) if len(df.columns) > 2 else ['Process', 'Description']
            st.session_state.data = df
            st.success(f"✅ {len(df)} experiences loaded")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error loading file: {e}")

if st.session_state.data is not None:
    st.markdown("<h3>💬 INTERVIEW QUESTION</h3>", unsafe_allow_html=True)
    question = st.text_area("Interview Question", height=100,
                            placeholder="e.g., Tell me about a time when you had to deal with a difficult stakeholder...",
                            label_visibility="collapsed")

    col1, col2 = st.columns([2, 1])
    with col1:
        leadership_principle = st.selectbox("Amazon Leadership Principle",
            ["Auto-detect", "Customer Obsession", "Ownership", "Invent and Simplify",
             "Are Right, A Lot", "Learn and Be Curious", "Hire and Develop the Best",
             "Insist on the Highest Standards", "Think Big", "Bias for Action",
             "Frugality", "Earn Trust", "Dive Deep", "Have Backbone; Disagree and Commit",
             "Deliver Results", "Strive to be Earth's Best Employer", "Success and Scale Bring Broad Responsibility"])
    with col2:
        generate_btn = st.button("🚀 GENERATE ANSWER", type="primary", use_container_width=True)

    st.markdown("---")

    if generate_btn:
        if not question:
            st.error("⚠️ Please enter a question")
        else:
            with st.spinner("🤖 Generating your STAR answer..."):
                context = "\n\n".join([f"Process: {row['Process']}\nDescription: {row['Description']}"
                                      for _, row in st.session_state.data.iterrows()])
                prompt = f"""Based on the following experiences, generate a compelling STAR method answer.

EXPERIENCES:
{context}

INTERVIEW QUESTION: {question}
{"LEADERSHIP PRINCIPLE: " + leadership_principle if leadership_principle != "Auto-detect" else ""}

Generate a structured STAR answer:
- Situation: Set the context
- Task: Describe your responsibility
- Action: Explain what YOU did (be specific)
- Result: Share the outcome with metrics if possible

Make it concise, impactful, and aligned with Amazon Leadership Principles. Use first-person perspective."""

                try:
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    answer = response.choices[0].message.content
                    st.markdown("<h3 style='color: #00d4ff;'>📝 YOUR STAR ANSWER</h3>", unsafe_allow_html=True)
                    st.markdown(f"<div class='star-answer'>{answer}</div>", unsafe_allow_html=True)
                    st.download_button("💾 DOWNLOAD", answer, file_name="star_answer.txt", mime="text/plain")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    st.markdown("---")
    st.markdown("<h3>📋 YOUR EXPERIENCES</h3>", unsafe_allow_html=True)
    st.dataframe(st.session_state.data, use_container_width=True, height=300)
else:
    st.markdown("""
    <div style='text-align: center; padding: 60px 20px;'>
        <h2 style='color: #00d4ff; font-size: 48px;'>👈</h2>
        <h3 style='color: #00d4ff;'>Upload Your Experiences</h3>
        <p style='color: #888; font-size: 16px; margin-top: 20px;'>
            Prepare an Excel or CSV file with:<br>
            <strong>Column A:</strong> Process/Project name<br>
            <strong>Column B:</strong> Description of your work
        </p>
    </div>
    """, unsafe_allow_html=True)
