import matplotlib.pyplot as plt

"""
Bar graphs are used to visualize categorical data, let's say responses to a survey carried out in a university
investigating what programming languages do students use.
Case: A student can use Python and Go at the same time.

"""

langs = ["Rust", "C++", "C#", "C", "Python", "Java", "Javascript", "Go"]
votes = [18, 9, 10, 22, 104, 4, 82, 15]

plt.bar(langs, votes, color='black')
plt.title("Programming languages that students at Kenyatta University use")
plt.ylabel("Votes")
plt.xlabel("Languages")
plt.show()