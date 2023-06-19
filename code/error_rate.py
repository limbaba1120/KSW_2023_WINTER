# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
data = pd.read_csv('error_rate.csv')

df = pd.DataFrame(data)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]    
df = df.drop(labels=2, axis=0)
# erase Nan column and row

df = df.set_index('label')
figure = df.plot(kind='bar', rot=0, xlabel="", ylabel="No connection Count", legend=None, title='Total number of message not received')
for container in figure.containers:     # for easy understanding, added value on the graph
    figure.bar_label(container)
plt.show()