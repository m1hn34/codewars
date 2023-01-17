# Python3
# Pytest script for camelcase.py

from camelcase import solution


def test_0():
    assert(solution('helloWorld') == 'hello World')
    assert(solution('camelCase') == 'camel Case')
    assert(solution('breakCamelCase') == 'break Camel Case')
