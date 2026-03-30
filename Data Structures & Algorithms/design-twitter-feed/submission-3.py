class Twitter:
    def __init__(self):
        # O(N * m)
        # N := total number of userIds
        # m := max. tweets by any user
        self.userTweetMap = defaultdict(list)
        # O(N * m)
        # N := total number of userIds
        # M := max number of followees for any user
        self.userFolloweeMap = defaultdict(set)
        # O(n)
        # n := followeeIds associated with userId
        self.count = 0

    # O(1) Time
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    # O(nlogn) Time
    def getNewsFeed(self, userId: int) -> List[int]:
        # list of userIds the user follows
        listOfPeopleTheUserFollows = self.userFolloweeMap[userId]
        listOfPeopleTheUserFollows.add(userId)

        # get corresponding tweets associated with the list
        tweets = []
        for person in listOfPeopleTheUserFollows:
            for tweet in self.userTweetMap[person]:
                tweets.append(tweet)
        
        heapq.heapify(tweets)
        res = []
        while tweets and len(res) < 10:
            count, tweetId = heapq.heappop(tweets)
            res.append(tweetId)

        return res[:10]


    # O(1) Time
    def follow(self, followerId: int, followeeId: int) -> None:
        # you can fetch all the people a person follow with this now
        self.userFolloweeMap[followerId].add(followeeId)

    # O(1) Time
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFolloweeMap[followerId].discard(followeeId)