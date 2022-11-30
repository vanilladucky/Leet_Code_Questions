int findMin(int* nums, int numsSize){
    int left = 0;
    int right = numsSize-1;
    int middle;
    int min = 5001;
    
    while (left<=right){
        middle = floor((left+right)/2);
        
        min = nums[middle] < min ? nums[middle] : min;
        
        if (nums[middle] < nums[right]){
            right = middle - 1;
        }
        else {
            left = middle + 1;
        }
    }
    
    return min;
}
