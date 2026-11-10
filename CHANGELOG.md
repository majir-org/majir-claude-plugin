# Changelog

## 1.1.4

- Shortens both skill descriptions (shopping from 817 to 552 characters, saved offers from 445 to 380). In eval runs the same skills loaded for the same requests before and after.
- Shopping skill: an alternative is always a product, never a code on its own, and no price is worked out after a code unless the returned terms establish that the code applies to that product. Before this change, eval runs showed an estimated "price after code" in 5 of 19 answers. After it, 0 of 9.
- No connector changes.

## 1.1.3

- Removes the CI helper script `.github/scripts/test_skill_scan.py`. The Claude plugin directory accepts script files only from Verified organizations, and it refused version 1.1.2 for this file. The agent skill scan still runs on pull requests; only its self-test is gone.
- Adds the three links the directory reads for the plugin's listing: terms of service (`termsOfServiceUrl`), documentation (`documentationUrl`) and support (`supportUrl`). The listing showed no value for them.
- No skill or connector changes.

## 1.1.2

- Updates the shopping skill to use the renamed `recommend_purchase` tool when available, preserving the `search_offers` fallback when it is unavailable or used or refurbished listings are needed.
- Removes account-plan wording from the saved-offers skill to match the fields returned by `get_my_account`.

## 1.1.1

- Adds the plugin icon (the Majir wallet mark, 512x512 PNG in `assets/icon.png`) and the privacy policy address (`privacyPolicyUrl`, https://majirshop.com/privacy), the two warnings the directory scan raised.
- No skill or connector changes.

## 1.1.0

- Adds the `majir-shopping` skill. It loads on buying intent (buy, replace, reorder, gift, "where can I get", "is this a good deal", deals at a store) and answers with one best pick plus two alternatives from Majir's results.
- Adds the `majir-saved-offers` skill for the signed-in person's own inbox offers: what they have, what expires soon, and the link or code for one chosen offer.
- Retires the `majir-savings` and `majir-redemption` skills. Their scope is covered by the two skills above.
- Plugin description and keywords now describe shopping, not only savings.
- README rewritten for the directory: what the plugin does, what it sends, and what it never does.
- The connector address in `.mcp.json` is unchanged.

## 1.0.1

- Adds a signed release tag for the Majir Claude plugin package.
- No plugin behavior changes.

## 1.0.0

- Initial Claude plugin package for the Majir hosted MCP server.
- Adds Majir savings and redemption skills.
