import matplotlib.pyplot as plt

labels = ['Math', 'Science', 'English', 'History']
sizes = [25, 35, 20, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Subject Distribution")
plt.show()
