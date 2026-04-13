# RAG HR Chatbot

## Project Structure

```plaintext
rag_hr_chatbot/
├── app/
│   ├── __init__.py         # Initializes the Flask app
│   ├── routes.py           # Defines the API routes
│   ├── models.py           # Contains the Firestore models
│   └── services.py         # Handles communication with Google Cloud services
├── tests/
│   ├── test_routes.py      # Unit tests for API routes
│   └── test_services.py     # Unit tests for services
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── main.py                 # Entry point for running the application
```

## Project Details

This project is a chatbot developed using Flask, which utilizes Google Cloud Vertex AI for machine learning capabilities, BigQuery for data analytics, and Firestore for data storage. The aim of the project is to create an HR assistant that can interact with users in natural language and provide responses based on the data stored within the system.

### Main Components:
- **Google Cloud Vertex AI**: Used for deploying machine learning models.
- **BigQuery**: Utilized for handling large datasets and performing analytics queries.
- **Firestore**: Provides a NoSQL database to store HR-related data.
- **Flask**: The web framework for building the API.

### Getting Started

Follow these steps to set up the project locally:
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up Google Cloud credentials to access the services.
4. Run the application with `python main.py`.

### Contributing

Contributions are welcome! Please follow the standard procedures for submitting issues and pull requests.
