def generate_answer(query, contexts):
    """
    Simple, stable answer generation without LLM.
    This avoids token limit crashes and keeps RAG intact.
    """

    if not contexts:
        return "I don't know. No relevant context was found."

    # Take the most relevant chunk
    top_context = contexts[0]

    answer = f"""
Based on the retrieved documents, here is the most relevant information:

{top_context}

(Answer generated using retrieval-based synthesis.)
""".strip()

    return answer
