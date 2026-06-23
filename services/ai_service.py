import requests


class AIService:

    OLLAMA_URL = "http://localhost:11434/api/generate"

    MODEL_NAME = "llama3"

    @staticmethod
    def generate_security_explanation(
        service,
        risk,
        description
    ):

        prompt = f"""
You are a Cybersecurity Analyst.

Service: {service}
Risk Level: {risk}
Description: {description}

Explain:
1. Why this service can be risky.
2. What attackers might do.
3. How to secure it.

Keep the response professional and beginner friendly.
"""

        try:

            response = requests.post(
                AIService.OLLAMA_URL,
                json={
                    "model": AIService.MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            data = response.json()

            return data.get(
                "response",
                "No AI response generated."
            )

        except Exception as error:

            print(
                f"AI ERROR: {error}"
            )

            return (
                "Unable to generate AI explanation."
            )