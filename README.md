# **Question-Answer Generation System**

---

## **Overview**
The **Question-Answer Generation System** is a FastAPI-based web application that processes uploaded PDF files, generates questions and answers based on the content, and saves the results in a CSV file. The system leverages the `langchain` library for natural language processing (NLP) tasks, including question generation, answer retrieval, and text summarization. It uses OpenAI's GPT models for generating high-quality questions and answers.

This project is ideal for educational purposes, such as creating study materials, exam preparation, or syllabus-based assessments.

---

## **Features**
1. **PDF Upload**:
   - Users can upload PDF files containing subject-specific content.
   - The system validates the uploaded file and stores it locally.

2. **Dynamic Question Generation**:
   - Generates four types of questions:
     - Long-answer questions
     - Short-answer questions
     - Fill-in-the-blank questions
     - Multiple-choice questions
   - The number of questions for each type is configurable by the user.

3. **Answer Retrieval**:
   - Uses embeddings and vector search to retrieve accurate answers for the generated questions.

4. **CSV Output**:
   - Saves the generated questions and answers in a structured CSV file for easy access and sharing.

5. **Asynchronous Processing**:
   - Supports long-running tasks without blocking the API.

6. **Frontend Integration**:
   - Provides a simple HTML interface for uploading files and viewing results.

---

## **Technologies Used**
- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **NLP Library**: [LangChain](https://python.langchain.com/)
- **OpenAI Models**: GPT-3.5-turbo
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **PDF Processing**: PyPDFLoader (from LangChain) and PyPDF2
- **File Storage**: Static file handling with FastAPI's `StaticFiles`
- **Frontend Templating**: Jinja2Templates
- **Deployment**: Uvicorn (ASGI server)

---

## **Installation and Setup**

### **Prerequisites**
1. Python 3.8 or higher
2. OpenAI API Key
3. Redis (optional, for asynchronous task queues)

### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/UppalaAravind28/Question_Answering
   cd question-answer-generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the Application**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn app:app --host=localhost --port=8000 --reload
   ```

5. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://localhost:8000/
   ```

---

## **API Endpoints**

### **1. Upload PDF**
- **Endpoint**: `/upload`
- **Method**: POST
- **Description**: Uploads a PDF file and stores it locally.
- **Request Body**:
  - `pdf_file`: The PDF file to be uploaded.
  - `filename`: Name of the file.
  - `subject`: Subject name (e.g., "Mathematics").
  - `Lqno`: Number of long-answer questions.
  - `Sqno`: Number of short-answer questions.
  - `Fqno`: Number of fill-in-the-blank questions.
  - `Mqno`: Number of multiple-choice questions.
- **Response**:
  ```json
  {
    "msg": "success",
    "pdf_filename": "static/docs/example.pdf"
  }
  ```

---

### **2. Analyze PDF**
- **Endpoint**: `/analyze`
- **Method**: POST
- **Description**: Processes the uploaded PDF, generates questions and answers, and saves them in a CSV file.
- **Request Body**:
  - `pdf_filename`: Path to the uploaded PDF file.
- **Response**:
  ```json
  {
    "output_file": "static/output/QA.csv"
  }
  ```

---

## **Folder Structure**
```
question-answer-generator/
├── app.py                # Main FastAPI application
├── static/
│   ├── docs/             # Uploaded PDF files
│   └── output/           # Generated CSV files
├── templates/
│   └── index.html        # Frontend template
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
```

---

## **How It Works**

### **Step 1: File Upload**
- The user uploads a PDF file via the `/upload` endpoint.
- The backend validates the file and stores it in the `static/docs/` directory.

### **Step 2: Question Generation**
- The system processes the PDF using `PyPDFLoader` to extract text.
- The text is split into chunks and passed to the `QAGenerationChain` for question generation.
- A dynamic prompt template is used to generate questions based on the specified counts (`Lqno`, `Sqno`, etc.).

### **Step 3: Answer Retrieval**
- The system creates embeddings for the text chunks and stores them in a FAISS vector store.
- For each generated question, the system retrieves the most relevant answer using the `RetrievalQA` chain.

### **Step 4: Save Results**
- The generated questions and answers are saved in a CSV file located in the `static/output/` directory.

---

## **Example Workflow**

1. **Upload PDF**:
   - Send a POST request to `/upload` with the following payload:
     ```json
     {
       "pdf_file": <binary_data>,
       "filename": "example.pdf",
       "subject": "Physics",
       "Lqno": 5,
       "Sqno": 10,
       "Fqno": 15,
       "Mqno": 20
     }
     ```

2. **Analyze PDF**:
   - Send a POST request to `/analyze` with the following payload:
     ```json
     {
       "pdf_filename": "static/docs/example.pdf"
     }
     ```

3. **Download CSV**:
   - The response will include the path to the generated CSV file:
     ```json
     {
       "output_file": "static/output/QA.csv"
     }
     ```

---

## **Sample CSV Output**
The generated CSV file will have the following structure:

| Question                          | Answer                              |
|-----------------------------------|-------------------------------------|
| What is Newton's First Law?       | An object remains at rest...        |
| Define acceleration.              | Rate of change of velocity...       |
| Fill in the blank: Force = ___    | Mass × Acceleration                 |
| Which law explains inertia?       | a) Newton's First Law...            |

---

## **Future Enhancements**
1. **Support for Other File Formats**:
   - Extend support to DOCX, TXT, and other document formats.

2. **Advanced NLP Models**:
   - Use more advanced models like GPT-4 for better accuracy.

3. **User Authentication**:
   - Add login functionality to secure the application.

4. **Real-Time Updates**:
   - Use WebSocket or SSE for real-time progress updates.

5. **Scalability**:
   - Deploy on cloud platforms (AWS, GCP, Azure) with load balancing.
---

## **Contact**
For questions or feedback, please contact:
- Email: aravind.uppala2002@gmail.com
- GitHub: [GitHub Profile](https://github.com/UppalaAravind28)

---

Thank you for using the **Question-Answer Generation System**!
