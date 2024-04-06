"""
Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to all houses within that number of units distance away.

Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every house is within range of at least one transmitter. Each transmitter must be installed on top of an existing house.

Example


antennae at houses and and provide complete coverage. There is no house at location to cover both and . Ranges of coverage, are , , and

.

Function Description

Complete the hackerlandRadioTransmitters function in the editor below.

hackerlandRadioTransmitters has the following parameter(s):

    int x[n]: the locations of houses
    int k: the effective range of a transmitter

Returns

    int: the minimum number of transmitters to install

https://www.hackerrank.com/challenges/one-month-preparation-kit-hackerland-radio-transmitters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four 
"""

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x = sorted(x)
    res = 0
    while x:
        i = x[0]
        j = i + k
        while j not in x:
            j -= 1
        for idx in range(len(x)):
            if x[0] in range(j-k, j+k+1):
                x.pop(0)
            else:
                break
        res += 1
    return res