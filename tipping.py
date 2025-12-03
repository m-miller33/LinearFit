import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from fitting_functions import *

filename = "tips.csv"
data = np.genfromtxt(filename, delimiter = ",", names = True)

x = data["Bill"]
y = data["Tip"]

slope, intercept, r, p, stderr = stats.linregress(x, y)

print_equation(slope, intercept, " dollars", "dollars")

plt.figure()
plt.plot(x, y, "o", label="Data")
plt.plot(x, slope*x + intercept, label="Linear fit")
plt.xlabel("Bill (dollars)")
plt.ylabel("Tip ( dollars)")
plt.show()

x2 = data["Bill"]
y2 = data["PctTip"]

slope2, intercept2, r2, p2, stderr2 = stats.linregress(x2, y2)

print_equation(slope2, intercept2, " dollars", "%")

plt.figure()
plt.plot(x2, y2, "o", label="Data")
plt.plot(x2, slope2*x2 + intercept2, label="Linear fit")
plt.xlabel("Bill ( dollars)")
plt.ylabel("Tip (%)")
plt.show()


# the tip verses bill has a strong and postive relationship meaning that higher bills tend
# to lead to higher tips.

# percent tip verses bill has a weak but positive relationship. the percent tipped does not
# change no matter the bill amount. 
