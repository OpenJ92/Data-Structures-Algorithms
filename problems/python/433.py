class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        gene_bank = set(bank)
        bases     = set(['A', 'C', 'G', 'T'])

        if not bank:
            return -1

        def mutate(gene, index):
            nbases = bases - set(gene[index])
            mutations = []
            for base in nbases:
                mutated_gene = gene[:index] + base + gene[index + 1:]
                if mutated_gene in gene_bank:
                    mutations.append(mutated_gene)
            return mutations

        def get_mutations(gene):
            indices = len(gene)
            mutations = []
            for index in range(indices):
                mutations = chain(mutations, mutate(gene, index))
            return mutations
        
        queue = deque([(startGene, 0)])
        seen = set()
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for mutated_gene in get_mutations(gene):
                if mutated_gene not in seen:
                    queue.append((mutated_gene, steps+1))
                    seen.add(mutated_gene)
        return -1
