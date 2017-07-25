from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

import random

app = Flask(__name__)
if __name__ == '__main__':
    app.run()


@app.route('/')
def start():
    return render_template('main.html')

# A simple hander function to take form input and pass to matching function, returning assignments or None if invalue input

@app.route('/calcuate', methods=['POST'])
def handle_input():
    n = int(request.form['total'])
    m = int(request.form['choices'])
    assignments = {}
    if (n <= 0 or m <= 0):
        assignments = None
    else:
        assignments = match(n,m)
    return render_template('result.html', assignments=assignments)


# match function randomizes assignments by shuffling the student list and then iterating through it and assigning videos
# for each student as the next m videos in sequence.

def match(n,m):
    print(n,m)
    if (m >= n):
        return None
    else:
        students = list(range(0, n))
        random.shuffle(students)
        assignments = {}

        for k in range(0, n):
            index = k + 1
            # print('student {}'.format(k))
            student_assigns = []
            for j in range(0, m):
                if (index >= n):
                    index = 0
                student_assigns.append(students[index])
                index += 1
            key = students[k]
            assignments[key] = student_assigns
        print(assignments)
        return assignments
