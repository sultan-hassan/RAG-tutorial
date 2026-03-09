# Deploying to Hugging Face Spaces

Want to share your Astronomy AI with the world? You can host this app for free on Hugging Face Spaces. Follow these steps!


## 🛰️ Step 1: Create your Space

1- Login to Hugging Face.
2- Click on your profile picture (top right) and select "New Space".
3- Space Name: Give it a cool name (e.g., cosmic-insight-ai).
4- SDK: Select Gradio.
5- Space Hardware: Choose "CPU Basic (Free)".
6- Visibility: Public.
7- Click "Create Space".


## 📂 Step 2: Upload your Files

Once your Space is created, you will see a page with instructions. You can upload files directly through the browser:


1- Click the "Files" tab at the top.
2- Click "Add file" -> "Upload files".
3- Drag and drop the app.py and requirements.txt from your local gradio_app folder.
4- Scroll down and click "Commit changes to main".


## 🔑 Step 3: Add your Groq Secret Key

Crucial: Never hardcode your API key in app.py. Hugging Face provides a secure way to store secrets.

1- In your Space, click the "Settings" tab (at the top).
2- Scroll down to "Variables and secrets".
3- Click "New secret".
4- Name: groq_api_keys
5- Value: (Paste your gsk_... key here).
6- Click "Save".


## ⏳ Step 4: Build & Run

1- Click back to the "App" tab.
2- Hugging Face will automatically detect your requirements.txt, install the libraries, and start the app.
3- First Run: It will take sometime to download the embedding model and index the ArXiv papers.
4- Once finished, your AI will be live!


