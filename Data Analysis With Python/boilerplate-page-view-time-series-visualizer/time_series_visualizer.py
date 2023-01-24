import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'Data Analysis With Python\boilerplate-page-view-time-series-visualizer\fcc-forum-pageviews.csv', index_col='date',parse_dates=True)#parse_dates=[0] or parse_dates=['date']

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(df.index,df['value'],color='red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # df_bar['year'] = pd.DatetimeIndex(df_bar.index).year  # you won't have to use reset index here
    # df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar.reset_index(inplace=True)
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    fig = df_bar.plot.bar()
    fig.legend(months, title='Months', prop={'size': 5})
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.tight_layout()
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month
    df_box['month_name'] = df_box['date'].dt.month_name().str[:3]
    df_box = df_box.sort_values('month')

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(28.8, 10.8))

    ax[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])

    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    sns.boxplot(data=df_box, x='month_name', y='value', ax=ax[1])

    for axes in range(len(ax.flat)):
        if axes==0:
            xlabel = 'Year'
        else:
            xlabel = 'Month'
        ylabel = 'Page Views'
        ax.flat[axes].set(xlabel=xlabel, ylabel=ylabel)

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
