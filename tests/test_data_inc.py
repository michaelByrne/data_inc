from data_inc.data_inc import match
import random
import pytest

def test_num_assignments_short():
    n = 10
    m = 5
    assignments = match(n,m)
    for key, value in assignments.items():
        assert len(value) == m

def test_num_assignments_long():
    n = 100
    m = 99
    assignments = match(n,m)
    for key, value in assignments.items():
        assert len(value) == m

@pytest.mark.parametrize('execution_number', range(10))
def test_reviews_per_video(execution_number):
    n = 20
    m = 10
    assignments = match(n, m)
    video = random.randint(0,n)
    count = 0

    for key, value in assignments.items():
        print(value)
        if video in value:
            count += 1
    assert count == m

def test_bad_input():
    n = 10
    m = 10
    assignments = match(n,m)
    assert assignments == None
