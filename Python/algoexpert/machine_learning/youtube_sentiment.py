def get_youtube_sentiment(video_stats_df):
    video_stats_df["sentiment"] = video_stats_df["likes"] / (
        video_stats_df["dislikes"] + video_stats_df["likes"]
    )
    mean_sentiment = (
        video_stats_df.groupby("category_id")["sentiment"]
        .mean()
        .sort_values(ascending=False)
    )

    return mean_sentiment
