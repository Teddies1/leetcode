

bool canConstruct(char * ransomNote, char * magazine){
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