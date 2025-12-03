from tasks.data_stuctures.bracket_sequence.solution import is_correct_bracket_seq


def test_usual():
    assert is_correct_bracket_seq("{[()]}") is True


def test_wrong():
    assert is_correct_bracket_seq("{[(({}])}") is False


def test_empty():
    assert is_correct_bracket_seq("") is True


def test_extra_element():
    assert is_correct_bracket_seq("(()){}]") is False


def test_long():
    assert is_correct_bracket_seq("{{[[[[[(((){}))]]{}]([])]]}()}") is True
