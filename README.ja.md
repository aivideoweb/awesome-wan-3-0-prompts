# 🎬 Awesome Wan 3.0 Prompts — AI 動画プロンプト集

MIT ライセンスの Flaq AI コレクションをもとにした VideoWeb 版です。120 本の本文は簡体字中国語と英語で、VideoWeb での全件検証は行っていません。このページは日本語の導入と例を提供します。[出典と画像について](UPSTREAM.md)。

[![日本語](https://img.shields.io/badge/日本語-現在-brightgreen)](README.ja.md)
[![简体中文](https://img.shields.io/badge/简体中文-阅读-red)](README.zh-CN.md)
[![English](https://img.shields.io/badge/English-Read-blue)](README.md)
[![Español](https://img.shields.io/badge/Español-Leer-blue)](README.es.md)

> **Wan 3.0 / Wan AI 動画生成**向けの 120 本の実用プロンプト。映画、広告、EC・美容、対話・ローカライズ、自然・動物、工業・製造、教育、建築、交通、制作制御を収録しています。

[テスト済みプロンプトをフォームから投稿](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml)したり、[コントリビューションガイド](CONTRIBUTING.md)に沿って翻訳や新カテゴリを提案したりできます。

![Wan 3.0 AI 動画プロンプト集](assets/videoweb-wan-3-hero.webp)

## VideoWeb AI で動画を作る

[VideoWeb AI の Wan 3.0](https://videoweb.ai/model/wan-3-0/) でテキストまたは画像を選び、プロンプトを貼り付け、画面にある設定を指定します。短い1カットから始め、一度に1項目だけ変えてください。[使い方（英語）](guides/videoweb-workflow.md) · [X の動画事例](guides/x-community-showcase.md)。

## 特徴

- 単なるキーワード集ではなく、動作の因果関係、カメラ、照明、音、固定条件まで記述。
- T2V、I2V、開始・終了フレーム、参照動画、動画編集の書き方に対応。
- 人物と商品の一貫性を保つための「固定アンカー」を採用。
- 映像説明とセリフの言語を分けた多言語プロンプトに対応。
- 分類画像は元のコレクションを継承し、VideoWeb の表紙は新たに制作。画像は説明用であり、動画の生成結果ではありません。

> Wan 3.0 の利用可能な時間、解像度、参照素材数、音声機能は、地域やサービスによって異なる場合があります。現在利用している公式画面の設定を優先してください。

## 基本フォーマット

```text
[出力] 秒数 + アスペクト比 + 映像表現
[主体] 同一性を保つ特徴 + 変えてはいけない要素
[環境] 時間 + 場所 + 天候 + 前景/中景/背景
[動作] きっかけ → 連続動作 → 目に見える結果
[カメラ] 画角 + 位置 + 一つの移動経路 + 最終構図
[画作り] 光 + 色 + 素材 + モーション表現
[音] 環境音 + 動作音 + 音楽 + セリフ
[制約] 保持するもの + 起こりやすい失敗
```

## カテゴリ

| カテゴリ | 本数 | リンク |
|---|---:|---|
| 映画的ストーリーテリング | 6 | [開く](prompts/cinematic-storytelling.md) |
| 商品広告・ブランド映像 | 6 | [開く](prompts/ads-and-products.md) |
| UGC・料理・旅行 | 6 | [開く](prompts/ugc-food-travel.md) |
| アクション・スポーツ | 6 | [開く](prompts/action-sports.md) |
| アニメーション・ファンタジー | 6 | [開く](prompts/anime-fantasy.md) |
| 音楽・コメディ・SNS | 6 | [開く](prompts/music-comedy-social.md) |
| ビジネス・公共サービス | 11 | [開く](prompts/professional-business.md) |
| 教育・科学 | 11 | [開く](prompts/education-science.md) |
| 建築・交通・ホテル | 11 | [開く](prompts/architecture-mobility.md) |
| 制作制御・編集 | 11 | [開く](prompts/production-control.md) |
| EC・美容・小売 | 10 | [開く](prompts/commerce-beauty-retail.md) |
| 人物・対話・ローカライズ | 10 | [開く](prompts/people-dialogue-localization.md) |
| 自然・動物・季節 | 10 | [開く](prompts/nature-animals-seasons.md) |
| 工業・製造 | 10 | [開く](prompts/industrial-manufacturing.md) |

## 完全なテストプロンプト

```text
8 秒、16:9、自然主義的な実写映画映像。雨上がりの夜明け、古い街路で、濃い緑のコートを着た若い郵便配達員がヴィンテージ自転車に乗り、浅い水たまりを通過する。前輪が水を左右二つの低い飛沫に分け、水滴は空中に浮かず石畳へ戻る。カメラは左後方の膝の高さから安定して追従し、街の環境を示すミディアムショットで始まり、手とベルへ近づいた後、通りの先の暖かな朝日へ上昇する。音：タイヤが水を切る音、遠くの店のシャッター、澄んだ自転車ベルを一度。顔、コート、自転車の形状、進行方向を維持する。文字、ロゴ、余分な手足、ジャンプカット、浮遊物は出さない。
```

プロンプト本文は簡体字中国語と英語ですが、構造化されているため日本語へ置き換えやすくなっています。セリフだけを日本語で指定する例：

```text
映像説明は中国語または英語。
セリフは日本語、東京標準語、静かな話し方。
正確なセリフ：「雨、まだ止みそうにないですね。」
字幕なし。聞き手は口を閉じ、一度だけ小さくうなずく。
```

詳細は[プロンプト作成ガイド](guides/prompting-guide.md)、[15 言語ディレクトリ](locales/README.md)、[トラブルシューティング](guides/troubleshooting.md)をご覧ください。本プロジェクトは独立したコミュニティ資料であり、モデル提供元の公式文書ではありません。

## VideoWeb AI アフィリエイトプログラム

[VideoWeb AI は現在アフィリエイトプログラムを提供しています](https://videoweb.ai/affiliate-program/)。AI 動画・画像・音楽の制作ツールを紹介する開発者、クリエイター、教育者、レビュアー、チームが対象です。通常の VideoWeb AI アカウントでログインし、プロフィールと契約を完了すると、自分の紹介リンクを作成して、チュートリアル、レビュー、コミュニティ、製品、Web サイトで共有できます。

- 紹介ユーザーの最初の有効な有料注文について **20%** の報酬。
- 登録後 **60 日間のアトリビューション期間**内に行われた後続の有効な有料注文について **10%** の報酬。
- 返金、チャージバック、リスクによるキャンセル、帰属状況、ポリシー違反は、報酬の支払い前に審査されます。

規則は変更される場合があります。紹介前に最新のページと Affiliate Agreement を確認してください。上記リンクは公式プログラムページであり、このプロジェクトの紹介リンクではありません。
