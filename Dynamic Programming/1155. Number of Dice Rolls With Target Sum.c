int dict[31][1001][2];

int dfs(int n, int k, int target){   
    if (target == 0 && n == 0){
        return 1;
    }
    
    if (target <= 0){
        return 0;
    }
    if (n <= 0){
        return 0;
    }
    
    if (dict[n][target][0]){
        return dict[n][target][1];
    }
    
    int out = 0;
    for (int i = 1; i <= k; i++) {
        out += dfs(n-1, k, target-i);
        out %= 1000000007;
    }
    
    dict[n][target][0] = 1;
    dict[n][target][1] = out;
    
    return out;   
}

int numRollsToTarget(int n, int k, int target){
    memset(dict, 0, sizeof(dict));

    return dfs(n, k, target);
}
