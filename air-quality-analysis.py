import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": [1, 2, 3, 4, 5],
    "AQI": [45, 52, 61, 58, 70]
}

df = pd.DataFrame(data)

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": [1, 2, 3, 4, 5],
    "AQI": [45, 52, 61, 58, 70]
}

df = pd.DataFrame(data)

plt.plot(df["Day"], df["AQI"], marker="o")
plt.title("Air Quality Index Over Time")
plt.xlabel("Day")
plt.ylabel("AQI")

plt.savefig("aqi_plot.png")

plt.show()

