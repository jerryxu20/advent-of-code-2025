#include <bits/stdc++.h>
using namespace std;

#define int long long
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define pb push_back
typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef tuple<int, int, int> ti;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

#ifdef LOCAL
#include <debug.h>
#else
#define debug(...)
#define debugArr(...)
#endif

const int MOD = 1000000007;
const char nl = '\n';



const int N = 6;
vector<vector<string>> shape = {{"##.", "##.", "###"}, {"###", "##.", ".##"}, {"#.#", "#.#", "###"}, {"##.", ".##", "..#"}, {"..#", ".##", "###"}, {"#.#", "###", "#.#"}};
vector<int> cnt;

vector<vector<array<int, 3>>> M;


int backtrack(int idx, vi &things, vi &grid, int a, int b) {
    if (idx == sz(things)) return true;


    for (int i = 0; i + 3 <= a; i++) {
        for (int j = 0; j + 3 <= b; j++) {


            for (auto &m: M[things[idx]]) {
                bool v = 1;
                rep(k, 0, 3) {
                    if (grid[i] & (m[k] << j)) v = 0;
                }
                if (!v) continue;

                rep(k, 0, 3) {
                    grid[i] ^= (m[k] << j);
                }
                if (backtrack(idx + 1, things, grid, a, b)) return 1;
                rep(k, 0, 3) {
                    grid[i] ^= (m[k] << j);
                }
            }
        }
    }

    return 0;
}

array<int, 3> mask_of(vector<string> &s) {
    array<int, 3> ans;
    ans[0] = 0;
    ans[1] = 0;
    ans[2] = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) if (s[i][j] == '#') ans[i] |= (1 << j);
    }
    return ans;
}

void flip(vector<string> &s) {
    for (auto &v: s) reverse(all(s));
}

void rotate(vector<string> &s) {
    vector<string> res(3, string(3, '.'));
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            res[3 - j - 1][i] = s[i][j];
        }
    }
    swap(s, res);
}

void solve() {
    for (auto &v: shape) {
        int c = 0;
        rep(i, 0, 3) c += count(all(v[i]), '#');
        cnt.pb(c);


        vector<array<int, 3>> masks;
        int k = 3;
        while(k--) {
            masks.pb(mask_of(v));
            flip(v);
            masks.pb(mask_of(v));

            rotate(v);
        }
        M.pb(masks);
    }
    
    

    string dim;
    
    vector<pi> dims;
    vector<array<int, 6>> req;
    while(cin >> dim) {
        array<int, 6> a;
        rep(i, 0, 6) cin >> a[i];
        req.pb(a);


        dims.pb(pi(stoi(dim.substr(0, 2)), stoi(dim.substr(3, 5))));
    }

    int ans = 0;
    rep(i, 0, sz(req)) {
        int s = dims[i].first * dims[i].second;

        for (int j = 0; j < 6; j++) {
            s -= cnt[j] * req[i][j];
        }
        if (s < 0) continue;

        vector<int> things;
        for (int j = 0; j < 6; j++) {
            rep(_, 0, req[i][j]) things.pb(j);
        }

        vector<int> grid(dims[i].first);
        if (backtrack(0, things, grid, dims[i].first, dims[i].second)) {
            ans++;
        }
    }
    cout << ans << nl;
}

signed main() {
    // cin.tie(0)->sync_with_stdio(0);
    // cin.exceptions(cin.failbit);
    int t = 1;
    //cin >> t;
    while(t--) solve();
}