from fastapi.testclient import TestClient
from main import app


# Create a test client for the FastAPI app
client = TestClient(app)

# Call the function and print the output
response = client.get("/api/question/list")

#response = requests.get('http://127.0.0.1:8000/items/1')

print(response.json())