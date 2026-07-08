-- In Lean 4, we define our domain with strict numeric types.
-- Using `Nat` (Natural numbers: 0, 1, 2, ...) guarantees amounts can NEVER be negative,
-- completely eliminating the negative-amount bug seen in the Python implementation by design.

def safe_transfer (balance1 balance2 amount : Nat) (h : amount ≤ balance1) : Nat × Nat :=
  (balance1 - amount, balance2 + amount)

-- Furthermore, we can mathematically PROVE that the total amount of money in the system
-- is exactly preserved after the transfer, guaranteeing no money leak or infinite money glitch.
theorem transfer_preserves_total_money (balance1 balance2 amount : Nat) (h : amount ≤ balance1) :
  let (new1, new2) := safe_transfer balance1 balance2 amount h
  new1 + new2 = balance1 + balance2 := by
  dsimp [safe_transfer]
  -- `omega` is a decision procedure in Lean 4 that solves
  -- quantifier-free Presburger arithmetic, successfully verifying our proof!
  omega
