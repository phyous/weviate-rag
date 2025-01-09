## Setting up weviate locally
https://weaviate.io/developers/weaviate/quickstart/local

1. Start weviate: `docker-compose up -d`
2. Check if it's ready: `python quickstart_check_readiness.py`
3. Create a collection & populate data: `python quickstart_import.py`
4. Try runing gensearch over a query: `python quickstart_neartext_query.py`
5. (when done) docker-compose down 