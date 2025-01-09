from helpers import create_client

client = create_client()

questions = client.collections.get("Question")

try:
    response = questions.generate.near_text(
        query="biology",
        limit=2,
        grouped_task="Write a tweet with emojis about these facts.",
    )
    print(response.generated)  # Inspect the generated text
except Exception as e:
    print(f"Error: {e}")
    # print stacktrace
    import traceback
    traceback.print_exc()
finally:
    client.close()  # Free up resources