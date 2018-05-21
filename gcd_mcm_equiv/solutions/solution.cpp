// Reducing the problem mcm to the problem gcd:

int oracle_gcd(int a, int b);

int mcm(int a, int b) {
  return (a*b)/oracle_gcd(int a, int b);
}

// Let's prove the two problems are actually equivalent:

// Reducing the problem gcd to the problem mcm:

int oracle_mcm(int a, int b);

int gcd(int a, int b) {
  return (a*b)/oracle_mcm(int a, int b);
}


