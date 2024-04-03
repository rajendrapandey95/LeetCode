#include <iostream>
#include <fstream>

#define MOD 1000000009

long long mulmod(long long a, long long b, long long c) {
    long long x = 0, y = a % c;
    while (b > 0) {
        if (b % 2 == 1) {
            x = (x + y) % c;
        }
        y = (y * 2) % c;
        b /= 2;
    }
    return x % c;
}

long long modulo(long long a, long long b, long long c) {
    long long x = 1, y = a;
    while (b > 0) {
        if (b % 2 == 1) {
            x = mulmod(x, y, c);
        }
        y = mulmod(y, y, c);
        b /= 2;
    }
    return x % c;
}

long long mod_inverse(long long n) {
    return modulo(n, MOD - 2, MOD);
}

long long abs(long long a) {
    if (a < 0) a = -a;
    return a;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int t;
    std::cin >> t;
    while (t--) {
        long long n;
        std::cin >> n;
        long long ans = ((modulo(10, n, MOD) - modulo(8, n, MOD)) * mod_inverse(2)) % MOD;
        std::cout << abs(ans) << std::endl;
    }

    return 0;
}
