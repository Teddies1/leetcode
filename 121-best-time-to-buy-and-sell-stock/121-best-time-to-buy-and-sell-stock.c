
int maximum(int a, int b){
    return (a > b) ? a : b;
}

int minimum(int a, int b){
    return (a > b) ? b : a;
}
int maxProfit(int* prices, int pricesSize){
    int min = prices[0];
    int max = 0;
    int profit = 0;
    
    for (int i = 1; i < pricesSize; i++){
        min = minimum(prices[i], min);
        profit = prices[i] - min;
        max = maximum(profit, max);
    }
    
    return max; 
    
    /*
    min = 7
    min = 1, profit = 0, max = 0;
    min = 1, profit = 4, max = 4;
    min = 1, profit = 2, max = 4;
    min = 1, profit = 5, max = 5;
    min = 1, profit = 3, max = 5;
    */
    
    
}