import openai


def get_messages(question: str):
    return [{"role": "user", "content": question.strip()}]


def ask_question(api_key: str, question: str):
    client = openai.OpenAI(
        api_key=api_key
    )

    openai.api_key = api_key
    MyMessage = get_messages(question)
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=MyMessage
    )

    return result.choices[0].message.content
