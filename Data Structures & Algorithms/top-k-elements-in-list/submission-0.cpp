class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //1 - declare map & result vector
        std::vector<int> result;
        std::unordered_map<int,int> map;

        //2 - loop nums and insert in map
        for(int x : nums)
        {
            map[x]++;
        }

        //3 - loop k times,
        //    get higest key,value then insert in vector and remove from map
        for(int i=0 ; i<k ; i++)
        {
            int max = INT_MIN;
            int key_to_remove;
            for(auto [key,value] : map)
            {
                if(value>max)
                {
                    max=value;
                    key_to_remove=key;
                }
            }
            result.push_back(key_to_remove);
            map.erase(key_to_remove);
        }
        return result;
    }
};
