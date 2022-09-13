#define TABLE_SIZE 10000

typedef struct hash {
    int value;
    int index;
    struct hash *next;
} hash;

hash *hash_table[TABLE_SIZE];

void init_hash_table()
{
	for (int i = 0; i < TABLE_SIZE; i++)
		hash_table[i] = NULL;
}

unsigned int hash_function(int key)
{
    unsigned int hash_value;
    hash_value = key > 0 ? (key) % TABLE_SIZE : (key * -1) % TABLE_SIZE;
    return hash_value;
}

hash *new_node(int value, int index)
{
    hash *temp = (hash*)malloc(sizeof(hash));
    temp->value = value;
    temp->index = index;

    return temp;
}

void hash_table_insert(int v, int i)
{
    int index = hash_function(v);
	
	hash *node = new_node(v, i);
	node->next = hash_table[index];
    hash_table[index] = node;

}

hash *hash_table_lookup(int key)
{
      int index = hash_function(key);
      hash *curr = hash_table[index]; 
      
      while (curr && curr->value != key)
          curr = curr->next;
      
      return curr;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){

    *returnSize = 2;
    int *result = malloc(*returnSize * sizeof(int));
    init_hash_table();

    for (int i = 0; i < TABLE_SIZE; i++)
    {
        int diff = target - nums[i];
        hash *check = hash_table_lookup(diff);

        if ((check != NULL) && (check->value + nums[i] == target) && (check->index != i))
        {
            result[0] = check->index;
            result[1] = i;
            return result;
        } 
        
        hash_table_insert(nums[i], i);
    }
    
    //pretend I call a function here that frees the nodes in hash_table
    
    return 0;
}
