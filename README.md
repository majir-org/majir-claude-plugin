# Majir Claude Plugin

Majir helps Claude Code and Cowork find money users already have. The plugin connects to the hosted Majir MCP server at `https://mcp.majir.shop/mcp`.

## What It Provides

- Current deals, promo codes, and cashback from Majir's current deals catalog.
- Saved offers, credits, gift cards, and expiring deals from a signed-in user's Majir wallet.
- Majir-tracked redemption links or codes for selected saved offers.

## Installation

Install this plugin from the Claude plugin marketplace after approval. For pre-approval testing, use the latest GitHub-verified signed release tag rather than a moving branch, and verify that `.mcp.json` points to `https://mcp.majir.shop/mcp`.

## Authentication

Majir uses OAuth through the hosted MCP server. Personal saved-money tools require the user to sign in with a Majir-linked account. Majir returns structured offer fields only, not raw inbox messages.

## Example Prompts

- Find current Nike promo codes.
- Check my saved offers that expire soon.
- Show my best saved money opportunities.
- Prepare the redemption link for one saved offer.

## Documentation

See `https://developers.majir.shop/mcp`.
