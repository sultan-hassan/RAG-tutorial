# RAG-tutorial

A tutorial on building a Retrieval-Augmented Generation (RAG) system using Groq (Llama 3.1), LangChain, and Gradio.

## 🚀 Setup Instructions

### 1. Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (The fastest Python manager).
- Get a free API Key from [Groq Cloud](https://console.groq.com/).

### 2. Clone the Repository

```bash
git clone https://github.com/sultan-hassan/RAG-tutorial.git
cd RAG-tutorial
```
### 3. Initialize the Environment
Using uv, you don't need to manually create a virtual environment. Run the following command to automatically install all required packages (Pandas, LangChain, Gradio, etc.):

```bash
uv sync
```

### 4. Configure Your API Key
To keep your API key secure, create a file named .env in the root folder of this project:

```bash
touch .env
```

Open the .env file and paste your Groq key:

```text
groq_api_keys=your_gsk_key_here
```
