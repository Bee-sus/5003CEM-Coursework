from Graph import Graph
class SocialMediaApp:

    def __init__(self):
        self.graph = Graph()
        self.users = {}  # Dictionary to store Person objects by user_id

    def addUser(self, person):
        # Add a new user to the social media app but limit the system to 10 users only
        if len(self.users) >= 10:
            print("There is a maximum limit of 10 users and it has been reached.")
            return False
        self.users[person.user_id] = person
        self.graph.addVertex(person.user_id)
        return True
    def followUser(self, follower_id, followee_id):
        # ake one user follow another
        return self.graph.addEdge(follower_id, followee_id)

    def getFollowing(self, user_id):
        # Get list of users that a person is following
        following_ids = self.graph.getToAdjVertex(user_id)
        return [self.users[uid] for uid in following_ids if uid in self.users]

    def getFollowers(self, user_id):
        # Get list of users that follow a person
        follower_ids = self.graph.getFromAdjVertex(user_id)
        return [self.users[uid] for uid in follower_ids if uid in self.users]

    def getAllUsers(self):
        # Get all users in the app
        return list(self.users.values())

    def getUser(self, user_id):
        # Get a specific user by ID
        return self.users.get(user_id)
