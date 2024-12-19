# einfachere Variante
""" import csv


turbinedata=[]

with open('10m.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        turbinedata.append(line)


print(turbinedata, "\n")

winddata=[x[0] for x in turbinedata]
print()
print(winddata, "\n")
wdsplit=[str(x).split(";") for x in winddata]
print()
print(wdsplit, "\n")
avgWind=[float(x[0]) for x in wdsplit]
print()
print(avgWind, "\n")
avgPower=[float(x[3])/200 for x in wdsplit]
print()
print(avgWind, "\n", avgPower)


from matplotlib import pyplot as plt

axx=[x for x in range(144)]

plt.plot(axx, avgWind, avgPower)

plt.show() """

# bessere Variante: Zwei x- Achsen
import csv
from matplotlib import pyplot as plt    # Beachte: Wenn matplotlib noch nicht installiert:
                                        # Terminal: pip install matplotlib
turbinedata = []

# Read the CSV file
with open('C:\\Users\\StefanKoschnik\\OneDrive - karriere tutor GmbH\\Dokumente\\Python\\PYKT20240513\\PYKT20240513\\9_CSV und Matplotlib\\Turbinendaten\\10m.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header
    for line in csv_reader:
        turbinedata.append(line)

# Extract wind and power data
winddata = [x[0] for x in turbinedata]
wdsplit = [str(x).split(";") for x in winddata]
avgWind = [float(x[0]) for x in wdsplit]
avgPower = [float(x[3]) for x in wdsplit]  # No division by 200

# X-axis (assuming 144 points)
axx = [x for x in range(144)]

# Create the plot
fig, ax1 = plt.subplots()

# Plot avgWind on the first y-axis
ax1.set_xlabel('Time (Index)')
ax1.set_ylabel('Average Wind Speed', color='tab:blue')
ax1.plot(axx, avgWind, color='tab:blue', label="Avg Wind Speed")
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for avgPower
ax2 = ax1.twinx()
ax2.set_ylabel('Average Power', color='tab:red')
ax2.plot(axx, avgPower, color='tab:red', label="Avg Power")
ax2.tick_params(axis='y', labelcolor='tab:red')

# Show the plot
plt.title('Wind Speed and Power Output')
fig.tight_layout()
plt.show()