"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
            {
        "input": [8, [2, 3, 5, 6, 7, 5, 4, 2]],
        "answer": "N"
    },
    {
        "input": [8, [2, 3, 6, 5, 4, 6, 3, 2]],
        "answer": "S"
    },    
    {
        "input": [5, [1, 2, 3, 2, 1]],
        "answer": "N"
    },
    {
        "input": [7, [1, 3, 2, 1, 2, 3, 1]],
        "answer": "S"
    },
    {
        "input": [9, [4, 3, 4, 5, 6, 7, 8, 9, 10]],
        "answer": "N"
    }
    ]
}
