"""
Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user and is able to see the 10 most recent tweets
in the user's news feed. Your design should support the following methods:

1. postTweet(userId, tweetId): Compose a new tweet.

2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's
     news feed. Each item in the news feed must be posted by users who the user
     followed or by the user herself. Tweets must be ordered from most recent
     to least recent.

3. follow(followerId, followeeId): Follower follows a followee.

4. unfollow(followerId, followeeId): Follower unfollows a followee.
"""

from collections import defaultdict
from itertools import chain
from time import time


class Twitter:
    """
    Runtime: 68 ms, faster than 76.24% of Python3.
    Memory Usage: 20.5 MB, less than 5.23% of Python3.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.followers = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append({'id': tweetId, 'timestamp': time()})

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user
        followed or by the user herself.

        Tweets must be ordered from most recent to least recent.
        """
        followers_tweets = list(chain.from_iterable(
            self.tweets[followerId] for followerId in self.followers[userId]
            ))
        all_tweets = self.tweets[userId] + followers_tweets
        all_tweets_sorted = sorted(all_tweets, key=lambda post: post['timestamp'], reverse=True)
        return [tweet['id'] for tweet in all_tweets_sorted][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].remove(followeeId)


if __name__ == "__main__":
    tw1 = Twitter()
    tw1.postTweet(1, 5)
    assert tw1.getNewsFeed(1) == [5]
    tw1.follow(1, 2)
    tw1.postTweet(2, 6)
    assert tw1.getNewsFeed(1) == [6, 5]
    tw1.unfollow(1, 2)
    assert tw1.getNewsFeed(1) == [5]

    tw2 = Twitter()
    tw2.postTweet(1, 5)
    tw2.postTweet(1, 3)
    assert tw2.getNewsFeed(1) == [3, 5]

    tw3 = Twitter()
    tw3.postTweet(1, 5)
    tw3.follow(1, 1)
    assert tw3.getNewsFeed(1) == [5]

    tw4 = Twitter()
    tw4.postTweet(1, 5)
    tw4.postTweet(1, 3)
    tw4.postTweet(1, 101)
    tw4.postTweet(1, 13)
    tw4.postTweet(1, 10)
    tw4.postTweet(1, 2)
    tw4.postTweet(1, 94)
    tw4.postTweet(1, 505)
    tw4.postTweet(1, 333)
    tw4.postTweet(1, 22)
    tw4.postTweet(1, 11)
    assert tw4.getNewsFeed(1) == [11,22,333,505,94,2,10,13,101,3]
