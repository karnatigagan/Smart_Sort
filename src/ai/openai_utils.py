# openai_utils.py
import openai
import os

# Ensure the API key is set in the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is None:
    raise ValueError("OpenAI API key is not set in the environment.")

openai.api_key = openai_api_key

def get_gpt_category(file_title):
    """
    Sends the file title to OpenAI GPT and returns a suggested category.
    """
    try:
        prompt = f"Categorize the following file based on its title: '{file_title}'. What category does this file belong to? Respond with a single word such as 'Reports', 'Invoices', 'Manuals', 'Images', 'Media', 'Documents', etc."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are an assistant that classifies files based on their titles."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=10  # We only need a short response
        )

        category = response['choices'][0]['message']['content'].strip()
        print(f"GPT categorized the file '{file_title}' as: {category}")
        return category
    except Exception as e:
        print(f"Error during GPT categorization: {e}")
        return None




















# import os
# import openai
# from openai.error import RateLimitError

# # Get the OpenAI API key from environment variables
# openai_api_key = os.getenv('OPENAI_API_KEY')
# if openai_api_key is None:
#     raise ValueError("OpenAI API key is not set in the environment.")

# openai.api_key = openai_api_key

# # Get embedding for a document using OpenAI API
# def get_document_embedding(content):
#     try:
#         response = openai.Embedding.create(
#             input=content,
#             model="text-embedding-ada-002"
#         )
#         embedding = response['data'][0]['embedding']
#         print(f"Generated embedding for document: {embedding[:5]}...")
#         return embedding
#     except RateLimitError as e:
#         print(f"Rate limit error: {e}")
#         return None
#     except Exception as e:
#         print(f"Error generating embedding: {e}")
#         return None






# import openai
# from openai.error import RateLimitError

# # Initialize OpenAI API key
# openai.api_key = 
# # Get embedding for a document using OpenAI API
# def get_document_embedding(content):
#     try:
#         response = openai.embeddings.create(
#             input=content,
#             model="text-embedding-ada-002"  # Embedding model designed for generating embeddings
#         )
#         embedding = response['data'][0]['embedding']
#         print(f"Generated embedding for document: {embedding[:5]}... (truncated)")  # Display part of the embedding
#         return embedding
#     except RateLimitError as e:
#         print(f"Rate limit error: {e}")
#         return None







# 


# import openai

# # Initialize OpenAI API key
# openai.api_key = '
# # Get embedding for a document using the new OpenAI API
# def get_document_embedding(content):
#     response = openai.embeddings.create(
#         input=content,
#         model="text-embedding-ada-002"  # Embedding model in the new API
#     )
#     return response['data'][0]['embedding']  # Return the embedding vector





#Doesn't work. 
