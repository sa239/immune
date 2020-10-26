# imports
from instapy import InstaPy
from instapy import smart_run
import random 

# login credentials
insta_username = '@gmail.com'
insta_password = '!'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    hashtags = ['footballmeme', 'manchesterunited', '433',
                'manchestercity',
                'chelsea', 'meme', 'epl',
                'everton', 'arsenal',
                'fcbarcelona', 'neymar', 'psg',
                'messi',
                'ronaldo', 'sports', 'soccermeme', 'TrollFootball',
                'Goal',
                'Cristiano', 'FIFA21', 'Football', 'Juventus',
                'thegreatoutdoors']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression','animals'])
    session.set_do_follow(enabled=True, percentage=80, times=1)
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([
                             u'What an amazing shot! :heart_eyes: What do '
                             u'you think of my recent shot?',
                             u'What an amazing shot! :heart_eyes: I think '
                             u'you might also like mine. :wink:',
                             u'Wonderful!! :heart_eyes: Would be awesome if '
                             u'you would checkout my photos as well!',
                             u'Wonderful!! :heart_eyes: I would be honored '
                             u'if you would checkout my images and tell me '
                             u'what you think. :wink:',
                             u'This is awesome!! :heart_eyes: Any feedback '
                             u'for my photos? :wink:',
                             u'This is awesome!! :heart_eyes:  maybe you '
                             u'like my photos, too? :wink:',
                             u'I really like the way you captured this. I '
                             u'bet you like my photos, too :wink:',
                             u'I really like the way you captured this. If '
                             u'you have time, check out my photos, too. I '
                             u'bet you will like them. :wink:',
                             u'Great capture!! :smiley: Any feedback for my '
                             u'recent shot? :wink:',
                             u'Great capture!! :smiley: :thumbsup: What do '
                             u'you think of my recent photo?'],
                         media='Photo')
                         
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_tags(my_hashtags, amount=90, media=None)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='sports', engagement_mode='no_comments')