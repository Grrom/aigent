import json
import os
from dotenv import load_dotenv
from flask import Response
import requests

load_dotenv()


def send_prompt(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    request_json = json.loads(request.data)

    prompt = request_json.get("prompt", None)
    if prompt is None:
        raise ValueError("Prompt is required")

    response = requests.post(
        f"{os.getenv('LLM_URL')}{os.getenv('APIKEY')}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"contents": [{"parts": [{"text": prompt}]}]}),
    )
    res = response.json()
    parts = res.get("candidates", [])[0].get("content", []).get("parts", [])

    return Response(json.dumps(parts), mimetype="application/json")
