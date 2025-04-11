

---

# **PulseBot**

![PulseBot](https://img.shields.io/badge/PulseBot-AI_Chatbot-blue?style=flat-square) ![Streamlit](https://img.shields.io/badge/Powered_By-Streamlit-green?style=flat-square) ![Gemini_API](https://img.shields.io/badge/API-Google_Gemini-orange?style=flat-square)

**PulseBot** is an intelligent AI-powered chatbot built using Google's Gemini API. Designed for real-time conversational interactions, PulseBot provides users with accurate, insightful, and engaging responses to their queries. Whether you're looking for answers, brainstorming ideas, or simply chatting, PulseBot is here to assist.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## **Overview**

PulseBot leverages **Google's Gemini API** to deliver a seamless conversational experience. Built on **Streamlit**, the app features a clean and intuitive interface with dynamic themes, error handling, and professional styling. It is ideal for developers, students, and professionals seeking a lightweight yet powerful AI chatbot solution.

---

## **Features**

- **Real-Time Conversations**: Instantly interact with the AI-powered chatbot.
- **Dynamic Themes**: Switch between Light and Dark modes for a personalized user experience.
- **Clear Conversation History**: Reset the chat history with a single click.
- **Professional Design**: Styled chat messages, icons, and a responsive footer for a polished look.
- **Error Handling**: Gracefully handles API errors and ensures a smooth user experience.
- **Sidebar Navigation**: Includes settings, an about section, and developer attribution.

---

## **Installation**

### **Prerequisites**
- Python 3.7 or higher
- A valid Google Gemini API key (sign up at [Google AI Studio](https://aistudio.google.com/))
- Streamlit installed (`pip install streamlit`)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/UppalaAravind28/PulseBot.git
   cd PulseBot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## **Configuration**

### **Environment Variables**
To securely store your API key, use environment variables:
- Add your Gemini API key to a `.env` file:
  ```env
  GEMINI_API_KEY=your_api_key_here
  ```
- Alternatively, set the environment variable in your terminal:
  ```bash
  export GEMINI_API_KEY=your_api_key_here  # macOS/Linux
  set GEMINI_API_KEY=your_api_key_here     # Windows
  ```

### **Customization**
- Modify the `chat_styles` CSS in `app.py` to customize the appearance of the chat interface.
- Update the footer in `app.py` to include your own branding or links.

---

## **Usage**

1. Launch the app by running:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser.
3. Type your question or message in the input box and press Enter.
4. The bot will respond in real-time, and the conversation history will be displayed.
5. Use the sidebar to:
   - Toggle between Light and Dark themes.
   - Clear the conversation history.
   - Access the **About** section for more information.

---

## **Deployment**

### **Streamlit Community Cloud**
1. Push your code to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign up.
3. Connect your GitHub repository and deploy the app.

### **Heroku**
1. Create a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```
2. Add a `Procfile`:
   ```
   web: streamlit run app.py
   ```
3. Deploy to Heroku using their CLI or GitHub integration.

### **Google Cloud Run**
1. Containerize your app using Docker.
2. Push the image to Google Container Registry.
3. Deploy the container to Google Cloud Run.

---

## **Contributing**

We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature or fix"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

Please ensure your contributions adhere to the project's coding standards and include appropriate documentation.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For inquiries, feedback, or collaboration, please reach out:

- **Developer**: Uppala Aravind  
- **Email**: [uppalaaravind28@gmail.com](mailto:uppalaaravind28@gmail.com)  
- **GitHub**: [@UppalaAravind28](https://github.com/UppalaAravind28)  
- **LinkedIn**: [Uppala Aravind](https://www.linkedin.com/in/uppala-aravind-28-lin/)  

---

## **Acknowledgments**

- Built using [Streamlit](https://streamlit.io/) for the frontend.
- Powered by [Google's Gemini API](https://ai.google.dev/).
- Inspired by open-source communities and innovative AI technologies.

---

