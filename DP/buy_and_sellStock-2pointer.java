class Main {
    public static int maxProfit(int[] prices) {
        int buy = 0, sell = 1;
        int maxP = 0;
        int n = prices.length;
        int buyAbs = 0, sellAbs = 0;

        while (sell < n){
            if (prices[buy] > prices[sell] ){
                int profit = prices[sell] - prices[buy];
                if ( maxP > profit){
                    maxP = profit;
                    buyAbs = buy;
                    sellAbs = sell;
                }
            } else {
                buy = sell;
            }
            sell += 1;
        }
        System.out.println(buyAbs + " " + sellAbs);
        return maxP;


    }
    
    public static void main (String[] args) {
        /* code */
        System.out.println(
        maxProfit(new int[]{7,5,3,4,6, 1}));
    }
}
