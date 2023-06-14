<h1 align="center"><img src="codewars-logo.jpg"/></h1>

# codewars

Solution for various kata that I've completed,
including those that are incomplete.

If you're lucky, you might find some katas which have multiple methods of solving it. Some of those methods are taken directly form the Solutions page since I find them to be very close to mine.

If you find multimple methods be sure to check the kata folder for a file that starts with ```speed_```. It is a timeit speed test on every method included in the kata solution.

I also included some PyTest scripts with tests for the solutions.

# Installation

Clone the repo with:

```bash
git clone https://github.com/m1hn34/codewars.git
```

# Tests

Run the tests in terminal.

Unit tests:

```bash
pytest test_file.py
```

Optional flag "-v" is used for a verbose output.
This helps when tests are failing.

```bash
pytest -v test_file.py
```

Speed tests:

```bash
python3 speed_test_file.py
```
