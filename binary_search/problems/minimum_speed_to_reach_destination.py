'''
problem:
--------

Geek is travelling from Geek Land to Destination Land. He has access to a magical spells that can boost his car's speed. 
Each spell, when cast at the exact time spells[i], instantly increases the car's speed to k meters per second and then decreases 
by 1 meter per second until it reaches 0.
Geek needs to cover at least trackLength distance to reach Destination Land. Help him find the minimum value of k required 
to complete the journey.

Example 1:

Input: tracklength = 20

n = 3 
spells = [1, 5, 9]
Output = 4

Explanation: Geek casts a spell at time 1, his car's speed reaches k = 4 m/s. During the 1st second, the car moves 1 meters, 
3 meters in the 2nd second, 2 meters in the 3rd second, and 1 meter in the 4th second. By then, his car has moved a total of 10 meters. If he casts the spell again in the 5th second, the car will move another 10 meters, completing the trackLength.

Example 2:

Input: trackLength = 10

Spells = [3, 4, 5]

Output: 3

Explanation: At time = 1 and 2, Geek is not able to cast any spells and car remain stationary. Geek casts the first spell at time = 3, 
making his car's speed 3 m/s. At time = 4 and 5, he casts additional spells to maintain a speed of 3 m/s. During the 6th second, 
the car's speed reduces to 2 m/s, helping it move 2 more meters and complete the trackLength

Your Task:
This is a functional problem, input/output is handled by driver code. You need to complete the function minimize Top Speed 
so that accepts three arguments, int n, array spells[] and distance trackLength. Return the minimum value of K required 
to complete the journey.

'''


def calculateLength(n, a, d):
  sum = (n/2) * ( (2 * a) + (n -1 ) * d) # AP sum
  print(f"sum: {sum}")
  return sum

def isTrackCovered(track_length, spells, k):
  track_covered = 0
  for i in range(1, len(spells)):
    track_covered += calculateLength(n=spells[i]-spells[i-1], a=k, d=-1)
  track_covered += calculateLength(n=k, a=k, d=-1)
  print(f"track_covered: {track_covered}")
  return track_length <= track_covered


def minimumSpeedToCompleteJourney(track_length, spells):
  
  if len(spells) == 1:
    return track_length

  high = track_length
  low = spells[1] - spells[0]

  while low <= high:
    mid = (high + low) // 2

    if isTrackCovered(track_length, spells, mid):
      high = mid - 1
    else:
      low = mid + 1

  return low


k = minimumSpeedToCompleteJourney(20, [1, 5, 9])

print(f"final answer: {k}")
