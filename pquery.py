class QueryHandler:
    def __init__(self, A, P):
        self.A = A[:]  # Copy of array A
        self.P = P[:]  # Copy of permutation P
        self.history = [(self.A[:], self.P[:])]  # History of states

    def update(self, l, r, v):
        for i in range(l, r + 1):
            self.A[self.P[i] - 1] += v  # Update according to permutation

    def query_sum(self, l, r):
        total = 0
        for i in range(l, r + 1):
            total += self.A[i]
        return total

    def swap_positions(self, x, y):
        self.P[x], self.P[y] = self.P[y], self.P[x]  # Swap implementation

    def revert(self, t):
        assert 0 <= t < len(self.history), "Invalid revert point"
        self.A, self.P = self.history[t]

    def save_state(self):
        self.history.append((self.A[:], self.P[:]))

# Input handling and processing
if __name__ == '__main__':
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    # Process queries
    results = []
    handler = QueryHandler(A, P)
    for _ in range(q):
        query = list(map(int, input().split()))
        query_type = query[0]

        if query_type == 1:
            l, r, v = query[1] - 1, query[2] - 1, query[3]
            handler.update(l, r, v)
        elif query_type == 2:
            l, r = query[1] - 1, query[2] - 1
            results.append(handler.query_sum(l, r))
        elif query_type == 3:
            x, y = query[1] - 1, query[2] - 1
            handler.swap_positions(x, y)
        elif query_type == 4:
            t = query[1] - 1
            handler.revert(t)

        if query_type in {1, 3, 4}:
            handler.save_state()

    # Output results for type 2 queries
    for result in results:
        print(result,end =" ")
