import sys
import os

backend_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(backend_dir)

sys.path.insert(0, root_dir)
sys.path.insert(0, os.path.join(root_dir, "app", "rag"))

from app.rag.retriever import retriever

async def rag_retrieve(query,role):
    res = retriever(query,role)
    return res
