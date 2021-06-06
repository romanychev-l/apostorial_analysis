#include <iostream>
#include <algorithm>
#include <cstddef>
#include <iterator>
#include <memory>
#include <time.h>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <ctime>

//#include <bits/stdc++.h>

using namespace std;


typedef pair<int,int> rib;
typedef vector<vector<rib> > graph;

const int inf = 1000*1000*1000;

void print_g(graph& g){
    for(int i = 0; i<g.size(); i++){
        cout << i << ":\n";
        for(int j = 0; j<g[i].size(); j++){
            cout << g[i][j].first << ':' << g[i][j].second << ' ';
        }
        cout << "\n";
    }
}

// обход в ширину

int main(){
    freopen(".txt", "w", stdout);
    srand(time(0));


    int c = 0;
    while(c < 1000) {
        vector<vector<int> > g;

        g.push_back({});
        int m = 200;
        for(int i = 0; i<m; i++){
            int ind = rand() % g.size();
            g[ind].push_back(i+1);
            g.push_back({ind});
            //cout << ind << ' ' << i + 1 << '\n';
        }

        int n = g.size();
        int s = 0;
        int v1 = 0, W = 100;
        int max_size = 1;

        queue<int> q;
        q.push (s);
        vector<bool> used (n);
        vector<int> d (n), p (n);
        used[s] = true;
        p[s] = -1;
        while (!q.empty()) {
            if(q.size() > max_size){
                max_size = q.size();
            }

            int v = q.front();
            q.pop();
            for (size_t i=0; i<g[v].size(); ++i) {
                int to = g[v][i];
                if (!used[to]) {
                    used[to] = true;
                    q.push (to);
                    d[to] = d[v] + 1;
                    p[to] = v;
                }
            }
        }

        cout << max_size << "\n";

        c++;
    }

    return 0;
}


//алгоритм Левита
/*
int main(){
    freopen("time_1000.txt", "w", stdout);
    srand(time(0));

    int c = 0;
    while(c < 10000){
        //cout << c << "\n";
        c++;

        int n = 1000, v1 = 0, W = 1000;
        //int m = rand() % (n * (n-1) / 2 - n) + n + 1;

        //int m = n * (5 + rand() % 5);
        int m = n * 10;
        graph g(n);

        //vector<vector<pair<int,int> > > g = {{{1, 8}, {3, 8}},
        //              {{2, 7}},
        //              {{3, 4}, {0, 7}, {4, 1}},
        //              {{4, 10}, {1, 3}},
        //              {{1, 6}, {0, 5}}};

        vector<set<int> > vs(n);

        //cout << rand() << "\n";

        for(int i = 0; i<n-1; i++){
            int w = rand() % W + 1;
            g[i].push_back({i+1, w});
            //g[i+1].push_back({i, w});

            vs[i].insert(i+1);
            //vs[i+1].insert(i);
        };

        for(int i = n; i<=m; i++){
            int v_1 = rand() % n;
            int v_2 = rand() % n;
            while(v_1 == v_2 || vs[v_1].find(v_2) != vs[v_1].end()){
                v_1 = rand() % n;
                v_2 = rand() % n;
            }
            int w = rand() % W + 1;
            g[v_1].push_back({v_2, w});
            //g[v_2].push_back({v_1, w});
            vs[v_1].insert(v_2);
            //vs[v_2].insert(v_1);
        }

        //print_g(g);

        vector<int> d(n, inf);
        d[v1] = 0;
        vector<int> id(n);
        id[v1] = 1;
        deque<int> q;
        q.push_back(v1);
        vector<int> p(n, -1);

        int ma = 0;
        int mi = inf;
        auto start = clock();
        while (!q.empty())
        {
            //cout << "OK";
            if(q.size() > ma){
                ma = q.size();
            }

            int v = q.front();
            q.pop_front();
            id[v] = 2;
            for (size_t i=0; i<g[v].size(); ++i)
            {
                int to = g[v][i].first, len = g[v][i].second;
                if (d[to] > d[v] + len)
                {
                    d[to] = d[v] + len;
                    if(id[to] == 0)
                        q.push_back(to);
                    else if(id[to] == 2)
                        q.push_front(to);
                    p[to] = v;
                    id[to] = 1;
                }
            }
        }
        auto end = clock();
        //cout << start << "\n";

        cout << end - start << "\n";

    }
    return 0;
}
*/