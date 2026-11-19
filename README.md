# RAG-Based Teaching AI Assistant

This project is a **Retrieval-Augmented Generation (RAG) Based Teaching AI Assistant**, developed using educational video content from the Love Babbar operating sysytem course on YouTube.

**Course Playlist:**  
https://youtube.com/playlist?list=PLDzeHZWIZsTr3nwuTegHLa2qlI81QweYG&si=lyiC1NqgoRlDLBFj

The project processes educational videos, converts their content into text, generates embeddings, stores information in chunks, and retrieves relevant content to answer users' questions.

If you want to use this project with your own videos, follow the setup and execution instructions below.

## 1. Prerequisites

Make sure you have installed the following software:

- Python 3.10 or above
- Git
- Visual Studio Code (recommended)
- Ollama
- An internet connection for downloading models and installing dependencies

## 2. Project Setup

**Step 1: Clone the repository**

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd <PROJECT_FOLDER>
```

**Step 2: Create a virtual environment**

```bash
python -m venv djangoenv
```

Activate the virtual environment on Windows:

```powershell
djangoenv\Scripts\activate
```

For Linux/macOS:

```bash
source djangoenv/bin/activate
```

**Step 3: Install dependencies**

If a `requirements.txt` file is available, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages individually according to your project imports.

## 3. Ollama Setup

This project uses Ollama for locally running language and embedding models.

1. Download and install Ollama from https://ollama.com/
2. Open your terminal.
3. Download the required models:

```bash
ollama pull deepseek-r1
ollama pull bge-m3
```

4. Ensure Ollama is running before executing the project.

**Note:** The DeepSeek model is used for generating responses, while BGE-M3 is used for generating text embeddings. Make sure the model names match your project configuration.

## 4. Video Processing and Execution Order

If you want to process your own educational videos, place them in the appropriate input directory used by the project.
ensure your video format follow this order
Lecture-number_Title.mp3
for ex-
Lecture-01_operating system.mp3

Run the following Python files in the exact order:

| Order | Python file | Purpose |
|---|---|---|
| 1 | `process_vedio.py` | Processes video files and extracts audio/transcription data |
| 2 | `create_chunks.py` | Divides extracted text into smaller chunks |
| 3 | `Read_chunks.py` | Reads chunks and generates/stores embeddings |
| 4 | `process_incoming.py` | Processes incoming user queries using the RAG pipeline |

Execute each file completely before running the next one.

**Execution commands:**

```bash
python process_vedio.py
python create_chunks.py
python Read_chunks.py
python process_incoming.py
```

## 5. Important Instructions

- Before starting a new video-processing session, delete all existing generated files from the `json` folder.
- Ensure that your input videos are placed in the correct directory.
- Do not change the execution order of the Python files.
- Make sure Ollama is running before generating embeddings or querying the assistant.
- Ensure that the required embedding and language models are downloaded.
- Do not delete source videos, Python scripts, configuration files, or other required project resources when cleaning generated data.

## 6. Troubleshooting

**Issue: Ollama connection error**

- Ensure Ollama is installed and running.
- Check whether the Ollama API is accessible at `http://localhost:11434`.
- Verify that the required models are downloaded.

**Issue: Module not found**

Run:

```bash
pip install -r requirements.txt
```

**Issue: Old or duplicate data**

- Clean the generated files inside the `json` folder.
- Run the processing pipeline again in the specified order.

## 7. Starting the Project

After completing the setup and video-processing steps, execute:

```bash
python process_incoming.py
```

You can now interact with the RAG-Based Teaching AI Assistant and ask questions about the processed educational video content.
