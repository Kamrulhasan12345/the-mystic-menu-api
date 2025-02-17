from google.genai import Client, types

import os


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai = Client(api_key=GEMINI_API_KEY)

async def generate_description(recipe_name, recipe_type="creative"):
    prompt = """**Recipe Name:** {recipe_name}
    Recipe Type: {recipe_type}
    """
    final_prompt = prompt.format(recipe_name=recipe_name, recipe_type=recipe_type)
    response = genai.models.generate_content(model="gemini-2.0-flash", contents=final_prompt, config=types.GenerateContentConfig(
        system_instruction="""**Instructions:** You are a creative, yet informative, historical, criminology-loving, horror-loving, lovecraftian and at the same time a joyous, peace-loving, a happy-to-serve, and a jack-of-all-trades recipe writer. You will generate a compelling description for the recipe.  The description should be concise, enticing, and highlight the key features of the recipe, **within 50 words**, and must not contain any **trailing newlines**. You are absolutely bound to follow the example given.
        **Input:**

        **Recipe Name**: Spicy Mango Salsa
        **Recipe Type**: Appetizer
        
        **Example:** 
        A vibrant and refreshing explosion of sweet mango, fiery jalapeño, and tangy lime, this Spicy Mango Salsa is the perfect party appetizer.  The contrasting flavors and textures create a tantalizing dip for tortilla chips, or a delicious topping for grilled chicken or fish.  Get ready for a flavor fiesta!
        """,

        temperature=0.3,
    ),
)

    return response.text.strip("*").strip()

async def generate_recipe():
    name = genai.models.generate_content(model="gemini-2.0-flash-001", contents="Generate a recipe name randomly", config=types.GenerateContentConfig(system_instruction="You are a creative, yet informative, historical, horror-loving, jack of-all-trades, happy-to-serve recipe writer. Your job is to only create new **recipe names**. Only generate names and nothing else beforehand or after that.")).text.strip("*").strip()
    type = genai.models.generate_content(model="gemini-2.0-flash-001", contents="Generate a recipe type from its name randomly. Name is {name}".format(name=name), config=types.GenerateContentConfig(system_instruction="You are a creative, yet informative, historical, horror-loving, jack of-all-trades, happy-to-serve recipe writer. Your job is to only create new **recipe types** out of given recipe names. Only generate recipe types and nothing else beforehand or after that.")).text.strip("*").strip()
    description = await generate_description(name, type)
    return {"name": name, "type": type, "description": description}