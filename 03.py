from google import genai
from pydantic import BaseModel
import os

# Pydanticモデルでデータの構造を定義
class RamenRecipe(BaseModel):
    recipe_name: str
    ingredients: list[str]
    instructions: list[str]

# 環境変数からAPIキーを取得
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# プロンプトを送信し、構造化出力をリクエスト
# response_schemaに作成したPydanticモデルを指定
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="日本の味噌ラーメンのレシピを一つ、材料と作り方も含めて教えてください。",
    config={
        "response_mime_type": "application/json",
        "response_schema": RamenRecipe,
    },
)

# 構造化されたデータをPythonオブジェクトとして利用
my_recipe: RamenRecipe = response.parsed

# オブジェクトの各要素を出力
print(f"レシピ名:\n{my_recipe.recipe_name}")
print("---------------------------")
print(f"材料:\n{'\n'.join(my_recipe.ingredients)}")
print("---------------------------")
print(f"作り方:\n{'\n'.join(my_recipe.instructions)}")