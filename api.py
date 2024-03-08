from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def testing():
    return {"message": "TESTING TESTING TESTING"}

@app.get("/more")
async def more():
    return {"1 + 1 = 3"}

from cocktail import generate_cocktail_recipe
user_liquor = "Whiskey"
user_flavor = "Spicy"
user_mood = "Relaxed"

@app.get("/cocktail")
# async def get_cocktail(liquor: str = Query(default=None), flavor: str = Query(default=None), mood: str = Query(default=None)):
#     return generate_cocktail_recipe(liquor, flavor, mood)
async def get_cocktail():
    return generate_cocktail_recipe(user_liquor, user_flavor, user_mood)