# code -> https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

def f_recurssive(ind, mlist, n):
  if ind == n-1:
    return mList[n-1]
  if ind > n-1:
    return 0
  
  pick = mList[ind] + f_recurssive(ind+2, mList, n)
  unpick = f_recurssive(ind+1, mList, n)  
  return max(pick, unpick)

def f_dp(ind, dp, mlist, n):
  if ind == n-1:
    return mList[n-1]
  if ind > n-1:
    return 0

  if(dp[ind] != 0 ):
    return dp[ind]
  
  pick = mList[ind] + f_dp(ind+2,dp, mList, n)
  unpick = f_dp(ind+1,dp,  mList, n)  
  dp[ind] = max(pick, unpick)
  return dp[ind]

def f_dp_with_tab(dp, mlist, n):
  dp[0] = mlist[0]

  for i in range(1, n):
    pick = mlist[i]
    if i > 1:
      pick += dp[i-2]
    unpick = dp[i-1]
    dp[i] = max(pick, unpick)
  
  return dp[n-1]

### __main()

mList = [5,8,7,2]
dp = [0]*len(mList)
#f_recurssive(0,mList, len(mList))
#f_dp(0, dp, mList, len(mList))
f_dp_with_tab(dp, mList, len(mList))
