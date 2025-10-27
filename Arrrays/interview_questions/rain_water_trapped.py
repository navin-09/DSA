def trap_two_pointer(height):
    left=0
    right=len(height)-1

    lmax = 0
    rmax = 0

    total_water_trapped = 0

    while(left<right):
        if(height[left]<=height[right]):
            if(height[left]>=lmax):
                lmax = height[left]
            else:
                total_water_trapped += lmax - height[left]
            left+=1
        else:
            if(height[right]>=rmax):
                rmax = height[right]
            else:
                total_water_trapped += rmax - height[right]
            right-=1
    return total_water_trapped


print(trap_two_pointer([0,1,0,2,1,0,1,3,2,1,2,1]))  # -> 6
