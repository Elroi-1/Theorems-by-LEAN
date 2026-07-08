# Lean 4 Formal Verification Project

This repository contains two tasks demonstrating mathematics, formal verification, and the power of theorem proving using Lean 4.

## Task 1: Propositional Logic Proofs
Located in the `task-1-logic-proofs/` folder. This contains standard propositional logic theorems (such as transitivity, modus tollens, contrapositive) thoroughly proved using valid explicit logic techniques in `Logic.lean`. `sorry` placeholders have been completely eliminated.

## Task 2: Formal Verification Case Study
Located in the `task-2-case-study/` folder.
A comparison study illustrating the differences in correctness guarantees between standard dynamic tests (in Python) vs mathematically rigorous proofs (in Lean 4) using a system addressing currency transfers.

- `python_impl.py`: Contains a standard Python function and unittest suite demonstrating a logical edge case vulnerability (negative input values causing incorrect mutated balances).
- `LeanImpl.lean`: Contains a fully verified Lean 4 implementation utilizing dependent types to explicitly bar invalid program states and verify a theorem proving total consistency.
- `CASE_STUDY.md`: A detailed report documenting the comparisons and the strengths of formal verification in crucial real-world environments.
