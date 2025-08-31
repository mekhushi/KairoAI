from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

class KairoBot:
    def __init__(self, model="gpt-3.5-turbo"):
        api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")

        if api_key is None:
            raise ValueError(" No API key found. Please set GROQ_API_KEY or OPENAI_API_KEY")

       
        if api_key.startswith("gsk_"):
            self.llm = ChatOpenAI(
                model="llama-3.3-70b-versatile",   
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )
        else:
           
            self.llm = ChatOpenAI(model=model, api_key=api_key)

        self.history = []

    def ask(self, query: str) -> str:
        self.history.append(("User", query))
        context = "\n".join([f"{role}: {msg}" for role, msg in self.history])

        prompt = ChatPromptTemplate.from_template(
            "You are Kairo, a helpful AI assistant.\n"
            "Here is the conversation so far:\n{history}\nUser: {q}\nKairo:"
        )
        final_prompt = prompt.format_messages(history=context, q=query)

      
        response = self.llm.invoke(final_prompt)
        answer = response.content
        self.history.append(("Kairo", answer))
        return answer
