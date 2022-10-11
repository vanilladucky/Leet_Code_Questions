#include <math.h>

bool increasingTriplet(int* nums, int numsSize){
    int first = INFINITY;
    int second = INFINITY;
    
    for (int i=0;i<numsSize;i++){
        if (nums[i] <= first){
            first = nums[i];
        }
        else if (nums[i] <= second){
            second = nums[i];
        }
        else {
            return true;
        }
    }
    
    return false;
}
