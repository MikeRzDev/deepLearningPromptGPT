"""
 Tactic 2:
 Ask for a structured output like JSON or HTML
"""
from shared import get_completion


def second_exercise():
    prompt = f"""
    Generate a list of three made-up book titles along \ 
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """
    response = get_completion(prompt)
    print(response)
