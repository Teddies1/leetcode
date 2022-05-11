

int countVowelStrings(int n)
{
    int array[n][5];
    int i, j;
    int sum = 0;
    
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if (i == 0 || j == 0)
            {
                array[i][j] = 1;
                
            }
            else
            {
                array[i][j] = array[i-1][j] + array[i][j-1];
            }
        }
    }
    for (i = 0; i < 5; i++){
        sum += array[n-1][i];
    }
    return sum;
}