import json
from urllib.request import Request
from main import send_prompt

test_body = {
    "prompt": "hello world",
    "base64_text_files": [
        "aGVsbG8gdGhlcmUhIGhvdyBhcmUgeW91IGRvaW5nPwo=",
    ],
}

request = Request(
    method="POST",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    headers={
        "Content-Type": "application/json",
    },
    data=json.dumps(test_body),
)


send_prompt(request)
