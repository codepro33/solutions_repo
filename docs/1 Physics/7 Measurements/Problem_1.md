 
# Course Content with Explanations, Examples, and Test Questions

---

## 1. The Language of Mathematical Logic

### Concept Explanation:
Mathematical logic deals with statements that are either true or false and methods for reasoning formally.

### Key Topics:
- **Inference Schemes**: Rules used to derive conclusions.
- **Zero-One Method**: Interpreting logical statements using 0 (false) and 1 (true).
- **Shortened Zero-One Method**: A more efficient variant for evaluating logical expressions.
- **Proof by Contradiction ("Not Directly")**: Assume the opposite of what you're trying to prove and show a contradiction.
- **Direct Proof**: Starting from known truths and applying logical steps to reach the conclusion.

### Example:
**Statement:** If $P \Rightarrow Q$ and $Q \Rightarrow R$, then $P \Rightarrow R$.

**Direct Proof:**
1. Assume $P$ is true.
2. From $P \Rightarrow Q$, it follows that $Q$ is true.
3. From $Q \Rightarrow R$, it follows that $R$ is true.
4. Therefore, $P \Rightarrow R$ is valid.

### Test-style Question:
**Q1:** Which of the following is a valid inference?  
A) If $A \Rightarrow B$, and $B$ is false, then $A$ is false.  
B) If $A \Rightarrow B$, and $A$ is true, then $B$ must be true.  
C) If $A \Rightarrow B$, and $B$ is true, then $A$ is true.  
D) If $A \Rightarrow B$, and $A$ is false, then $B$ must be false.

**Answer:** B  
**Explanation:** Only in B do we apply the implication correctly. If the premise is true and the implication holds, then the conclusion must be true.

---

## 2. Quantifiers and Predicates

### Concept Explanation:
Predicates express properties or relations among objects. Quantifiers help express generality:
- **Universal Quantifier ($\forall$)**: "For all..."
- **Existential Quantifier ($\exists$)**: "There exists..."

### Free and Bound Variables:
- A **bound variable** is quantified (e.g., $\forall x, P(x)$).
- A **free variable** is not bound and can take any value.

### Example:
**Statement:** "All humans are mortal. Socrates is a human. Therefore, Socrates is mortal."

**Formalization:**
Let $H(x)$: "x is a human", $M(x)$: "x is mortal"  
Then:  
- $\forall x (H(x) \Rightarrow M(x))$  
- $H(\text{Socrates}) \Rightarrow M(\text{Socrates})$

### Test-style Question:
**Q2:** Identify which expression has a bound variable:  
A) $P(x)$  
B) $\forall x\, P(x)$  
C) $Q(y) \land R(z)$  
D) $x + y > 0$

**Answer:** B  
**Explanation:** Only B has a quantifier that binds variable $x$.

---

## 3. Relations and Cartesian Product

### Concept Explanation:
- **Ordered Pair**: $(a, b)$ where order matters
- **Cartesian Product**: $A \times B = \{(a, b) | a \in A, b \in B\}$
- **Binary Relations**: Subsets of Cartesian products

### Types of Relations:
- **Reflexive**: $\forall x, (x, x) \in R$
- **Symmetric**: $(x, y) \in R \Rightarrow (y, x) \in R$
- **Transitive**: $(x, y), (y, z) \in R \Rightarrow (x, z) \in R$
- **Antisymmetric**: $(x, y), (y, x) \in R \Rightarrow x = y$
- **Equivalence Relation**: Reflexive, symmetric, transitive

### Example:
Set $A = \{1, 2\}$, relation $R = \{(1, 1), (2, 2), (1, 2), (2, 1)\}$  
- Reflexive? ✅  
- Symmetric? ✅  
- Transitive? ✅  
→ So, it's an equivalence relation.

### Test-style Question:
**Q3:** Is the relation $R = \{(1,1), (2,2), (1,2)\}$ on set $\{1, 2\}$ symmetric?

**Answer:** No  
**Explanation:** $(1,2) \in R$ but $(2,1) \notin R$, so it's not symmetric.

---

## 4. Elements of Combinatorics

### Concept Explanation:
Combinatorics is about counting elements in sets.

### Key Concepts:
- **Injection**: One-to-one function
- **Surjection**: Onto function
- **Bijection**: Both injective and surjective

### Counting Principles:
- **Addition**: If task A has m ways, task B has n ways (non-overlapping), total = $m + n$
- **Multiplication**: Task A then B → total = $m \times n$
- **Inclusion-Exclusion**: $|A \cup B| = |A| + |B| - |A \cap B|$
- **Pigeonhole Principle**: If $n$ items in $m$ containers and $n > m$, at least one container has more than one item

### Example:
You have 3 shirts and 2 pants. How many outfits?  
- Answer: $3 \times 2 = 6$

### Test-style Question:
**Q4:** In how many ways can you distribute 10 identical balls into 3 distinct boxes?

**Answer:**  
$\binom{10 + 3 - 1}{2} = \binom{12}{2} = 66$

---

## 5. Binomial Coefficients, Permutations and Combinations

### Concept Explanation:
- **Permutation:** Arrangement of objects (order matters)
- **Combination:** Selection of objects (order doesn't matter)
- **Binomial Coefficients:**  
  $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

### Advanced Topics:
- **Cycle decomposition**: Writing a permutation as product of disjoint cycles
- **Transposition**: Swapping two elements
- **Pascal’s Triangle**: Used to compute $\binom{n}{k}$

### Example:
How many 3-letter words from {A, B, C, D} without repetition?  
- $4 \times 3 \times 2 = 24$ permutations

### Test-style Question:
**Q5:** How many ways can you choose 3 students from 5?  
- $\binom{5}{3} = 10$

---

## 6. Number Theory Basics

### Concept Explanation:
Number theory studies properties of integers.

### Key Topics:
- **Divisibility**: $a$ divides $b$ if $\exists k$ such that $b = ak$
- **GCD and Euclidean Algorithm**: GCD$(a, b)$ via repeated division
- **LCM**: $\text{lcm}(a, b) = \frac{ab}{\text{gcd}(a, b)}$
- **Prime Numbers**: Only divisible by 1 and itself

### Example:
Find GCD of 48 and 18:  
- $48 = 18 \times 2 + 12$  
- $18 = 12 \times 1 + 6$  
- $12 = 6 \times 2 + 0$ → GCD = 6

### Test-style Question:
**Q6:** What is the LCM of 6 and 8?  
- $\text{gcd}(6,8) = 2$, so  
- $\text{lcm} = \frac{6 \times 8}{2} = 24$

---

**End of document.**
