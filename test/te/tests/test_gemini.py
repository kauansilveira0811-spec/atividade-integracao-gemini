import pytest
from unittest.mock import patch
from gemini_client import GeminiClient

def test_send_prompt_valid():
    """Testa envio de prompt válido e recebimento da resposta"""
    with patch('gemini_client.genai.GenerativeModel') as mock_model:
        mock_instance = mock_model.return_value
        mock_instance.generate_content.return_value.text = "Resposta de teste"
        
        client = GeminiClient()
        client.api_key = "test-key"
        client.model = mock_instance
        
        response = client.send_prompt("Olá")
        assert response == "Resposta de teste"

def test_send_prompt_empty():
    """Testa validação de prompt vazio"""
    client = GeminiClient()
    client.api_key = "test-key"
    with pytest.raises(ValueError):
        client.send_prompt("")
