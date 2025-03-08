"""
A piechart is used to represent data of a certain sample size out of a larger population. For example, a gaming company conducted a survey on what action and RPG games gamers love the most.
The question could be: "Which game do you like playing"

"""
import matplotlib.pyplot as plt

games = ["Fortnite", "Valorant", "CS:GO", "Call of Duty", "Rainbow Siege 6"]
votes = [50, 32, 83, 137, 24]
# Let's highlight votes for Call of Duty
explodes = [0, 0, 0, 0.1, 0]

plt.pie(votes, labels=games, explode=explodes, autopct='%.1f%%') # autopct='%.1f%%' shows the percentages of the votes as a part of the whole (100%)
plt.title("Favourite RPG/Action games as voted by gamers at GameCon")
plt.show()