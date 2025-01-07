/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var num = prices[0];
    var diff = 0;
    for(let i=1; i < prices.length; i++){
        if(prices[i] <= num){
            num = prices[i];
        }else {
            diff = Math.max(diff, prices[i] - num); 
        }
    }
    return diff;
};