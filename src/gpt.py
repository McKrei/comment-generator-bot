import openai

from config import OPEN_AI_API_TOKEN, MODEL_GPT


openai.api_key = OPEN_AI_API_TOKEN


def get_answer_gpt(question: str, role: str = None, examples: list = None):
    message = [{"role": "user", "content": question}]
    if role:
        message.append({"role": "system", "content": role})
    if examples:
        for ex in examples:
            message.append({"role": "assistant", "content": ex})
    completion = openai.ChatCompletion.create(
        model=MODEL_GPT,
        messages=message[:2000],
    )
    return completion.choices[0].message.content
