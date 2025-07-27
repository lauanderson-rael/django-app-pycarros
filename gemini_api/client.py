import google.generativeai as genai
from django.conf import settings

def get_car_ai_bio(model, brand, year):
    prompt = f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas positivas e descreva especificacoes tecnicas sobre o modelo de carro.
    '''
    genai.configure(api_key=settings.GEMINI_API_KEY)

    model_ai = genai.GenerativeModel('gemini-2.5-flash')

    try:
        response = model_ai.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar descrição: {str(e)}"

# Exemplo de uso
if __name__ == "__main__":
    descricao = get_car_ai_bio("Civic", "Honda", "2023")
    print(descricao)
