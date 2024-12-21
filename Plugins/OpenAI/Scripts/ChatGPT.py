import openai

client = openai.OpenAI(
    api_key=""
)


def get_messages(question: str):
    return [{"role": "user", "content": question.strip()}]


def ask_question(question: str, api_key: str):
    openai.api_key = api_key
    messages = get_messages(question)
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=messages
    )

    return result.choices[0].message


print(ask_question("qual a cor do ceu?", client.api_key))
