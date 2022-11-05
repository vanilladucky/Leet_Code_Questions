class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        def tmp():
            return [0,0,'z']
        store = defaultdict(tmp)
        for i,c in enumerate(creators):
            if views[i] > store[c][1]:
                store[c] = [store[c][0]+views[i], views[i], ids[i]]
            elif views[i] == store[c][1]:
                if ids[i] <= store[c][-1]:
                    store[c] = [store[c][0]+views[i], views[i], ids[i]]
                else:
                    store[c] = [store[c][0]+views[i], views[i], store[c][-1]]
            else:
                store[c] = [store[c][0]+views[i], store[c][1], store[c][2]]
    
        print(store)
           
        store = dict(sorted(store.items(), key=lambda item:-1*item[1][0]))
        res=[]
        highest = list(store.values())[0][0]
        for key in store:
            if store[key][0] == highest:
                temp = [key, store[key][-1]]
                res.append(temp)
            else:
                break
        return res
