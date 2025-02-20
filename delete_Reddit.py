import praw
import time

# Fill in your Reddit API credentials here
CLIENT_ID = "add yours"
CLIENT_SECRET = "add yours"
USERNAME = "add yours"
PASSWORD = "add yours"
USER_AGENT = "script:delete_upvotes:v1.0 (by u/your_username)"

# Authenticate with Reddit
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT
)

# Function to remove upvotes
def clear_upvotes():
    print("Removing upvotes...")
    for submission in reddit.user.me().upvoted(limit=None):
        try:
            submission.clear_vote()
            print(f"Removed upvote from: {submission.title}")
            time.sleep(2)  # Avoiding API rate limits
        except Exception as e:
            print(f"Error removing upvote: {e}")

# Function to delete all comments
def delete_comments():
    print("Deleting comments...")
    for comment in reddit.user.me().comments.new(limit=None):
        try:
            comment.delete()
            print("Deleted a comment.")
            time.sleep(2)
        except Exception as e:
            print(f"Error deleting comment: {e}")

# Function to delete all posts
def delete_posts():
    print("Deleting posts...")
    for submission in reddit.user.me().submissions.new(limit=None):
        try:
            submission.delete()
            print(f"Deleted post: {submission.title}")
            time.sleep(2)
        except Exception as e:
            print(f"Error deleting post: {e}")


def delete_saved():
    print("Un-saving all saved posts...")
    for saved in reddit.user.me().saved(limit=None):
        try:
            saved.unsave()
            print(f"Un-saved: {saved.title if hasattr(saved, 'title') else 'a comment'}")
            time.sleep(2)
        except Exception as e:
            print(f"Error un-saving: {e}")



# Execute the functions
clear_upvotes()
delete_comments()
delete_posts()
delete_saved()
print("All upvotes, comments, saved, and posts have been deleted.")
