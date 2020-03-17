import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import get_data

data = get_data.main()
data = data[data['Country/Region'] == 'US']
data = data[data['Province/State'] == 'Minnesota']
data_to_plot = data.get(['Province/State', 'date', 'n_cases'])
data_to_plot.plot()

plt.savefig('us_cases_by_state.pdf')
