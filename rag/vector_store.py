import chromadb
import os

repo_path = "E:/Fall 26-27/enterprise-ai-assistant/data"

client = chromadb.PersistentClient(os.path.normpath(os.path.join(repo_path, "..", "chroma_db")))
collection = client.get_or_create_collection(name="codebase")
print(client)

def store_embedding(id_counter,embedding,chunk,department,file_name):
    collection.add(
            ids=[str(id_counter)],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "department": department,
                "source": file_name
            }]
        )