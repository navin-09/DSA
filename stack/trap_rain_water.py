def trap_rain_water(height):
    n = len(height)
    if n < 3:
        return 0
    left = 0
    right = len(height)-1
    lmax = 0
    rmax = 0
    traped_water = 0
    while left < right:
        if (height[left] < height[right]):
            if(height[left] >= lmax):
                lmax = height[left]
            else:
                traped_water += (lmax - height[left])

            left+=1
        else:
            if(height[right] >= rmax):
                rmax = height[right]
            else:
                traped_water += (rmax - height[right])
            right -=1

    return traped_water

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_rain_water(heights))  # Output: 6

