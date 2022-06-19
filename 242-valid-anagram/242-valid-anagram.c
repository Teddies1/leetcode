

bool isAnagram(char * s, char * t){
    int array1[26] = {0};
    int array2[26] = {0};
    int letter1, letter2, i = 0, j = 0, m = 0, n = 0;
    while (s[i] != '\0' && t[j] != '\0'){
        letter1 = s[i] - 'a';
        array1[letter1]++;
        i++;
    }
    while (t[j] != '\0'){
        letter2 = t[j] - 'a';
        array2[letter2]++;
        j++;
    }
    while (m < 26 && n < 26){
        if (array1[m] != array2[n]){
            return false;
        }
        m++;
        n++;
    }
    return true;
}