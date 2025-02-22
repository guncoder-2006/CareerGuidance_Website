from flask import Flask, request, render_template, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace with your Google API key
GOOGLE_API_KEY = "AIzaSyCtXkAqz7D8DZGasMZLb_TaecCzKTHftK4"

# Configure the Generative AI API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the GenerativeModel
model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def index():
    return render_template("index.html")  # Serve the HTML form

@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()  # Get JSON data from the request
        print("Received data:", data)  # Log the received data

        # Prepare the prompt
        prompt = f"""
        The user has the following details:
        - Name: {data.get('name')}
        - Skills: {data.get('skills')}
        - Interests: {data.get('interests')}
        - Certifications: {data.get('certifications')}

        Based on this information, suggest a structured career pathway that includes:
        1. Best Career Option (Job Title)
        2. Why it's Suitable (A brief explanation)
        3. Step-by-Step Guide (Numbered steps for progression)
        
        Ensure the response is concise, well-structured, and formatted for readability.dont add any asterick(*) signs
        """

        # Call Google Gemini API
        response = model.generate_content(prompt)

        if not response.text:
            raise ValueError("Empty response from AI")

        # Convert response text into structured JSON format
        career_options = response.text.replace("\n", "<br>")  # Preserve formatting for HTML display

        structured_response = {
            "status": "success",
            "message": career_options
        }

        print("Career options generated successfully.")
        return jsonify(structured_response)

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"status": "error", "message": f"Failed to fetch career options: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)