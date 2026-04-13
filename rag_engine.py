import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting
from vertexai.language_models import TextEmbeddingModel
from bq_utils import perform_vector_search
from prompts import GlobalHRPrompts
from secret_manager import config

vertexai.init(project=config.project_id, location=config.location)

def get_answer(user_query, chat_history):
    # Embedding
    embed_model = TextEmbeddingModel.from_pretrained("text-embedding-004")
    query_emb = embed_model.get_embeddings([user_query])[0].values
    
    # Retrieval
    contexts = perform_vector_search(query_emb)
    
    # Generation
    llm = GenerativeModel("gemini-1.5-pro")
    full_prompt = GlobalHRPrompts.construct_rag_prompt(contexts, chat_history, user_query)
    
    response = llm.generate_content(
        full_prompt,
        generation_config={"temperature": 0.2},
        system_instruction=GlobalHRPrompts.SYSTEM_INSTRUCTION,
        safety_settings=[
            SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE")
        ]
    )
    
    return {"answer": response.text, "sources": contexts}
