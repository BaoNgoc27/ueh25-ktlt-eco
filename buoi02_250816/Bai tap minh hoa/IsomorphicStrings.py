import sys

lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip()]

def extract(x: str) -> str:
    return x.split("=", 1)[1].strip() if "=" in x else x

if len(lines) < 2:
    print("False")
    raise SystemExit(0)

s, t = extract(lines[0]), extract(lines[1])

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    m1, m2 = {}, {}
    for a, b in zip(s, t):
        if a in m1 and m1[a] != b: return False
        if b in m2 and m2[b] != a: return False
        m1[a] = b
        m2[b] = a
    return True

print("True" if is_isomorphic(s, t) else "False")
