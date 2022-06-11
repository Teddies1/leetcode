

bool canConstruct(char * ransomNote, char * magazine){
    /* 
    idea is to maintain an 26 member array, initialised to 0,
    storing the counter of alphabetical characters in the magazine string.
    then we traverse the magazine string, incrementing the array entry
    corresponding to the letter (a -> array[0], etc.)
    
    then we traverse the ransomNote string. for each letter,
    first check if the array entry is empty. if yes, the note 
    cannot be complete, and return false.
    if it's not empty, then decrement it by 1. 
    */
    
    int mag[26] = {0};
    int letter, ransom;
    int i = 0, j = 0;
    while (magazine[i] != '\0'){
        letter = magazine[i] - 97;
        mag[letter]++;
        i++;
    }
    while (ransomNote[j] != '\0'){
        ransom = ransomNote[j] - 97;
        if (mag[ransom] == 0){
            return false;
        }
        if (mag[ransom] > 0){
            mag[ransom]--;
        }   
        j++;
    }
    return true;
}