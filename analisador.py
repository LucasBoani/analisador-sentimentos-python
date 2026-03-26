from textblob import TextBlob

def analisar_sentimento(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    if polaridade > 0:
        return "Positivo 😊"
    elif polaridade < 0:
        return "Negativo 😡"
    else:
        return "Neutro 😐"

# Teste com suas frases
frases = [
    "O curso no IDP é sensacional!",
    "O trânsito em Brasília está terrível hoje.",
    "I love studying Python at IDP!"
]

print("\n--- RESULTADO DA ANÁLISE ---")
for f in frases:
    print(f"Frase: '{f}' | Sentimento: {analisar_sentimento(f)}")

    