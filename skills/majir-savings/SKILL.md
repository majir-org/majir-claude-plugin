---
name: majir-savings
description: Use Majir to find current deals and review saved money from a connected Majir account.
---

# Majir Savings

Use this skill when the user wants to find savings, promo codes, cashback, credits, gift cards, saved offers, or expiring deals through Majir.

## Workflow

1. Use Majir current-deal tools for public catalog searches.
2. Use Majir saved-money tools only after the user is signed in through the Majir connector.
3. Prefer structured summaries with merchant, offer value, promo code when available, expiration date when available, and recommended next action.
4. If Majir returns no results, say that directly and do not invent offers.
5. Do not claim Majir searched arbitrary websites. Majir searches its current deals catalog and user-scoped saved offer data.

## Guardrails

- Do not expose raw inbox messages.
- Do not imply that Majir guarantees a discount at checkout.
- Do not tell the user to buy something.
- Do not browse external merchant sites unless the user separately asks for web research.

## Good Prompts

- Find current Nike promo codes.
- Check my saved offers that expire soon.
- Show my best saved money opportunities.
- Search my saved money for travel deals.
