import base64
import json
import os
from dotenv import load_dotenv
from flask import Response
import google.generativeai as genai
import os

load_dotenv()


def send_prompt(request):
    genai.configure(api_key=os.getenv("APIKEY"))

    request_json = json.loads(request.data, strict=False)

    prompt = request_json.get("prompt", None)
    if prompt is None:
        raise ValueError("Prompt is required")

    base64_text_files = request_json.get("base64_text_files", [])
    for file in base64_text_files:
        decoded_file = base64.b64decode(file).decode("utf-8")
        prompt += "\n" + decoded_file

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    parts = [part.text for part in response._result.candidates[0].content.parts]

    return Response(
        json.dumps(parts),
        status=200,
        mimetype="application/json",
    )
