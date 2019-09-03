import pytest

import eval_implementation as app


@pytest.mark.parametrize("i", [i for i in [1, 2]])
def test_app(i):
    with open('tests/test_input{:d}.txt'.format(i), 'r') as f:
        line = f.readline()

    with open('tests/test_output{:d}.txt'.format(i), 'r') as f:
        output_line = float(f.readline())

    input_value = line

    output = []

    def mock_input():
        return input_value

    app.input = mock_input
    app.print = lambda x: output.append(x)
    app.main()

    assert output == [output_line]
