# Multiple PDF Chat Application Using RAG Architecture with LangChain

## Overview

This project is a **Multiple PDF Chat Application** that allows users to interact with and query multiple PDF documents through a chat interface. It leverages **Retrieval-Augmented Generation (RAG)** architecture to provide accurate and contextually relevant responses by retrieving information from the PDF content and generating answers using a language model.

The application is implemented in **Python** using the **LangChain** framework, which simplifies building applications with LLMs and retrieval components.

---

## Features

- Load and process multiple PDF documents
- Extract text and embed content for efficient retrieval
- Use a vector store for fast similarity search over the PDFs
- Query the documents through a chat interface
- Use RAG architecture combining retrieval and generation for precise answers
- Easy to extend for other document types or LLM providers

---

## Technologies Used

- Python 3.x
- LangChain
- FAISS / Chroma / Other vector stores (specify which you used)
- OpenAI / HuggingFace / Other LLM APIs (specify your model/provider)
- PyPDF2 / pdfplumber / other PDF parsers

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables (e.g., OpenAI API key):
    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    ```

---

## Usage

1. Add your PDF files in the `pdfs/` directory (or specify your directory).

2. Run the application:
    ```bash
    python app.py
    ```

3. Interact with the chat interface in the terminal or web UI (if implemented).

---

## Project Structure

