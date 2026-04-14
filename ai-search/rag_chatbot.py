from query import search
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_answer(user_query):
    # Step 1: Get relevant data from Endee
    results = search(user_query)

    context = "\n".join(results)

    # Step 2: Create prompt
    prompt = f"""
You are an AI assistant. Answer the question ONLY using the context below.

Context:
{context}

Question:
{user_query}

Answer:
"""

    # Step 3: Call LLM
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def chat():
    print("🤖 Chatbot ready! Type 'exit' to quit.\n")

    while True:
        user_query = input("You: ")

        if user_query.lower() == "exit":
            print("👋 Exiting chatbot...")
            break

        answer = generate_answer(user_query)

        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    chat()