class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # the user who we're following's count increases by one.
        user.followers += 1
        # the primary user's "following" count increases by one.
        self.following += 1

# creating a single object..
# user_1 = User()
# creating individual attributes..
# user_1.id = "001"
# user_1.username = "Natalie"

user_1 = User("001", "Natalie")
user_2 = User("002", "Katie")

user_1.follow(user_2)


