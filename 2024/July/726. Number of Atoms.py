class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        self.idx = 0

        def parse():
            curr_map = defaultdict(int)
            atom = ""
            count = ""

            while self.idx < n:
                if formula[self.idx].isupper():
                    if atom:
                        curr_map[atom] += int(count or 1)
                    atom = formula[self.idx]
                    count = ""
                    self.idx += 1
                elif formula[self.idx].islower():
                    atom += formula[self.idx]
                    self.idx += 1
                elif formula[self.idx].isdigit():
                    count += formula[self.idx]
                    self.idx += 1
                elif formula[self.idx] == "(":
                    self.idx += 1
                    nested = parse()
                    for elem in nested:
                        curr_map[elem] += nested[elem]
                elif formula[self.idx] == ")":
                    if atom:
                        curr_map[atom] += int(count or 1)
                    self.idx += 1
                    multiplier = ""
                    while self.idx < n and formula[self.idx].isdigit():
                        multiplier += formula[self.idx]
                        self.idx += 1
                    if multiplier:
                        multiplier = int(multiplier)
                        for elem in curr_map:
                            curr_map[elem] *= multiplier
                    return curr_map

            if atom:
                curr_map[atom] += int(count or 1)
            return curr_map

        final_map = dict(sorted(parse().items()))
        return ''.join(f"{atom}{final_map[atom] if final_map[atom] > 1 else ''}" for atom in final_map)
