int* sortArrayByParity(int* nums, int numsSize, int* returnSize){
    int* res = (int*)malloc(sizeof(int)*numsSize);
    int i = 0;
    int l = 0;
    int r = numsSize-1;
    
    for (i=0; i<numsSize; i++){
        if (nums[i] % 2 == 0){
            res[l] = nums[i];
            l++;
        }
        else {
            res[r] = nums[i];
            r--;
        }
    }
    *returnSize = numsSize;
    return &res[0];
}
