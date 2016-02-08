from __future__ import division
from collections import Counter
from collections import defaultdict

# A database of users. Each user is represented
# as a dictionary.
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# An array of tuples signifying friendships.
# For example, the tuple (0,1) indicates the
# user with id=0 and the user with id=1 are friends.
friendships = [
    (0, 1), (0, 2), (1, 2),
    (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7),
    (6, 8), (7, 8), (8, 9)
]

###
# QUESTION: How many friends does a typical user have?
###

# (1) Add a `friends` collection for each user.
for user in users:
    user["friends"] = []

# (2) Create the friendship both ways.
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    """How many friends does a yser have?"""
    return len(user["friends"])

# (3) Find total number of connections by summing up
#     the lengths of all the friends lists.
total_connections = sum(number_of_friends(user)
                        for user in users)

# (4) Then we divide by the number of users.
num_users = len(users)
avg_connections = total_connections / num_users

print("Connections per user (mean): {}".format(avg_connections))

###
# QUESTION: Who are the key connectors within
# the user base? (These are the people with the
# largest friends lists in the database.)
###

# (1) Create a list of tuples of type (user_id, num_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]


# (2) Sort it largest to smallest
sorted_list = sorted(num_friends_by_id,
                     key=lambda (user_id, num_friends): num_friends,
                     reverse=True)

print "Connections sorted DESC (degree centrality): {}".format(sorted_list)

###
# QUESTION: How do we encourage more connections among our members?
###

def friends_of_friend_ids_bad(user):
    return [foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]]

# Show friends of friends for user 0
print("Friend of friends for user 4 (BAD): {}".format(friends_of_friend_ids_bad(users[3])))

# Here's a better implementation
def not_the_same(user, other):
    return user["id"] != other["id"]

def not_friends(user, other):
    return all(not_the_same(friend, other)
                for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
        for friend in user["friends"]  # for each of my friends
        for foaf in friend["friends"]  # count *their* friends
        if not_the_same(user, foaf)    # who aren't the same
        and not_friends(user, foaf))   # and who aren't my friends

# This correctly tells Chi (id 3) that she has two mutual friends
# with Hero (id 0) but only one mutual friend with Clive (id 5).
print(friends_of_friend_ids(users[3]))

###
# QUESTION: How do we match people up based on common interests?
###

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

print(data_scientists_who_like("Big Data"))

# Let's build an index of a search term and the users who are interested in it
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"])

print(most_common_interests_with(users[0]))

# Salary data
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}

print(average_salary_by_bucket)


###
# QUESTION: How popular are certain interests across the user base?
###

words_and_counts = Counter(word
    for user, interest in interests
    # (1) Lowercase each interest
    # (2) Split it into words
    for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    # (3) Count it
    if count > 1:
        print word, count
