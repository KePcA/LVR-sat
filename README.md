LVR-sat
=======

# Documentation

Implementation of a SAT solver (in the course Logic in CS).

## Algorithms used

We used the DPLL algorithm in the implementation of our SAT solver. The algorithm was upgraded by removing unneeded duplicates, sorting values
(in the specified order False, True, Var, Not, And, Or), so that solutions and shorter formulas can be processed/found faster.

## Project structure
 * `SAT_implementation/` implementation of SAT solver.
 * `SAT_translations/` translation of problems into Boolean formulas.
 * `examples/` examples of solving problems.
 * `unit_tests/` automated tests.

## How to

See the `examples/` directory for further information. The directory contains basic examples and examples of solving problems that have already been translated to boolean
formulas.

In short, we build an arbitrary expression with the operands that can be found in `SAT_implementation/bool_formulas.py` or use one of the translations found in
`SAT_implementation/`. The resulting formula can then be directly processed with the methods of `SAT_implementation/algorithm_utilities.py`
or by running the `SAT_implementation/algorithm_DPLL.py`. The solution for a given formula is either False for no solution
or a dictionary of values that solve the problem.

## Unit tests

The `unit_tests/` directory consists of multiple `*.py` files which test each aspect of our implementation. Each test can be run
directly. The whole implementation can be tested by running the `unit_tests/run_all_unit_tests.py` script.

All tests can be run from Pycharm as well. This can be done simply by clicking in a `*.py` the methods right-click-and-play "Run Unittests and Mytestcase"-
(Note: the Python interpreter must be set beforehand).