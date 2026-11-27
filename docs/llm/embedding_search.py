"""ローカルのOllamaで、同じ教材3節を意味の近さから並べる実装例。"""

import argparse
import json
import math
import sys
from urllib.request import Request, urlopen

from study_assistant import TOPICS, load_source


def get_embeddings(model, texts):
    request = Request(
        "http://127.0.0.1:11434/api/embed",
        data=json.dumps({"model": model, "input": texts}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urlopen(request, timeout=60) as response:
        vectors = json.load(response)["embeddings"]

    if not vectors or len(vectors) != len(texts):
        raise ValueError("入力とEmbeddingの件数が一致しません。")
    return vectors


def normalized(vector):
    length = math.hypot(*vector)
    if not math.isfinite(length) or length == 0:
        raise ValueError("比較できないベクトルが返されました。")
    return [value / length for value in vector]


def rank_sources(question, model):
    sources = [load_source(filename, heading) for _, filename, heading in TOPICS]
    texts = [question, *(f"{heading}\n{excerpt}" for _, heading, excerpt in sources)]
    query, *documents = map(normalized, get_embeddings(model, texts))
    scores = [
        sum(a * b for a, b in zip(query, document, strict=True))
        for document in documents
    ]
    return sorted(zip(scores, sources, strict=True), key=lambda item: item[0], reverse=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", help="教材についての質問")
    parser.add_argument("--model", required=True, help="Ollamaに登録済みのEmbeddingモデル名")
    args = parser.parse_args()

    try:
        ranked = rank_sources(args.question, args.model)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Embedding検索を実行できませんでした: {error}", file=sys.stderr)
        return 1

    print("近い候補（スコアは正しさを保証しません）")
    for score, (filename, heading, _) in ranked:
        print(f"{score:.3f}  docs/{filename} — {heading.lstrip('# ')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
