import requests, json
import logging
from weaviate.classes.config import Configure

from helpers import create_client
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = create_client()

client.collections.delete("Question")

questions = client.collections.create(
    name="Question",
    vectorizer_config=Configure.Vectorizer.text2vec_openai(     # Configure the openai embedding integration
        model="text-embedding-3-small"
    ),
    generative_config=Configure.Generative.anthropic(              # Configure the anthropic generative integration
        model="claude-3-5-sonnet",                               # The model to use
        max_tokens=1000,
    )
)

resp = requests.get(
    "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
)
data = json.loads(resp.text)

questions = client.collections.get("Question")

with questions.batch.dynamic() as batch:
    for d in data:
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }
        batch.add_object(
            properties=properties
        )

    # Check for failed objects
    if client.batch.failed_objects:
        for failed_object in client.batch.failed_objects:
            logger.error("Failed object: %s", failed_object)
    
    if questions.batch.failed_objects:
        for failed_object in questions.batch.failed_objects:
            logger.error("Failed object: %s", failed_object)

client.close()  # Free up resources