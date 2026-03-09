# Deploying to Hugging Face Spaces

Want to share your Astronomy AI with the world? You can host this app for free on Hugging Face Spaces. Follow these steps!


## 🛰️ Step 1: Create your Space

- Login to Hugging Face.
- Click on your profile picture (top right) and select "New Space".
- Space Name: Give it a cool name (e.g., cosmic-insight-ai).
- SDK: Select Gradio.
- Space Hardware: Choose "CPU Basic (Free)".
- Visibility: Public.
- Click "Create Space".


## 📂 Step 2: Upload your Files

Once your Space is created, you will see a page with instructions. You can upload files directly through the browser:


- Click the "Files" tab at the top.
- Click "Add file" -> "Upload files".
- Drag and drop the app.py and requirements.txt from your local gradio_app folder.
- Scroll down and click "Commit changes to main".


## 🔑 Step 3: Add your Groq Secret Key

Crucial: Never hardcode your API key in app.py. Hugging Face provides a secure way to store secrets.

- In your Space, click the "Settings" tab (at the top).
- Scroll down to "Variables and secrets".
- Click "New secret".
- Name: groq_api_keys
- Value: (Paste your gsk_... key here).
- Click "Save".


## ⏳ Step 4: Build & Run

- Click back to the "App" tab.
- Hugging Face will automatically detect your requirements.txt, install the libraries, and start the app.
- First Run: It will take sometime to download the embedding model and index the ArXiv papers.
- Once finished, your AI will be live!


### Once deployed, you should see a similar RAG app like this: https://huggingface.co/spaces/sultan-hassan/RAG-tutorial-light