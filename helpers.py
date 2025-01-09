import os
from typing import Dict
import weaviate

def create_client() -> weaviate.WeaviateClient:
    openai_key = os.getenv("OPENAI_APIKEY") 
    anthropic_key = os.getenv("ANTHROPIC_APIKEY") 

    if not openai_key or not anthropic_key:
        raise ValueError("OPENAI_APIKEY or ANTHROPIC_APIKEY is not set")

    headers: Dict[str, str] = {
        "X-OpenAI-Api-Key": openai_key,
        "X-Anthropic-Api-Key": anthropic_key,
    }

    client = weaviate.connect_to_local(headers=headers)
    return client