friends={'Bob','Rolf','Anne'}
abroad={'Bob','Anne'}

local_friends=friends.difference(abroad)
print(local_friends)
print('---------------------------------')

local_friends=friends.difference(abroad)
n_friend=local_friends=local_friends.union(abroad)
print(n_friend)
print('---------------------------------')


art={'Bob','Jen','Rolf','Charlie'}
science={'Bob','Jen','Adam','Anne'}

both= art.intersection(science)
print(both)
