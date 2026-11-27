# 実装例｜教材を検索して答えるPythonアプリ

[← LLM入門の実装例](README.md#07-実装例) ｜ [ミニ演習](exercise.md)

質問に関連する教材の節を探し、出典と抜粋を表示します。Ollamaがある場合は、その抜粋をローカルのLLMに渡して回答も生成できます。[Pythonのソースコード](study_assistant.py)

## 1. Pythonで検索を試す

Python 3で動きます。リポジトリのルートをVSCodeで開き、ターミナルで実行します。Windowsで `python` が見つからない場合は `py -3`、macOSでは `python3` を試してください。

```bash
python docs/llm/study_assistant.py "注文がない商品をSQLで探すには？"
```

`docs/sql/README.md` の「4. よくあるミス：NULLを比較する」が出典として表示されます。検索だけなら追加パッケージ・LLM・APIキーは不要です。

```bash
python docs/llm/study_assistant.py "来年度の提出期限はいつですか？"
```

対応する節が見つからないというメッセージが出ます。この試作が検索できるのは、コード内の `TOPICS` に登録した3つの節です。

## 2. ローカルのLLMで回答を生成する

[Ollama](https://ollama.com/)を起動し、使用できるモデルを用意します。`ollama list` で確認し、以下の `qwen2.5:1.5b` を一覧にあるモデル名に置き換えます。このモデルを使う場合は、先に `ollama pull qwen2.5:1.5b` でダウンロードします。

```bash
python docs/llm/study_assistant.py "注文がない商品をSQLで探すには？" --model qwen2.5:1.5b
```

検索で見つけた節と質問が、PC上で動くOllamaのChat APIに渡されます。モデルを利用できない場合も、第1節のキーワード検索を試せます。回答の文面はモデルや実行ごとに変わるため、`LEFT JOIN` と `IS NULL` が正しく使われているか、表示された教材の箇所と照らし合わせます。Ollamaが応答しない場合は、エラーと教材の抜粋が表示されます。[Ollama Chat API](https://docs.ollama.com/api/chat)

## 3. コードを読んで改善する

| 処理 | コード内の役割 |
| --- | --- |
| 検索 | `find_source` が質問のキーワードと、対応する教材の見出しを照合する。 |
| 生成 | `generate_answer` が質問・抜粋・回答ルールをモデルに送る。 |
| 出典の表示 | `main` が検索で選んだファイルと見出しを表示する。 |

「ステージから外したい」と「選んだファイルをコミットの対象から外したい」の両方で試してください。どちらも同じ意図ですが、後者は今のキーワードでは見つからない場合があります。キーワードを追加し、別の質問で誤ってその節が選ばれないかも確認してみましょう。

## 4. Embeddingで言い換えに近い教材を探す

[Embedding検索のソースコード](embedding_search.py)で、同じ教材3節と質問を1つのEmbeddingモデルで数値に変換し、コサイン類似度で並べます。この例には Python 3.10 以上と Ollama が必要です。Ollamaを起動し、Embedding用のモデルを用意します。`embeddinggemma` を使う場合の例です。

```bash
ollama pull embeddinggemma
python docs/llm/embedding_search.py "選んだファイルをコミットの対象から外したい" --model embeddinggemma
```

第3節のキーワード検索と比べ、必要な節が何位に出るかを確認します。加えて「来年度の提出期限はいつですか？」でも候補が出る点に注目してください。類似度は正しさの確率ではないため、候補に根拠がないと判断したら回答に使いません。この例は候補を表示するところまでで、LLMによる回答生成は行いません。

少数の資料を実行時にメモリで比較するので、ベクトルDBは不要です。取得した候補を評価する方法は[06 評価と運用](README.md#06-評価と運用)を参照してください。[OllamaのEmbedding API](https://docs.ollama.com/api/embed)

---

[← LLM入門の実装例](README.md#07-実装例) ｜ [ミニ演習](exercise.md)
