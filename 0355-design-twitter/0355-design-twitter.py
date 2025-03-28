class Twitter:

    def __init__(self):
        self.time = 1
        self.user = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user[userId].append([-self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if self.user[userId]:
            heap.append(self.user[userId][-1] + [userId, len(self.user[userId])-1])
        for people in self.follows[userId]:
            if self.user[people]:
                heappush(heap, self.user[people][-1] + [people, len(self.user[people])-1])
        res = []
        print(heap)
        for i in range(10):
            if not heap:
                break
            timer, postID, uid, idx = heappop(heap)
            res.append(postID)
            if idx > 0:
                idx -= 1
                heappush(heap, self.user[uid][idx] + [uid, idx])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)