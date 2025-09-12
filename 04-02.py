import getpass
import os
from pydantic import BaseModel

# 環境変数にGOOGLE_API_KEYが設定されているか確認
if not os.environ.get("GOOGLE_API_KEY"):
  # 環境変数が未設定の場合、ユーザーにAPIキーの入力を促す
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# LangChainのinit_chat_model関数を使用して、Geminiモデルを初期化
# "gemini-2.5-flash"は利用するモデル名、model_providerはプロバイダー名
from langchain.chat_models import init_chat_model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# PydanticのBaseModelを継承して、出力したいデータの構造を定義
class RamenRecipe(BaseModel):
    recipe_name: str
    ingredients: list[str]
    instructions: list[str]

# with_structured_outputメソッドを使用して、モデルに構造化出力を指示
# これにより、モデルの応答が指定したPydanticモデルの形式に変換される
structured_llm = model.with_structured_output(RamenRecipe)

# 定義した構造化モデル（structured_llm）を呼び出し、プロンプトを送信
# モデルは、指示されたラーメンのレシピを、RamenRecipeクラスの形式で返そうと試みる
result = structured_llm.invoke("日本の味噌ラーメンのレシピを一つ、材料と作り方も含めて教えてください。")

# 結果を出力。Pydanticモデルのインスタンスとして返されるため、
# ドット記法（.recipe_nameなど）で各データにアクセスできる
print(result)