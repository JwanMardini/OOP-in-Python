Python development project template
==========================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A template for a Python development project.

[[_TOC_]]



Get going
--------------------------

This is how you can work with the development environment.



### Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



### Run the code

The example program can be started like this.

```
# Execute the main program
python guess/main.py
```

All code is stored below the directory `guess/`.



### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `guess/`.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```



Optional targets
--------------------------

These targets might be helpful when running your project.



### Codestyle with black

You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

```
# Same same, different names
make black
make codestyle
```

Read more on [black](https://pypi.org/project/black/).



More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.


"Pig" is a very simple game. Two players take turns; on each turn, a player rolls a six-sided die ("die" is the singular of "dice") as many times as she wishes, or until she rolls a 1. Each number she rolls, except a 1, is added to her score this turn; but if she rolls a 1, her score for this turn is zero, and her turn ends. At the end of each turn, the score for that turn is added to the player's total score. The first player to reach or exceed 100 wins.

For example:

Alice rolls 3, 5, 3, 6, and stops. Her score is now 19.
Bob rolls 5, 4, 6, 6, 2, and stops. His score is now 23.
Alice rolls 5, 3, 3, 5, 4, and stops. Her score is now 39 (19 + 20).
Bob rolls 4, 6, 1. He has to stop, and his score is still 23 (23 + 0).
Etc.
As defined above, the first player has an advantage. To make the game more fair, we will say that if the first player reaches or exceeds 100, the second player gets one additional turn. (If the second player is the first to reach 100, the first player does not get an additional turn.)

In this project, the player will play against the computer. The computer always goes first, so the player get one more turn if the computer is the first to reach 100.

If both players are tied with 100 or more, each gets another turn until the tie is broken.
