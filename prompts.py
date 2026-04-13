class GlobalHRPrompts:
    SYSTEM_INSTRUCTION = """
    You are the Global HR Expert for QAD. Your goal is to provide high-precision answers 
    based ONLY on the retrieved policy context.
    
    ### CORE DIRECTIVES:
    1. GROUNDING: Every statement must be supported by a specific source file name. 
       If multiple regions are mentioned (e.g., India vs Global), clarify which applies 
       to which location[cite: 5, 27, 48].
    2. FALLBACK: If the retrieved context does not contain the answer, explicitly state: 
       "I'm sorry, this policy is not found in our current global records. Please contact 
       the HR Service Desk at hr.servicedesk@qad.com"[cite: 6, 45].
    3. LANGUAGE: Respond in the language used by the employee.
    4. NO EXTERNAL KNOWLEDGE: Do not use your internal knowledge about labor laws 
       unless it is explicitly stated in the provided text.
    """

    @staticmethod
    def construct_rag_prompt(context_list, history, query):
        # Metadata-aware context formatting
        context_blocks = []
        for i, c in enumerate(context_list):
            block = (
                f"--- DOCUMENT {i+1} ---\n"
                f"Source: {c['filename']}\n"
                f"Text: {c['content']}\n"
                f"Similarity Score: {c.get('distance', 'N/A')}\n"
            )
            context_blocks.append(block)
        
        context_str = "\n".join(context_blocks)
        
        return f"""
        INSTRUCTIONS:
        1. Read the CONTEXT below.
        2. Extract relevant facts.
        3. Check for regional contradictions.
        4. Provide the final answer with [Source: filename] citations.

        CONTEXT:
        {context_str}

        CONVERSATION HISTORY:
        {history}

        EMPLOYEE QUERY: {query}
        
        THOUGHT PROCESS (Verify facts against context):
        FINAL ANSWER:
        """