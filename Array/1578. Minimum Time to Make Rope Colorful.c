#define MAX(a,b) ((a>b)?a:b)

int minCost(char * colors, int* neededTime, int neededTimeSize){
    int i = 0;
    int j = 0;
    int res = 0;
    
    while (i < neededTimeSize && j < neededTimeSize){
        int curr_sum = 0;
        int curr_max = 0;
        
        while (j < neededTimeSize && colors[i] == colors[j]){
            curr_sum += neededTime[j];
            curr_max = MAX(curr_max, neededTime[j]);
            j += 1;
        }
        
        res += (curr_sum - curr_max);
        i = j;
    }
    
    return res;
}
