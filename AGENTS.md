# Documentation project instructions

Public developer documentation for the Splendor API, built on [Mintlify](https://mintlify.com) and deployed to https://splendor-9a061a0e.mintlify.app/.

## About this project

- Pages are MDX files with YAML frontmatter. Site configuration lives in `docs.json`.
- Brand styling lives in `custom.css` (cream base, navy ink, forest accent, sharp corners).
- For Mintlify product knowledge, install the skill: `npx skills add https://mintlify.com/docs`.
- The API reference is generated from the Splendor FastAPI OpenAPI spec (committed under `api-reference/`), not hand-written. Regenerate it with `make openapi` in the product repo and copy the result here.

## Terminology

- Use **tenant** or **workspace** for an organization's account, **dataset** for a collection of records, **member** / **admin** for roles.
- Use **search**, not "query," for the product action; "query" is the request body or SQL.
- A **handle** is a `search_id`, `view_id`, or cursor. A **view** is saved or materialized; a **source** is where data is ingested from.

## Style preferences

- Active voice, second person ("you"). One idea per sentence.
- Sentence case for headings and code block titles.
- Bold for UI elements (Click **Settings**); code formatting for fields, paths, commands, and identifiers.
- Document outcomes, not functions: title guides by what the reader accomplishes ("Run your first search").
- No marketing language ("powerful", "seamless", "robust"), no filler ("it's important to note", "simply"), no emoji.
- All code blocks need a language tag; use realistic values, not `foo`/`bar`.

## Content boundaries

- Document only the **member** and **tenant-admin** API planes.
- Do **not** document Splendor-staff/platform endpoints (workspace provisioning) or internal operator tooling (object-browser, Quickwit diagnostics). These are hidden from the OpenAPI spec by design.
- The production API base URL is not finalized; pages use `https://api.splendor.io` with a TODO marker until confirmed.
