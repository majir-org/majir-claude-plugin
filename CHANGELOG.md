# Changelog

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
