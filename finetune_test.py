from openai import OpenAI
client = OpenAI()

# 学習データのアップロード
client.files.create(
  file=open("ninja_corpus.jsonl", "rb"),
  purpose="fine-tune"
)

client.fine_tuning.jobs.create(
  training_file="ninja_corpus", 
  model="davinci-002"
)