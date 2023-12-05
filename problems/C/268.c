struct HashNode {
    int num;
    UT_hash_handle hh;
};

struct HashTable {
    struct HashNode* table;
};

struct HashTable* createHashTable() {
    struct HashTable* hashtable = malloc(sizeof(struct HashTable));
    if (hashtable != NULL) {
        hashtable->table = NULL;
    }
    return hashtable;
}

void insert(struct HashTable** hashtable, int num) {
    struct HashNode* newNode = malloc(sizeof(struct HashNode));
    newNode->num = num;

    HASH_ADD_INT((*hashtable)->table, num, newNode);
}

void freeHashTable(struct HashTable* hashtable) {
    struct HashNode *current, *tmp;
    HASH_ITER(hh, hashtable->table, current, tmp) {
        HASH_DEL(hashtable->table, current);
        free(current);
    }
    free(hashtable);
}

int missingNumber(int* nums, int numsSize) {
    struct HashTable* hashtable = createHashTable();

    for (int i = 0; i < numsSize; ++i) {
        insert(&hashtable, nums[i]);
    }

    for (int i = 0; i <= numsSize; ++i) {
        struct HashNode* result = NULL;
        HASH_FIND_INT(hashtable->table, &i, result);
        if (result == NULL) {
            freeHashTable(hashtable);
            return i;
        }
    }

    freeHashTable(hashtable);
    return -1;
}
