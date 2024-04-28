class UnionFind():
    def __init__(self):
        self.root, self.rank, self.count = {}, {}, 0

    def add(self, node):
        if node not in self.root:
            self.root[node] = node
            self.rank[node] = 1
            self.count += 1

    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node, npde):
        root = self.find(node)
        rppt = self.find(npde)

        if root != rppt:
            if self.rank[root] > self.rank[rppt]:
                self.root[rppt] = root
            elif self.rank[root] < self.rank[rppt]:
                self.root[root] = rppt
            else:
                self.root[root] = rppt
                self.rank[root] += 1
            self.count -= 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        disjoint = UnionFind()
        for index in range(len(accounts)):
            disjoint.add(index)

        emails = dict()
        for group, account in enumerate(accounts):
            name, *information = account
            for email in information:
                if email in emails:
                    disjoint.union(emails[email], group)
                else:
                    emails[email] = group

        groups = defaultdict(list)
        for email, group in emails.items():
            groups[disjoint.find(group)].append(email)

        merged = []
        for group, emails in groups.items():
            emails.sort()
            merged.append([accounts[group][0], *emails])

        return merged

