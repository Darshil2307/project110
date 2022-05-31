import plotly.figure_factory as ff
import statistics as st
import random as rd
import pandas as pd

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

fig=ff.create_distplot([data],["reading Time"], show_hist=False)
fig.show()

population_mean=st.mean(data)
print("Mean of the population is", population_mean)

dataset = []
for i in range(0, 1000):
    rd_index=rd.randint(0, len(data))
    value=data[rd_index]
    dataset.append(value)

    mean=st.mean(dataset)
    sd = st.stdev(dataset)
    print('Mean of 1000 values', mean)
    print('Standard deviation of 1000 values', sd)
