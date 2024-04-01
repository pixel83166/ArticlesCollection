import json


def get_articles():
    with open("articles.json", "r", encoding="utf-8") as art:
        f = json.load(art)
    return f


def save_article(name, text):
    save_file = get_articles()

    save_file[name] = text

    with open("articles.json", "w", encoding="utf-8") as arti:
        json.dump(save_file, arti, ensure_ascii=False)


def delete_article(name):
    delete_file = get_articles()

    del delete_file[name]

    with open("articles.json", "w", encoding="UTF-8") as soh_file:
        json.dump(delete_file, soh_file, ensure_ascii=False)

