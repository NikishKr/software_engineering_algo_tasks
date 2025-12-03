def is_correct_bracket_seq(s: str) -> bool:
    """Функция, опредлеляющая является ли
    заданная скобочная последовательность правильной.
    """
    memory = ["empty_value"]

    if not s:
        return True
    for c in s:
        if c in "([{":
            memory.append(c)
        if c == ")" and memory.pop() != "(":
            return False
        if c == "]" and memory.pop() != "[":
            return False
        if c == "}" and memory.pop() != "{":
            return False

    return len(memory) == 1
