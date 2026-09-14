from openai import OpenAI 

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

def generate_embedding(data):
    return client.embeddings.create(
        model="text-embedding-nomic-embed-text-v1.5",
        input=data
    )