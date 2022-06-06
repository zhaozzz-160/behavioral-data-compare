from matplotlib import pyplot as plt


def plot(df):

    plt.plot(df.index, df[['value1', 'value2']])