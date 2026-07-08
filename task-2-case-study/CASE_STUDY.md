# Formal Verification Case Study: Bank Transfers

## Overview
This case study explores a critical use case where formal verification demonstrates a definitive advantage over traditional automated testing: **banking transactions and total currency preservation**. When handling financial transfers, preventing money creation or loss is absolutely critical.

## The Problem: Edge Cases in Traditional Testing
In traditional dynamic languages like Python, software testing generally relies on writing specific test cases to cover expected behavior and known edge cases.

In our python implementation (`python_impl.py`), we have a seemingly sound function:
```python
def bank_transfer(balance1, balance2, amount):
    if balance1 >= amount:
        balance1 -= amount
        balance2 += amount
    return balance1, balance2
```
A standard test suite might test normal transfers (e.g., $30) and insufficient funds cases (e.g., trying to transfer $150 with a $100 balance). These tests pass perfectly.

However, if a developer forgets to check if `amount` is positive, **an attacker can transfer negative money**.
Because `100 >= -500` is `True`, reversing the operation causes `balance1` to become `600` and `balance2` to become `-450`. The code silently corrupted total balances. Because testing requires a developer to think of every single mathematical possibility, this edge case went unchecked.

## The Solution: Formal Verification in Lean 4
In Lean 4 (`LeanImpl.lean`), we take a mathematically rigorous approach to completely eliminate these categories of bugs:

1. **Type-Level Guarantees**: By defining `amount` strictly as a Natural Number (`Nat`), it mathematically cannot be negative. The bug is systematically eradicated at compile-time.
2. **Dependent Types**: The transfer function explicitly requires a mathematical proof object (`h : amount ≤ balance1`) to even compile, meaning it's impossible to call the function under invalid states.
3. **Provable Correctness**: Unlike software tests, formal verification allows us to prove, mathematically, for ALL POSSIBLE VALID inputs, that total money is preserved.
```lean
theorem transfer_preserves_total_money (balance1 balance2 amount : Nat) (h : amount ≤ balance1) :
  let (new1, new2) := safe_transfer balance1 balance2 amount h
  new1 + new2 = balance1 + balance2
```
We verified this theorem mathematically using Lean 4's `omega` decision procedure, which solves Presburger arithmetic.

## Conclusion
Traditional software testing can only prove the *presence* of bugs in specific sampled branches, whereas Formal Verification in Lean 4 explicitly guarantees the *absence* of bugs for every mathematically possible state. In critical domains like finance or cryptography, this standard of correctness is unmatched by alternative methodologies.
