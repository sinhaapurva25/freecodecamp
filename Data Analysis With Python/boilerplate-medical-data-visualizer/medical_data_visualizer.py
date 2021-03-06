import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r'Data Analysis With Python\boilerplate-medical-data-visualizer\medical_examination.csv')

# Add 'overweight' column
df.loc[(df['weight']/((df['height']/100)*(df['height']/100))) > 25, 'overweight'] = 1
df.loc[(df['weight']/((df['height']/100)*(df['height']/100))) <= 25, 'overweight'] = 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[(df['cholesterol'] == 1), 'cholesterol'] = 0
df.loc[(df['cholesterol'] > 1), 'cholesterol'] = 1
df.loc[(df['gluc'] == 1), 'gluc'] = 0
df.loc[(df['gluc'] > 1), 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars = ['cardio'], value_vars=['active','alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'
    df_cat = sns.catplot(x='variable', hue='value', data=df_cat,col='cardio', kind="count").set_ylabels("total")
    plt.figure(figsize=(20,20))
    fig = df_cat.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # df_heat = df[((df['ap_lo'] <= df['ap_hi']) &
    #              (df['height'] >= df['height'].quantile(0.025)) &
    #              (df['height'] >= df['height'].quantile(0.975)) &
    #              (df['weight'] >= df['weight'].quantile(0.025)) &
    #              (df['weight'] >= df['weight'].quantile(0.975)))
    #              ]
    df_heat = (df['ap_lo'] > df['ap_hi'])| (df['height'] < df['height'].quantile(0.025)) | (df['height'] > df['height'].quantile(0.975)) | (df['weight'] < df['weight'].quantile(0.025)) | (df['weight'] > df['weight'].quantile(0.975))

    # Calculate the correlation matrix
    corr = df.drop(df[df_heat].index).reset_index(drop=True).corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    plt.figure(figsize = (11,9))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask,annot=True,fmt=".1f")
    fig = ax.get_figure()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
