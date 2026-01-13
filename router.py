import re
def normalize_key(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def route_prompt(prompt: str):
    p = prompt.lower().strip()

    if "remember" in p or "save" in p:
        if " is " not in p:
            return None, None, None

        before, after = prompt.split("is", 1)

        raw_key = (
            before.lower()
            .replace("remember", "")
            .replace("save", "")
            .replace("my", "")
            .strip()
        )

        key = normalize_key(raw_key)
        value = after.strip()

        return "memory_save", key, value
    if p.startswith("what is my") or "recall" in p:
        clean = normalize_key(p)
        key = (
            clean
            .replace("what is my", "")
            .replace("recall", "")
            .strip()
        )
        return "memory_read", key, None

    if p.startswith("what is") or p.startswith("calculate"):
        clean = normalize_key(p)

        expression = (
            clean
            .replace("what is", "")
            .replace("calculate", "")
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("x", "*")
            .replace("divided by", "/")
            .strip()
        )

        return "calculator", expression, None
    return None, None, None
