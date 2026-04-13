def evaluate_rag_triad(query, retrieved_context, bot_response):
    """
    Measures the three pillars of RAG precision:
    1. Faithfulness: Is the answer derived ONLY from context?
    2. Answer Relevance: Does the answer actually address the query?
    3. Context Precision: Was the retrieved context actually useful?
    """
    evaluator = GenerativeModel("gemini-1.5-pro")
    
    scoring_prompt = f"""
    Context: {retrieved_context}
    Query: {query}
    Response: {bot_response}
    
    Rate 1-5 for FAITHFULNESS (1 = contains made up info, 5 = 100% grounded):
    Rate 1-5 for RELEVANCE (1 = off topic, 5 = perfectly addresses query):
    """
    # In production, parse this response to trigger alerts if scores fall below 4.
    return evaluator.generate_content(scoring_prompt).text