import seaborn as sns
sns.set_theme()
fmri = sns.load_dataset("fmri")
sns.replot(
    data=fmri,kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",

)