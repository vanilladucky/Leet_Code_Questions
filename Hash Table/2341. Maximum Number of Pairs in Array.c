int* numberOfPairs(int* nums, int numsSize, int* returnSize){
   int cnt[101] = {};
   int i, left = 0;
   for(i = 0; i < numsSize; i++)
   {
       cnt[nums[i]]++;
   }
   for(i = 0; i < 101; i++)
   {
       left += (cnt[i] & 0x1);
   }
   
   int *ret = (int*)malloc(2 * sizeof(int));
   *returnSize = 2;
   ret[1] = left;
   ret[0] = (numsSize - left) >> 1;
   
   return ret;
}
