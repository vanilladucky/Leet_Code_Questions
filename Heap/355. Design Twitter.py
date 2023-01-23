# Honestly one of the most difficult problems I saw so far

class Twitter:

    def __init__(self):
        self.count = 0 # Keeping track of time/recent posts
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # More recent posts would have a lower count

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for follower in self.followMap[userId]:
            if follower in self.tweetMap:
                index = len(self.tweetMap[follower])-1
                count, tweetid = self.tweetMap[follower][index]
                heapq.heappush(minHeap, [count, tweetid, follower, index-1])

        while minHeap and len(res) < 10:
            count, tweetid, follower, index = heapq.heappop(minHeap)
            res.append(tweetid)
            if index >= 0:
                count, tweetid = self.tweetMap[follower][index]
                heapq.heappush(minHeap, [count, tweetid, follower, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
