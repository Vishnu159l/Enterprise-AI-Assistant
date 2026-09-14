from document_loader import get_files_content
from chunker import chunk_text
from vector_store import store_embedding
from embeddings import generate_embedding

repo_path = "E:/Fall 26-27/enterprise-ai-assistant/data"

file_content = get_files_content(repo_path)

id_counter = 0

for file in file_content:
    chunks = chunk_text(file["content"])
    for chunk in chunks:
        response = generate_embedding(chunk)
        embedding = response.data[0].embedding
        store_embedding(id_counter,embedding,chunk,file["department"],file["source"])
        id_counter += 1
print("Stored successfully!")