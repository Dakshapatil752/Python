import matplotlib.pyplot as plt

names = ['Daksha', 'Raj', 'Sneha', 'jay']
marks = [85, 90, 78, 92]

plt.bar(names, marks, color='orange')
plt.title("Students' Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()
