# Majir Claude Plugin

Compare products and savings with Claude. Majir helps choose a best pick and up to two alternatives from available store listings, coupons and cashback. Sign-in adds saved inbox offers. Majir never buys anything.

The plugin bundles two skills and a reference to the hosted Majir MCP server at `https://mcp.majir.shop/mcp`. It works in Claude chat, Cowork and Claude Code.

## What it does

For shopping requests, Claude can use Majir to suggest one best pick and two alternatives when enough suitable options are available. It explains the choice and shows returned prices, codes and shopping links when available. Some results have no checked product price or usable link. Claude checks fit against stated measurements and explains what is unknown. It can keep the shopping items you have discussed in view as the conversation continues.

- `majir-shopping`: loads when you want to buy, replace, reorder or gift something, ask where to get an item or whether a price is good, need a part that must fit, set a budget, or ask what deals a store has today.
- `majir-saved-offers`: loads when you ask what coupons, credits or rewards you already have, what expires soon, or want the link or code for one saved offer. Needs sign-in.

Majir checks its own catalog of coupons, promo codes and cashback, live store prices from the stores it covers, and, when you are signed in, the offers it found in your connected inbox. It does not search the whole web. Delivery times are not checked. Claude shows a product photo and stated specs only when Majir returns them.

## Install

- From Anthropic's directory, once the plugin is listed.
- For testing before that: in claude.ai, go to Customize, Plugins, Add, Upload plugin, and upload a zip of this repository. In Claude Code, run `claude --plugin-dir ./majir-claude-plugin`.

Use a tagged release rather than a moving branch, and check that `.mcp.json` points to `https://mcp.majir.shop/mcp`.

## Sign in

The connector uses OAuth on the hosted Majir server. Finding products and store deals works without an account. Your own saved offers need a Majir account with a connected inbox. Connect from the plugin's Connectors tab.

## Data

- What Claude sends to Majir: the product words and filters for a search (item, budget, store, condition, must-have words), and the id of an offer you choose. The skills tell Claude to keep names, addresses, emails, phone numbers, account or order numbers and health details out of queries.
- What Majir returns: structured offer fields (store, title, price, code, savings, deadline, link, and a photo or stated specs when available). Majir returns offer fields from your inbox, never the email text itself.
- What the plugin stores: nothing. It is Markdown and JSON. The hosted server's data handling is described in Majir's privacy policy at https://majirshop.com/privacy.

## What Majir never does

- It never buys anything or submits checkout details. Its links open the store.
- It never applies a discount by itself. A coupon code is entered at the store, and the store decides.
- It never reads your chat, memory or files. It sees only what Claude sends in a tool call.

Links may earn Majir a commission. Our picks never depend on it. This disclosure appears at connect or beside Majir links, with any additional disclosure required by the host.

## Example prompts

- I need a wire grid for the bottom of my sink. It's 29.5 by 16 inches.
- Housewarming gift, around $50, something for the kitchen.
- Does Best Buy have any deals I can use in the store today?
- Is $89 a good price for this air fryer, or is it cheaper online?
- What saved offers do I have that expire this week?
- Get me the link for my Lowe's credit.

## Documentation and support

Connector documentation: https://developers.majir.shop/mcp. Security reports: see `SECURITY.md`.

## Skill scan validation

PRs scan skills with local analyzers. Findings are advisory, but incomplete
scans fail: every skill must have one result, with no skipped skills, failed
analyzers, or unscanned content. Files above the pinned scanner's 10 MiB
per-file limit also fail validation.
