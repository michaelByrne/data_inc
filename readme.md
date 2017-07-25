The data_inc app takes in 2 parameters from a simple web form.
n is the total number of students, m is the number of videos each student is to watch.

The matching function operates by first shuffling the student roster, a basic list of integers.
It iterates through the class roster once per student.
If m videos are to be watched per student, then the next m videos in sequence are selected.
If the end of the list is reached, the index wraps around to the beginning.

For example:

n = 5
m = 3

student roster: 1 2 3 4 5
shuffled: 2 1 5 3 4

Student 5 watches 3, 4, and 2.


I think this implementation is almost unavoidable given the requirements. In a relatively "sparse" scenario where, say, 20 students each only watch two videos, it seems reasonable to select random videos at a per-student level--checking that videos haven't already been assigned and for self-assignment--but in the worst case where each of those students must watch 19 videos, satisfying the constraints means per-student randomization converges on the implementation above. Visualizing the problem as a graph makes this clear. 

The match function runs in worst-case n^2 time, but could be improved to linear time using Python list comprehension
in place of the inner loop. Its worst case space complexity is also n^2.

From the root folder, the matching function can be tested by 'pytest tests/test_data_inc.py' 
