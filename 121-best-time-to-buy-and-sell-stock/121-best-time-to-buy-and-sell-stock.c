
int maximum(int a, int b){
    return (a > b) ? a : b;
}

int minimum(int a, int b){
    return (a > b) ? b : a;
}
int maxProfit(int* prices, int pricesSize){
    int min = prices[0];
    int max = 0, profit = 0;
    
    for (int i = 1; i < pricesSize; i++){
        min = minimum(prices[i], min);
        profit = prices[i] - min;
        max = maximum(profit, max);
    }
    
    
    
    return max; 
     
}