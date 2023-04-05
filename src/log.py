from datetime import datetime


def write_log(question, answer):
    text = f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n{question}\n{answer}\n\n'
    with open("log.txt", "a", encoding='utf-8') as f:
        f.write(text)
