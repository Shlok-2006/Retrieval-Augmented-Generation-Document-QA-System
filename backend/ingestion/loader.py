from pypdf import PdfReader
import os

def load_documents(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            documents.append({"text": text, "source": file})

        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.append({"text": f.read(), "source": file})

    return documents
