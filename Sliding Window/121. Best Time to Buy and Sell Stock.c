#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int maxProfit(int* prices, int pricesSize){
    int res = 0;
    int buy_price = 1000000;
    for (int i = 0; i < pricesSize; i++){
        buy_price = MIN(buy_price, prices[i]);
        res = MAX(res, prices[i] - buy_price);
    }
    return res;
}
