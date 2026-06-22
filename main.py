from gemini_client import GeminiClient

def main():
    print("🤖 Integração com Gemini API")
    print("-" * 40)
    
    try:
        client = GeminiClient()
        prompt = input("\nDigite sua pergunta: ")
        resposta = client.send_prompt(prompt)
        print("\n✅ Resposta do Gemini:\n")
        print(resposta)
    except Exception as e:
        print(f"\n❌ Erro: {e}")

if __name__ == "__main__":
    main()
