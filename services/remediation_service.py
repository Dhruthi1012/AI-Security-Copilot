import requests


class RemediationService:

    OLLAMA_URL = "http://localhost:11434/api/generate"

    MODEL_NAME = "llama3"

    @staticmethod
    def generate_remediation_plan(
        service,
        risk,
        description
    ):

        prompt = f"""
You are a Senior Cybersecurity Consultant.

Service:
{service}

Risk:
{risk}

Description:
{description}

Generate:

1. Priority Level
2. Step-by-step Remediation Plan
3. Security Best Practices
4. Expected Risk Reduction

Keep response concise and professional.
"""

        try:

            response = requests.post(
                RemediationService.OLLAMA_URL,
                json={
                    "model": RemediationService.MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            data = response.json()

            return data.get(
                "response",
                "No remediation generated."
            )

        except Exception as error:

            print(
                f"REMEDIATION ERROR: {error}"
            )

            return (
                "Unable to generate remediation."
            )