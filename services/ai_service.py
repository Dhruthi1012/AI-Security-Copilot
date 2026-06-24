import requests


class AIService:

    OLLAMA_URL = "http://localhost:11434/api/generate"

    MODEL_NAME = "phi3:latest"

    @staticmethod
    def generate_security_explanation(
        service,
        risk,
        description
    ):

        prompt = f"""
Service: {service}
Risk: {risk}
Description: {description}

Give 3 short security recommendations.
"""

        try:

            response = requests.post(
                AIService.OLLAMA_URL,
                json={
                    "model": AIService.MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=300
            )

            data = response.json()

            return data.get(
                "response",
                "No AI response generated."
            )

        except Exception as error:

            print(f"AI ERROR: {error}")

            return "Unable to generate AI explanation."