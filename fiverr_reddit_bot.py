# by John Hadden
import praw
import random
import time  # the modules needed for the script

# the code to access praw and login to reddit
reddit = praw.Reddit(client_id='LsDR_-EEXqr-xA',
                     client_secret='UIzmQDXm4uG-_SIjGc1PBdvDw78',
                     user_agent='reddit bot for a client on 5iverr',
                     username='Interesting-Parsnip4',
                     password='SwagKing69', )
titles = ['hello', 'title', 'title3']  # the titles, you can add more to this
old_titles = []  # where the titles are put once they have been used
# you can see them using print(old_titles)
post_text = ['this is a post', 'as is this', 'and so is this']  # the post text, you can also add more to this
old_postText = []  # where the used post_texts are put


def post(): # declares a function
    for i in range(len(titles)):        # keeps on looping through the below code, as many times as the length of the
        # titles array
        sleeper = random.randint(1, 86400)  # causes the loop to execute again at a random time between 1 and 86400
        # seconds (24 hours)
        time.sleep(sleeper)
        global subreddits     # declares the subreddits variable
        global pos
        int1 = random.randint(0, len(titles) - 1)   # gets a random number for the titles
        title = (titles[int1])     # declares a random member of titles to use in the post
        titles.remove(title)      # removes it from the titles array
        old_titles.append(title)   # adds it to the old_titles array
        int2 = random.randint(0, len(post_text) - 1)   # does the same again except with the post_text
        post = (post_text[int2])
        post_text.remove(post)
        old_postText.append(post)

        subreddit = reddit.subreddit('worldpowers')   # declares the subreddit that you want to do this on
        subreddit.submit(title, post)  # posts the post


post()  # calls the function post