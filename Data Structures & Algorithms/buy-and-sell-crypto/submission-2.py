class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0 
        start = 0
        buy = 0
        #[7,1,5,3,6,4]
        for sell in range(len(prices)):

            #find the lowest buy then keep moving end window to see if it improves max
            while prices[buy] > prices[sell]:
                buy += 1

            curr_max = max(curr_max, prices[sell] - prices[buy])



        
        return curr_max
            