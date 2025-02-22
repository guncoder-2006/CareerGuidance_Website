# Career Guidance Web App

## Overview
This **Career Guidance Web App** helps users explore career options based on their skills, interests, and certifications. It utilizes **Flask** for the backend and integrates **Google Gemini AI** to generate personalized career recommendations.

## Features
- **User Input Form** – Collects user details like skills, interests, and certifications.
- **AI-Powered Recommendations** – Uses Google Gemini AI to generate career suggestions.
- **Modern UI** – Built with **HTML, Tailwind CSS, and JavaScript** for a smooth user experience.
- **Flask Backend** – Processes user input and interacts with the AI model.

## Technologies Used
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Flask (Python)
- **AI Integration:** Google Gemini API

## Installation
### Prerequisites
- Python installed
- Flask installed (`pip install flask`)
- Google Gemini API client (`pip install google-genai`)
- Requests library (`pip install requests`)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/career-guidance-app.git
   cd career-guidance-app
   ```
2. Install dependencies:
   ```sh
   pip install flask google-genai requests
   ```
3. Set up your API key in `app.py`:
   ```python
   client = genai.Client(api_key="YOUR_API_KEY")
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
5. Open the browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter your skills, interests, and certifications in the form.
2. Click **Submit** to receive career suggestions from the AI.
3. View recommendations and explore career options.

