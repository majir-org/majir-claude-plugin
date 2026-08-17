---
name: majir-redemption
description: Use Majir to prepare a tracked redemption link or code for a selected saved offer.
---

# Majir Redemption

Use this skill when the user wants to use, redeem, open, or prepare a saved Majir offer.

## Workflow

1. Identify the saved offer the user wants to use.
2. If the user gave only a merchant or category, search saved offers first and ask the user to pick when there are multiple matches.
3. Use the Majir redemption tool only for the selected saved offer.
4. Return the Majir-tracked redemption link or code and summarize what it is for.
5. Make clear that Majir does not purchase anything, spend money, or submit checkout details.

## Guardrails

- Do not say a purchase has been made.
- Do not claim the offer is guaranteed to work unless Majir explicitly returns that status.
- Do not modify external merchant accounts.
- Do not expose raw inbox content.
