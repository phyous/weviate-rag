import weaviate
from weaviate.classes.config import Configure

client = weaviate.connect_to_local()

questions = client.collections.create(
    name="Question",
    vectorizer_config=Configure.Vectorizer.text2vec_openai(     # Configure the openai embedding integration
        model="text-embedding-3-small"
    ),
    generative_config=Configure.Generative.anthropic(              # Configure the anthropic generative integration
        model="claude-3-5-sonnet",                                 # The model to use
    )
)

client.close()