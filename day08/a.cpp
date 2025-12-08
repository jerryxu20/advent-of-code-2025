#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define pb push_back
typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef tuple<ll, ll, ll> ti;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

#ifdef LOCAL
#include <debug.h>
#else
#define debug(...)
#define debugArr(...)
#endif

const int MOD = 1000000007;
const char nl = '\n';

struct UF {
    vi id, rank;
    UF(int n): id(n), rank(n, 1) {
        iota(all(id), 0);
    }
    int find(int a) {
        if (a == id[a]) return a;
        id[a] = find(id[a]);
        return id[a];
    }
    bool join(int a, int b) {
        a = find(a);
        b = find(b);
        if(a == b) return 0;
        id[b] = a;
        rank[a] += rank[b];
        return 1;
    }
};

void solve() {
    char c;
    int x, y, z; 
    vector<ti> pts;
    while(cin >> x >> c >> y >> c >> z) {
        pts.pb({x, y, z});
    }

    vector<ti> edge;
    rep(i, 0, sz(pts)) {
        rep(j, 0, sz(pts)) if (i < j) {
            auto [x, y, z] = pts[i];
            auto [xx, yy, zz] = pts[j];
            ll d = (x - xx) * (x -xx) + (y - yy) * (y - yy) + (z - zz) * (z - zz);
            edge.pb({d, i, j});
        }
    }

    sort(all(edge));

    int cnt = 1000;
    UF uf(sz(pts));
    
    for (auto &[c, i, j]: edge) {
        cnt--;
        uf.join(i, j);
        if (cnt == 0) break;
    }

    vi arr;
    rep(i, 0, sz(pts)) if (uf.find(i) == i) {
        arr.pb(uf.rank[i]);
    } 
    sort(all(arr), greater<int>());

    ll ans = (ll)arr[0] * arr[1] * arr[2];
    cout << ans << nl;
}

int main() {
    int t = 1;
    while(t--) solve();
}