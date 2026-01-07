def complaint_summary(df):
    return df.groupby('category').size().reset_index(name='count')

def average_resolution_time(df):
    return df.groupby('category')['resolution_time'].mean().reset_index()
