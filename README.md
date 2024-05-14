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
    gpt-4、gpt-3.5-turboは2021/9まで、gpt-4.0-turboは2023/4までのデータを反映する  
    いずれのモデルも数カ月毎に更新されていることに注意  
    モデルを固定するにはバージョンを固定する必要があるが、直近数バージョンより前のものは使用できなくなる可能性が高い  
    プロンプトの実行例  
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
    - ChatGPTをゲームに使おう  
    ChatGPTに採点させたスコアを用いたゲーム  
    Flaskパッケージを用いることでHTMLをインターフェイスにしたゲームが作成可能  

    5. ChatGPTを使ったLINEボットを作ろう  
    - VPS  
    KAGOYA CLOUD VPSの最低単位（CPU: 1コア1GB、メモリー: 25GB）  
    OSはUbuntu 22.04LTS  
    SSH用の認証キーファイル（～.key）を取得し、SSHを実行するフォルダに保存  
        ~~~
        VPSサーバーへの接続テスト
        ssh -i ~.key root@(与えられたIP Address)
        ~~~  
    - ドメイン名  
    お名前.comでドメイン名を取得  
    ドメイン名に対してVPSのIPアドレスをDNSレコード設定  
    指定のネームサーバーに変更  
    - SSLサーバー証明書の取得  
    取得したドメインに対して証明書を取得  
    Certbotで取得  
    - LINEアプリの作成  
    LINE上でWebhookを上記ドメインに設定する  
    VPSサーバー上で、LINEからメッセージを受け取り、それをChatGPTに投げ、結果をLINEに返すPythonプログラムを実行する    

4. 大規模言語モデルと作るアプリ開発  
    1. 生成AIで変わるアプリ開発の現場  
    アイデア出しに活用可能  
    複数のアイデアを要求することもできる  
    テーマ、条件、出力形式の設定の仕方で、出力数や制度をコントロールできる  
    KJ法、オズボーンのチェックリスト等、有名なアイデア生成方法を直接使わせることもできる  
    出力されたアイデアに質問することで深堀  
    
    2. 生成AIで仕様書を作ろう  
    - 仕様書  
    始めに仕様書作成に必要な情報を問う  
    必要な情報を箇条書きにして、仕様書としてまとめるように依頼する  
    技術用件等、重要なポイントは質問を繰り返して詳細を詰めて箇条書きする  
    - 画面遷移図、スケジュール図  
    要件を定義して画面遷移図（スケジュール図）の作成を依頼すると構成を箇条書きで返してくれる  
    これをダイアグラム作成のGPTs（Show Me等）に入力してベースとする  
    直接ダイアグラム作成用コード（Mermaid等）の出力を依頼した方が速い

    3. 生成AIでプログラムを自動生成しよう  
    クイックソート等、有名なアルゴリズムの作成を依頼する  
    手順を箇条書きする等、詳細に指示するのが無難だが、曖昧な依頼もかなり通る  
    詳しくない言語（HTML/JavaScript等）のプログラム作成はベースとして有益  
    適宜、プログラム作成上の問題を質問する  
    注釈の追加を依頼する  
        ~~~   
        あなたは優秀なプログラマーであり、プログラミング教室の先生です。
        次のプログラムは、コマンドラインからSQLiteを操作するプログラムですが、Pythonのプログラムが生徒に分かりやすいようにコメントを加える修正をしてください。
        '''

        '''
        ~~~

    4. 生成AIでデータベースを操作しよう  
    - SQLiteと連携したプログラム（コマンドラインからSQLを実行等）の作成が可能  
    - テーブル作成のSQL発行を依頼  
        ~~~
        あなたは優秀なデータベースデザイナーです。
        ToDo管理が出来るテーブルtasksを定義し、SQliteのSQLを出力して下さい。
        ~~~  
    - テーブル作成のSQL発行を依頼  
        ~~~
        あなたは優秀なソフトウェアのテスターです。
        以下のテーブルに対する日本語のサンプルデータを5件SQLで生成してください。
        '''
        SQL(Table Definition)
        '''
        ~~~
    - RDBのER図作成を依頼    
        ~~~
        あなたは優秀なソフトウェアのマニュアル作成者です。
        以下のSQLを説明するER図をmermaid記法で記述してください。
        '''
        SQL(Table Definitions)
        '''
        ~~~
    - 検索用SQLの作成依頼  
        ~~~
        あなたは優秀なデータベースデザイナーです。
        指定したユーザーのタスク一覧をユーザーの名前入りで抽出するSQLを作成してください。
        '''
        SQL(Table Definitions)
        '''
        ~~~
    
    5. 生成AIでテストを自動化しよう  
    - プログラムをテストする過程を自動化  
    pytest等のパッケージ  
    コマンドラインから実行可能  
        ~~~
        pytest test.py
        ~~~
    - 直接依頼する  
        ~~~
        あなたは優秀なプログラマーです。
        - 関数の定義 -
        この関数をpytestでテストするコードを作成してください。
        ~~~
    - テストプログラム（関数）を生成するプログラムの生成を依頼する  
        ~~~
        あなたは優秀なプログラマーです。
        - 関数の定義 -
        pytestと関数〇〇をテストするテストケースを生成するプログラムを作ってください。
        なお、以下の手順を利用したプログラムを作ってください。
        - 手順 -
        なお、上記で生成するテストコードの前に以下のプログラムを追加してください。
        from ++ import %%
        def **():
        ~~~
    - プログラム自体を与えてテスト作成を依頼する  
    長いプログラムの場合は、分割した処理を関数機能、引数、戻り値に要約させ、インプットとする  
        ~~~
        以下のプログラムをpytestでテストするコードを作成してください。
        - 対象のプログラム -
        なお、テストコードの上に上記プログラムを埋め込んでください。
        ~~~
    6. マニュアルを自動作成しよう  
    作成方法自体をChatGPTに問える  
    仕様書をインプットにしてマニュアルに変換してもらう  
    機能を箇条書きにして、それをベースにマニュアルを作成してもらう  
    - マニュアル作成サポートツールのショートカット登録  
        1. 作成した下記のバッチファイルに対してショートカットを作成する  
        2. ショートカットタブでショートカットキーを設定し、「実行時の大きさ」を「最小化」にする  
        ~~~
        call conda activate gtp_env # Anacondaを前提に仮想環境設定
        cd C:\Users\yh_in\learning\ChatGPT10 # フォルダ移動
        python C:\Users\yh_in\learning\ChatGPT10\capture_tool_gpt.py # Pythonプログラムの実行
        ~~~

5. 大規模言語モデルを10倍強化する  
    1. オープンソースで使える大規模言語モデル（LLM）
    GPT3以降は有料サービスに  
    オープンソースであっても商用利用が禁止されているモデルがある（Meta/LLaMA等）  
    オープンソースの商用利用可能な日本語LLMには、サイバーエージェントのOpenCALM、Rinna社のrinna-3.6Bがある  
    AlphabetのGeminiはオープンソースではない  
    GemmaはオープンソースだがGeminiの軽量版（テキストのみ対応）  
    基本的にGPU端末以外での実行は極めて遅くなるため、Google Colab等を用いるべき  
    - LLaMAをCPUで実行する  
    Linux環境で動作するllama.cppを利用する    
    モデル自体はHuggingfaceからダウンロード（wget）  
    binはggufに変換しないと使用できない（convert-llama-ggml-to-gguf.pyを使用）  

    2. 大規模言語モデルを拡張するLangChain  
    LangChainはLLMを用いたアプリケーション作成をサポートするパッケージ  
    モデルの呼び出しや各種プロンプトの作成機能だけではなく、テキストのベクトル化や分割といったテキスト分析全般に関する機能も有する  
    - 任意の長文に関する質問に回答するプログラム  
    テキストのロード、分割、ベクトル化  
    リトリーバー（プロンプトに付加するテキスト集合）の設定  
    モデルのロード  
    質問用プロンプトの作成  
    - 長文要約  
    テキストのロード、分割  
    モデルのロード  
    要約用プロンプトの作成（要約手法の選択）  

    3. 自立駆動型のAIエージェント（AGI）
    


    







    








    


    




    







