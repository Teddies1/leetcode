


typedef struct Trie{
    struct Trie *alphabet[26];
    bool marker;
} Trie;


Trie* trieCreate() {
    Trie *root = malloc(sizeof(Trie));
    for (int i = 0; i < 26; i++){
        root->alphabet[i] = NULL;
    }
    root->marker = false;
    return root;
}

void trieInsert(Trie* obj, char *word) {
    int letter;
    int i = 0;
    while (word[i] != '\0'){
        letter = word[i] - 'a';
        if (obj->alphabet[letter] == NULL){
            Trie *newnode = trieCreate();
            obj->alphabet[letter] = newnode;
        }
        obj = obj->alphabet[letter];
        i++;
    }
    obj->marker = true;
}

bool trieSearch(Trie* obj, char *word) {
    int i = 0, letter;
    while(word[i] != '\0'){
        letter = word[i] - 'a';
        if (obj->alphabet[letter] == NULL){
            return false;
        }
        obj = obj->alphabet[letter];
        i++;
    }
    if (obj->marker && obj != NULL){
        return true;
    }
    return false;
}

bool trieStartsWith(Trie* obj, char *prefix) {
    int i = 0, letter;
    while(prefix[i] != '\0'){
        letter = prefix[i] - 'a';
        if (obj->alphabet[letter] == NULL){
            return false;
        }
        obj = obj->alphabet[letter];
        i++;
    }
    if (obj != NULL){
        return true;
    }
    return false;
}

void trieFree(Trie* obj) {
    if (obj == NULL){
        return;
    }
    for (int i = 0; i < 26; i++){
        if (obj->alphabet[i] != NULL){
            trieFree(obj->alphabet[i]);
        }
    }
    free(obj);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/