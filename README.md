# 📄 RAG Document Q&A with 🦙 Ollama + 🧠 Groq + Streamlit

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** app built using **LangChain**, **Groq’s LLaMA3-8B**, and **Ollama embeddings**. Users can upload research PDFs, create a vector database, and ask questions with LLM-powered accurate answers.

Built with ❤️ by **Jatin**.

---

## 📺 Demo

▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=dQS3hz9lra0&list=PLe-YIIlt-fbO3hXVoaPK56ikWRT0A9Gzr&index=6&ab_channel=Jatin)  


---

## 🧩 Key Features

- 🔍 Upload & query research papers (PDFs)
- 🦙 Uses `all-minilm` Ollama embeddings
- ⚡ Powered by `LLaMA3-8B` via Groq API
- 🧠 Implements RAG with LangChain chaining
- 🖥️ Streamlit UI for real-time question answering

---

## 📁 Project Structure

```plaintext
.
├── app.py                  # Main Streamlit app
├── research_papers/        # Folder for user PDFs
├── .env                    # Environment variables
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/jatinydav557/RAG-document-ollama.git
cd RAG-document-ollama
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up `.env` file

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=chatbot-ollama
```

### 5️⃣ Place your PDFs

Put all your PDFs inside the `research_papers/` folder.

### 6️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Workflow

1. 🔍 Click **"Build Vector Database"**
2. 💬 Ask any question related to the uploaded papers
3. ✅ Get an accurate, context-aware answer from the LLM
4. 📄 View matched PDF chunks used to answer

---

## 📦 Requirements

```
streamlit
python-dotenv
langchain
langchain-community
langchain-openai
langchain-groq
langchain-ollama
faiss-cpu
pypdf
```

---

## 🙋‍♂️ About Me

I'm **Jatin**, a final-year MCA student and an aspiring **Machine Learning Engineer** passionate about building **real-world AI apps** with **LangChain**, **RAG pipelines**, and **LLMs**.

Currently building 20+ GenAI projects to showcase end-to-end engineering skills in:

- 📊 Data Science
- 🧠 LLM Engineering
- 🤖 NLP / GenAI
- ⚙️ MLOps & Deployment

---

## 🧩 Let's Connect

- **💼 LinkedIn:** [linkedin.com/in/jatin557](https://www.linkedin.com/in/jatin557)
- **📦 GitHub:** [github.com/jatinydav557](https://github.com/jatinydav557)
- **📬 Email:** [jatinydav557@gmail.com](mailto:jatinydav557@gmail.com)
- **📱 Phone:** [+91-7340386035](tel:+917340386035)
- **🎥 YouTube:** [Watch More Projects](https://www.youtube.com/@jatinML/playlists)

---

## 🚀 Future Enhancements

- 🧠 Add memory or feedback loop to improve response quality  
- 🌍 Deploy on Streamlit Cloud, Hugging Face Spaces, or GCP  
- 🧾 Add PDF title summarization & multi-file context management  

---

⭐ If you like this project, give it a **star** and feel free to fork it to make your own version!

> “You're one project away from your dream role — so build boldly.”

