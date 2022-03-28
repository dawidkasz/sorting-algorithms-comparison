# sorting algorithms comparison

## Usage
1. Install dependencies with `pip install -r requirements.txt`.
2. Generate benchmark.json file using `pytest --benchmark-json=benchmark.json`.<br>
    Note, that you may need to execute `export PYTHONPATH=src` in order for the tests to run correctly.
3. Run `python3 src/main.py benchmark.json comparison.png`.


### Custom parameters
`python3 main.py [-h] [-s] INPUT_FILE OUTPUT_FILE`

**positional arguments**:

    INPUT_FILE      Path to the file generated by `pytest --benchmark-json=PATH`
    OUTPUT_FILE     Output file path


**optional arguments**:

    -s, --separate  Generate separate chart for each algorithm