
def run_agent(question: str):
    """
    Simple mock AI agent.
    We will integrate a real LLM later.
    """

    if not question:
        return "Please provide a question."

    return f"AI Agent received your question: {question}"
