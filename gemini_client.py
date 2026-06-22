import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    """Cliente para comunicação com Gemini API"""
    
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY não encontrada!")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def send_prompt(self, prompt: str) -> str:
        """Envia prompt e retorna resposta"""
        if not prompt or not prompt.strip():
            raise ValueError("Prompt não pode estar vazio!")
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            raise RuntimeError(f"Erro na API: {str(e)}")
