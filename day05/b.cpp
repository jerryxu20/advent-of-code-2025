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

const int inf = 1e9;
struct Node {
	Node *l = 0, *r = 0;
    ll lo, hi, mset = inf, madd = 0, val = 0;
	Node(ll lo,ll hi):lo(lo),hi(hi){} // Large interval of -inf

	ll query(ll L, ll R) {
		if (R <= lo || hi <= L) return 0;
		if (L <= lo && hi <= R) return val;
		push();
		return l->query(L, R) + r->query(L, R);
	}
	void set(ll L, ll R, ll x) {
		if (R <= lo || hi <= L) return;
		if (L <= lo && hi <= R) {
            mset = val = x, madd = 0;
            val = hi - lo;
        }
		else {
			push(), l->set(L, R, x), r->set(L, R, x);
			val = l->val + r->val;
		}
	}
	void add(ll L, ll R, ll x) {
		if (R <= lo || hi <= L) return;
		if (L <= lo && hi <= R) {
			if (mset != inf) mset += x;
			else madd += x;
			val += x;
		}
		else {
			push(), l->add(L, R, x), r->add(L, R, x);
			val = max(l->val, r->val);
		}
	}
	void push() {
		if (!l) {
			ll mid = lo + (hi - lo)/2;
			l = new Node(lo, mid); r = new Node(mid, hi);
		}
		if (mset != inf)
			l->set(lo,hi,mset), r->set(lo,hi,mset), mset = inf;
		else if (madd)
			l->add(lo,hi,madd), r->add(lo,hi,madd), madd = 0;
	}
};

void solve() {
    ll a, b;
    Node seg(0, 1e15);
    ll mx = 0;
    while(cin >> a >> b) {
        seg.set(a, b + 1, 1);
    }  
    cout << seg.query(0, 1e15) << nl;
}

int main() {

    int t = 1;
    //cin >> t;
    while(t--) solve();
}