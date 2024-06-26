from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import os

# Warningsを無効化
import warnings
warnings.simplefilter('ignore')

# 直接APIキーを指定する場合、以下↓に指定する
# os.environ["OPENAI_API_KEY"] = 'xxx'

# 質問内容を指定する --- (*1)
question1 = '紳士は何人登場しましたか？'
question2 = '紳士が連れていた犬について教えてください。'

# テキストを読み込む --- (*2)
# loader = TextLoader('./chumonno_oi_ryoriten_utf8.txt')
loader = TextLoader('./chumonno_oi_ryoriten_utf8.txt',
                    encoding='Utf-8')
documents = loader.load()

# テキストを分割 --- (*3)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, # 文字数
    chunk_overlap=0) # オーバーラップする文字数
docs = text_splitter.split_documents(documents)

# 分割したテキストをベクターストアに保存 --- (*4)
# ベクトル化
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings)
# retriever（プロンプトに付加するテキスト集合）として設定
retriever = db.as_retriever()

# ChatGPTに質問する準備 --- (*5)
# LLMの設定
# llm = OpenAI(model_name="text-davinci-003", temperature=0, max_tokens=500,)
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=500,)
qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", 
    retriever=retriever)

# 実際に質問する --- (*6)
print(question1)
print('答え:', qa.run(question1))
print('-------------')
print(question2)
print('答え:', qa.run(question2))
