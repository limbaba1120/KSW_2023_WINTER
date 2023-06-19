# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
data = pd.read_csv('total_env.csv')

df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax2 = ax.twinx()            # two graphs in the same page
df['rssi'] += 180           # convert RSSI to positive value, to present them (0, -140, -120 ..)


df.groupby(['label', 'type'], sort=False)['count'].sum().unstack().plot(rot=0, kind='bar',  ax=ax, legend=False, width=0.3, color=['#006699', '#FFCC33'])   
# represent the connection counts with bar plot
df.groupby(['label', 'type'], sort=False)['rssi'].sum().unstack().plot(rot=0, ax=ax2, style=["r^-", "bs-"], ms=10, ylabel="RSSI (dBm)")
# represent RSSI in each connections with line plot

ax.legend(bbox_to_anchor=(0, 1.02, 0.5, 0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=2, title='The number of message received')
# displace a legend of bar graph
ax2.legend(bbox_to_anchor=(0.51,1.02,0.5,0.2), title='Average RSSI', loc="lower left", mode="expand", borderaxespad=0, ncol=2)
# displace a legend of line graph

for container in ax.containers:
    ax.bar_label(container)         # for easy understanding, show count value in graph

ax.set_ylim(0,24)                    # count limit is 0~3
ax2.set_yticklabels([0, -130, -120, -110, -100, -90, -80, -70])      # to show low RSSI is better
plt.tight_layout()
plt.subplots_adjust()
ax.set_xlabel("")

plt.show()