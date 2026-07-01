# security/prompt_guard.py

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "reveal hidden instructions",
    "forget your instructions",
]


def guard_user_request(user_query: str) -> str:
    text = user_query.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in text:
            return (
                "Security Alert: Potential prompt injection detected."
            )

    return "Request is safe."