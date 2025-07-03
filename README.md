
---

````markdown
# 📄 RAG Document Q&A with 🦙 Ollama + 🧠 Groq + Streamlit

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** app built using **LangChain**, **Groq’s LLaMA3-8B**, and **Ollama embeddings**. Users can upload research PDFs, create a vector database, and ask questions with LLM-powered accurate answers.

---

## 📺 Demo

▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)  
<!-- Replace with your actual demo link -->

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
````

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/rag-document-ollama.git
cd rag-document-ollama
```

### 2️⃣ Create a virtual environment

```bash
uv venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3️⃣ Install Requirements

```bash
uv pip install -r requirements.txt
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

I'm currently a **final-year MCA student** and an **aspiring Machine Learning Engineer**. I'm passionate about building real-world applications with **GenAI, LangChain, RAG pipelines**, and **LLMs**.

📌 Actively looking for roles in:
📊 Data Science • 🧠 LLM Engineering • 🤖 NLP / GenAI • ⚙️ MLOps

🔗 [LinkedIn](https://www.linkedin.com/in/yourname)
🌐 [Portfolio](https://yourwebsite.com)

---

## 🚀 Future Enhancements

* 🧠 Add memory or feedback loop to improve response quality
* 🌍 Deploy on Streamlit Cloud, Hugging Face Spaces, or GCP
* 🧾 Add PDF title summarization & multi-file context management

---

⭐ If you like this project, give it a **star** and feel free to fork it to make it your own!

```

---

✅ Be sure to replace:
- `https://www.youtube.com/watch?v=dQw4w9WgXcQ` → your actual demo link  
- `yourusername` → your GitHub username  
- `your_groq_api_key`, `your_langchain_api_key` → your actual API keys (in `.env`, never commit!)  
- `https://www.linkedin.com/in/yourname` → your LinkedIn  
- `https://yourwebsite.com` → your personal website (optional)

Would you like me to generate all your readme thumbnails (banner or preview image) or help you deploy this?
```
