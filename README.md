# ChatGPT10
生成AI/ChatGPTでPythonプログラミング  

1. 大規模言語モデル  
    1. 生成AIに対する期待  
    - 生成AI（Generative AI）  
    画像、文章、音声、プログラムコード等を対話的に生成  
    GPT-4の作成費用は10億ドル超  
    - 生成AIの利用における現時点の問題点  
    著作権やプライバシーの侵害  
    生成物の著作権は米国では認められないが、日本では認められうる  
    2. AIの機能とその仕組み  
    3. 画像生成AIの仕組み  
    - 画像生成AIについて  
    GoogleのStable Diffusionはオープンソース、GPU端末で利用可能  
    - 敵対的生成ネットワーク（Generatibe Adversarial Networks）  
    生成器と識別器を競わせることで教師なし学習を繰り返し行う  
    音声や文章等、画像以外の分野に拡張されている  
    多様性への対応に限界がある（モード崩壊）  
    - 拡散モデル（Diffusion Model）
    元のデータにノイズを加える拡散過程、ノイズを除去する逆拡散過程を交互に繰り返すことで教師なし学習を行う  
    GANに比べて出力に多様性がある  
    4. 画像生成AIを試してみよう  
    Hugging Faceのdiffusersパッケージで学習済みの画像生成モデルのDLと使用が可能  
    5. ChatGPTの仕組み  
    - ChatGPTと各モデルのスペック  
    GPT-4でパラメーター数の増加に応じた性能向上は頭打ち  
    ⇒ 処理可能なトークン数に応じた最適なパラメータ数が存在  
    語順を考慮する「位置エンコーディング」  
    単語間の関係性を考慮したベクトル化「アテンション」  
    - RLHF（Reinforcement learning from human feedback）  
    人為的に作成したデータでファインチューニング  
    出力に対して人間が3つの観点（真実性、無害性、有益性）から評価データを作成  
    評価データから作成した報酬モデルを用いて強化学習  

2. ChatGPT プロンプト  
    1. ChatGPTの正しい理解とハルシネーションについて  
    - ChatGPTを利用するのに適したタスク  
    要約、推論、変換、拡張  
    入出力の合計トークン数がGPT-3.5で2048、GPT-4で4096が上限になることに注意  
    ⇒ 英語の方が多くの情報を与えることができる  
    - ハルシネーションに注意  
    計算問題は苦手  
    情報の鮮度は落ちる  
    ⇒ プロンプトエンジニアリング  
    2. 効果的なプロンプトと要約タスク  
    要約依頼の例  
        ~~~
        次の文章を要約してください。
        ただし、100字以下にしてください。
        箇条書きも使ってください。
        「メモリ管理」について強調してください。
        スティーブジョブズのようにお願いします。

        [対象の文章]
        ~~~
    3. 志向の連鎖（CoT）と文章生成タスク  
    - 連想から答えを導くことができる「思考の連鎖」  
    例を示す  
    Q（質問）とA（答え）は認識している  
    問題を小分けにする（「ステップバイステップで」）  
    出力形式を指定する  
    文章生成が可能  
        ~~~
        ### 以下を学習してください ###
        Q: 〇〇
        A: △△
        ### 質問です ###
        Q: ✕✕
        A: 

        ステップバイステップで考えて下さい。

        以下の箇条書きからレポートを作成し、Markdownで出力してください
        ~~~
    - Zero-ShotプロンプトとFew-Shotプロンプトについて  
    例を与えないのがZero-Shot、与えるのがFew-Shot  

    4. 文章の分析と数値化  
    - 文章に表れる感情分析をしてみよう  
    文章を様々な評価軸で数値化できる  
        ~~~
        次の文章を、向上心、技術力の2つのパラメータで数値化してください
        ~~~
    - 文章からキーワードを抽出してみよう  
    指定した単語の抽出もできる  
        ~~~
        次の文章で訪れた場所を抽出してください
        ~~~

    5. 再帰生成とプロンプト内プログラム  
    - プロンプトはプログラミング言語の一種だ  
    プログラムコードのようにプロンプトを作成することで再帰的な処理やループ処理も可能  
        ~~~
        先に、失恋した友人を元気づけるアイデアを5つ考えて配列変数{idea}に入れてください。
        次に、次のプログラムをシミュレーションして、関連するアイデアを次々と考えてください。
        for y in idea:
            for x in idea:
                box[y][x] = アイデアを組合わせて考案(x, y)
        次に変数{box}を表形式で表示してください。
        ~~~
    
    6. プロンプトによるプロンプト生成術  
    - 画像生成AIのためにプロンプトを生成しよう  
    プロンプトの作成を指示
        ~~~
        画像生成AIで、一度は行ってみたい絶景画像を生成するプロンプトを作成したいです。
        以下の条件でプロンプトを作ってください。
        ・幻想的な風景
        ・古代遺跡
        ・奥行きがある
        ただし、英語で生成してください。
        ~~~
    - ChatGPT用のプロンプトを生成するプロンプト  
    望みのプロンプトに対するアドバイスを求め、それに従ったプロンプトを作成する
        ~~~
        [アドバイスを求めるプロンプト]
        プログラミング上達のためにするべきアイデアを生成するプロンプトを作りたいです。
        より良いプロンプトを生成するために、どんな追加情報が必要ですか?
        [アドバイスをベースに作成したプロンプト]
        次の目標を達成するため条件を考慮してChatGPT用のプロンプトを5つ生成してください。
        ### 目標
        ・プログラミング上達のためにするべきアイデア
        ### 条件
        ・プログラミング言語: Python
        ・スキルレベル: 初心者
        ・目標: Python全般
        ~~~
3. ChatGPT API編  
    1. ChatGPT APIでできること  
    - ChatGPIのAPIとは何か  
    OpenAI、Microsoft Azureのいずれかから利用可能  
    APIキーは環境変数に設定して利用すること  
    Windows+R、sysdm.cpl、詳細設定で環境変数は設定できる  
    2. ChatGPT APIの基本を確認しよう  
    - ChatGPT APIの応答を確認してみよう  
    APIの実行例  
        ~~~
        import openai, os
        openai.api_key = os.environ["OPEN_API_KEY"]
        feature='フレンチブルドッグ'
        # プロンプトの作成
        prompt = f'''
        下記の特徴を元にペットの名前を考えてください。
        特徴: {feature}
        '''
        # プロンプトの実行
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{'role': 'user', 'content': prompt}]
        # 応答部分を抽出
        content = response.choices[0]['message']['content']
        )
        ~~~
    3. APIの種類とモデル  
    - ChatCompletionの詳しい使い方  
    プロンプトの実行  
        ~~~
        openaai.ChatCompletion.create(
            model='gpt-3.5-turbo,
            messages=[{'role': 'user', 'content': 'プロンプト'}],
            temperature=1.0
        )
        ~~~
        temperatureはランダム性を制御するパラメータで、1.0が中央値、0に近づくほどランダム性が低くなり、2に近づくほどランダム性が高くなる  
        APIの呼び出しはその都度リセットされるため、会話をするためにはそれまでの会話を全て指定する必要がある  

        |role|設定|
        |:---|:---|
        |system|役割の設定等、どの立場で応答を返すかを指定|
        |user|ChatGPTに対するユーザーの入力を指定|
        |assistant|ChatGPTからの出力を指定|

    4. ChatGPTを使ってゲームを作ろう   



    




    







