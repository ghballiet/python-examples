# Grading Sheet #

When I was taught at ASU, there were about 97 students enrolled in the four
labs of Intro to C++ that I was teaching. A lab assignment was due every
class, and we met twice a week. This meant that I had to review almost a
hundred lab submissions over two days, grade them, and (because of university
requirements) give each student a written report outlining their grade.

I wrote this simple utility to make that process a lot easier for myself. It
reads through a CSV file of students and their scores on each part of the
rubric, and generates LaTeX code for reports for each students. I could then
just compile all the LaTeX files with BASH script, and I had nicely formatted
PDF reports.

If it looks incomplete, it's because I had to delete several files containing
actual assignment and student information.
