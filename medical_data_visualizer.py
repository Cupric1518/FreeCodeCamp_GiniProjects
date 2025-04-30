import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 

# 1
df = pd.read_csv('medical_examination.csv',sep=',', header=0)

# 2
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2) > 25

# 3
df['overweight'] = df['overweight'].astype(int)
df['overweight'] = np.where((df['cholesterol'] <= 1) & (df['gluc'] <= 1), 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar', 
        height=5, 
        aspect=1
    )


    # 8
    fig.set_axis_labels('variable', 'total')


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()
    df_heat = df_heat[(df_heat['ap_lo'] <= df_heat['ap_hi']) & (df_heat['height'] >= df_heat['height'].quantile(0.025)) & (df_heat['height'] <= df_heat['height'].quantile(0.975)) & (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr(method='pearson')

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 8))


    # 15
    sns.heatmap(
		corr, 
		mask=mask, 
		annot=True, 
		fmt='.1f', 
		linewidths=.5, 
		cmap='coolwarm', 
		cbar_kws={"shrink": .8}, 
		ax=ax
	)


    # 16
    fig.savefig('heatmap.png')
    return fig
