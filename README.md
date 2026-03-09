# Interview Preparation Tool - STAR Method

A web-based tool to generate STAR-method interview answers based on your experiences, aligned with Amazon Leadership Principles.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get a FREE API key:
   - **Google Gemini**: https://makersuite.google.com/app/apikey (FREE, no credit card needed)

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Prepare your data file** (Excel or CSV):
   - Column A: Process/Project name
   - Column B: Description of your work

2. **Upload the file** via the sidebar

3. **Enter an interview question**

4. **Select a Leadership Principle** (optional)

5. **Generate STAR answer** - The AI will create a structured response based on your experiences

## Example Data Format

| Process | Description |
|---------|-------------|
| Cloud Migration | Led migration of 50+ microservices to AWS, reduced infrastructure costs by 30% |
| Customer Portal | Designed and implemented self-service portal, decreased support tickets by 45% |
| Team Leadership | Managed team of 5 engineers, delivered 3 major releases on time |

## Features

- Upload Excel/CSV files
- AI-powered STAR answer generation
- Amazon Leadership Principles alignment
- Download generated answers
- Clean, intuitive interface

## Notes

- Keep descriptions specific with metrics when possible
- The more detailed your experiences, the better the generated answers
- API key is not stored and only used for the current session
