from transformers import pipeline

class LLMResponseAgent:
    def __init__(self):
        # Load a small, free model that works well on student laptops
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def generate_response(self, query, top_chunks):
        # Join the top chunks into a single paragraph of context
        context = "\n".join(top_chunks)

        # Ask the model to answer the question based on that context
        result = self.qa_pipeline(question=query, context=context)

        return result["answer"]
