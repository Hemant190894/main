import sys
from datetime import datetime
import pandas as pd
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utilss.constants import SECRET_APP, CLIENT_ID, USER_AGENT, OUTPUT_PATH


def reddit_pipeline(file_name: str, subreddit: str, limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET_APP, USER_AGENT)
    # extraction
    print("******* INSERTING INTO Extract Function *******")
    posts = extract_posts(instance, subreddit, limit)
    print("******* EXIT FROM Extract Function *******")
    if posts:
        print("******* EXIT FROM Extract Function *******")
        post_df = pd.DataFrame(posts)
        # Transformation
        post_df = transform_data(post_df)
        print(post_df)
        # Loading to CSV
        file_path = f'{OUTPUT_PATH}/{file_name}.csv'
        load_data_to_csv(post_df, file_path)
    else:
        print("No posts were extracted.")


if __name__ == "__main__":
    file_postfix = datetime.now().strftime("%Y%m%d")
    subreddit = "Python"
    limit = 1
    reddit_pipeline(file_postfix,subreddit, limit)