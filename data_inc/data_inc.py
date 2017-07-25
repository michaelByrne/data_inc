from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

import random

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('main.html')

@app.route('/calcuate', methods=['POST'])
def handle_input():
    n = int(request.form['total'])
    m = int(request.form['choices'])
    assignments = match(n,m)
    return render_template('result.html', assignments=assignments)



if __name__ == '__main__':
    app.run()

def match(n,m):
    print(n,m)
    if (m >= n):
        return None
    else:
        students = list(range(0, n))
        random.shuffle(students)
        assignments = {}
        print(students)

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
