class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        //vector<int> nums={10,9,2,5,3,7,12,11};
        int n=nums.size();
        int arr[2002]={};
        for(int i=0;i<n;i++)nums[i]+=1001;
        for(int i=0;i<n;i++){
            int k=arr[nums[i]-1];
            for(int j=nums[i];j<2002;j++){
                if(k+1>arr[j])arr[j]=k+1;
                else break;
            }
        }
        int ans=arr[2001];
        return ans;
    }
};
