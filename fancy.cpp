#include <bits/stdc++.h>
using namespace std;

class Fancy {
#define ll long long
#define len(a) (int)(a).size()
public:
	vector<vector<ll>> bl;
	vector<vector<ll>> ev;
	int added = 0;
	int K = 320;
	int MD = int(1e9+7);

    Fancy() {
    }
    
    void append(int val) {
    	int blN = len(bl), evN = len(ev);
        if (len(bl) == 0 or len(bl[blN-1]) == K) {
        	bl.push_back({val});
        	ev.push_back({1, 0});
        } else {
        	for (int i = 0; i < len(bl[blN-1]); i++) {
        		bl[blN-1][i] *= ev[evN-1][0];
        		bl[blN-1][i] += ev[evN-1][1];
        		bl[blN-1][i] %= MD;
        	}
        	ev[evN-1] = {1, 0};
        	bl[blN-1].push_back(val);
        }
        added += 1;
    }
    
    void addAll(int inc) {
        if (added == 0)
        	return;
        for (int i = 0; i < len(bl); i++) {
        	ev[i][1] += inc;
        	ev[i][1] %= MD;
        }
    }
    
    void multAll(int m) {
        if (added == 0) 
        	return;
        for (int i = 0; i < len(bl); i++) {
        	ev[i][0] = (ev[i][0] * m) % MD;
        	ev[i][1] = (ev[i][1] * m) % MD;
        }
    }
    
    int getIndex(int idx) {
    	if (added <= idx) return -1;
    	int id = idx / K;
    	for (int i = 0; i < len(bl[id]); i++) {
    		bl[id][i] *= ev[id][0];
    		bl[id][i] += ev[id][1];
    		bl[id][i] %= MD;
    	}   
    	ev[id] = {1, 0};
    	return bl[id][idx % K];
    }
};

int main() {
	vector<string> cmd = 
}