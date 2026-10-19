# Homeschool Hub team operations

## Scope and budget
Maintain the existing free ages 3–8 resource site. No additional charges: no paid APIs, paid runners, upgrades, domains, trials or billing changes. Stop if an operation's cost cannot be confirmed free/included. Keep GitHub Pages hosting and existing content.

## Coordinated roles
- Research: inspect existing packs and requests, select a useful gap and write a brief.
- Marketing: improve page titles, navigation and clear copy; draft promotion ideas. External messages or posts are not authorized.
- Quality: check educational accuracy, age guidance, answers, links and rendered printable layouts.
- Publishing lead: combine findings, implement one coherent update, check fresh branch state, publish without force pushes and verify deployment.

Agents share findings with the lead; only the lead publishes. If specialist agents are unavailable, do these roles sequentially. This file is a shared handoff, not a scheduler. The recurring task is managed in ChatGPT. Old Grok scheduling has not been disabled or verified.

## 2026-10-17 first cycle
- Research, marketing and quality agents independently inspected the existing site.
- Inventory: 21 packs. All 21 PDFs opened locally and relative HTML links/anchors resolved. This does not certify educational correctness of every existing worksheet.
- Homepage changes: count corrected from 14 to 21; stale refresh banner removed; title and introductory copy simplified.
- Public request form: removed email collection and serialization, replaced Student with Educator, added public-visibility and personal-information warning. Newsletter mailto preserved.
- Clipboard fallback corrected to report failed copy honestly.
- QA: both executable inline JavaScript blocks passed syntax checks; removed email references absent from request script; 21 count matches 21 PDFs.
- Deployment status must be checked against the commit containing this entry before claiming live publication.

## Backlog
1. Tell the Time: O’clock prepared in the 2026-10-19 cycle below; verify deployment before treating it as live.
2. Add subject navigation/filtering for the 21 packs, with accessible no-results feedback.
3. Clearly mark older-age stage cards without resources as planned; avoid implying existing coverage.
4. Clarify newsletter is an email signup request, not an automated subscription service.

## 2026-10-18 maintenance cycle
- Fresh main inspected at 209f5c8; no open PRs and no repository AGENTS.md found. Local index.html and packs/pack.css contain unfinished redesign work; neither is included in this update.
- Research selected an existing-resource usability gap instead of increasing pack count: Subitising to 5 lacked a practical parent teaching routine.
- Added a short show/cover/check activity, counting support, optional adult scribing, answer-page directions, and a descriptive link to Number Bonds to 5. Existing PDF, branding, free resources and URLs preserved.
- Quality: rendered existing activity pages 3–7 and matched all 15 dot counts to the answer table on page 8; relative targets exist; existing homepage and sitemap already include the page. No new PDF was created.
- Publishing lead alone owns the commit. Verify deployment and live page after committing; this log is not a claim of live deployment.
- Zero-cost scope: only existing connected capabilities and existing Pages deployment; no workflow, runner, tracking, account, payment, hosting or billing changes.
- Weekly recap (12–18 October, before this update): repository history contains one commit on 17 October, correcting homepage pack count/copy and public request privacy and adding this operations document. Existing inventory remains 21 packs. No new pack was published in that interval.
- Grok scheduling remains unverified.

## Business validation backlog
- Audience visits, downloads and sales remain unknown. No tracking installed. Search Console ownership/access remains unverified; inspect existing measurement only when available.
- Product hypothesis: “10-minute Number Confidence”, four weeks of parent-led number play, approximately ages 4–6. Use existing free subitising, number bonds, picture arithmetic and numbers 1–10 packs as sample anchors; preserve their free availability.
- Differentiator to test: readiness check, 20 original sequenced sessions, household-object games, exact adult prompts, worked answers, and easier/stretch routes. Do not merely repackage free pages for sale.
- €9 is an untested price assumption, not evidence of demand. Proposed usability gate: five consenting adult testers, at least four able to use a sample without clarification within 10–15 minutes, and at least three requesting a fuller progression. These are internal decision thresholds, not proof of purchase intent.
- Next: prepare one sample session and adult feedback questions; outreach requires separate authorization. Suitable storefront terms/fees and hosting rules must be freshly checked before any sales implementation; do not open accounts or publish a paid offer.

## 2026-10-19 maintenance and content cycle
- Inspected fresh main at 17c7def, recent commits, recursive source inventory, open PRs (none), branch metadata (unprotected; no required checks) and rulesets (none). No AGENTS.md or custom workflow exists. Preserved the recent redesign and Grok's Euro Coins pack; no overlapping files were replaced with stale copies.
- Lead implements/publishes; research, marketing and quality agents provide read-only reviews. Existing 22 PDF paths remain unchanged.
- Prepared original Telling Time to the Hour pack, ages about 5–7: four A4 pages, parent model, six read and six draw exercises, full answers. Generator retained in tools/generate_oclock.py; ReportLab and DejaVu Sans are required to regenerate it.
- Quality specialist visually inspected all four final PNG renders: no clipping; accurate odd-hour reading examples, even-hour drawing answers and overlapping hands at 12. Lead independently reviewed the parent guide. Embedded fonts and black-and-white layouts improve print reliability.
- Added matching page with descriptive title/metadata, worksheet preview, homepage download/card, ages 5–7 navigation and sitemap entry. Relative paths and XML are checked before publishing. Browser layout verification is not yet established.
- Zero-cost check: public repository, existing dynamic Pages deployment, no workflow/runner/cache additions. Standard public/Pages runner use is free per https://docs.github.com/en/billing/concepts/product-billing/github-actions (checked 19 October). No paid services, billing controls, hosting, tracking or permissions changed.
- Publication must be checked against this cycle's commit; this pre-publication log does not claim a successful live deployment. Public URL retrieval currently fails from both web retrieval and local networking; retry an available supported surface after deployment and report any remaining limit.
- Measurement: inspected current homepage source; no analytics script or Search Console verification marker found. That does not establish absence of account-level or DNS verification. No connected report was available. Website visits, PDF interest and sales remain unknown; repository traffic must not be used as a substitute.

## Reviewable business draft (not a published offer)
- Keep the existing narrow hypothesis: “10-minute Number Confidence”, ages about 4–6, for parents unsure how to progress beyond counting. Four weeks, 20 original sessions, readiness check, exact adult prompts, common-error support, worked answers and easier/stretch routes. Existing free packs stay free; the proposed paid value is guided progression. €9 remains an untested price hypothesis.
- Concrete sample session: “Hide five”. Materials: five large safe objects and an opaque cup, supervised by an adult. (1 min) Count all five together. (2 min) Show two, cover three; ask “There are five altogether. Two are here. How many are hiding?” (3 min) Uncover, count and explain “Two and three make five”; repeat with 1+4 and 4+1. (2 min) Let the child choose the hidden group. (2 min) Ask them to show a different way to make five. Easier: use three objects and uncover freely. Stretch: predict all ways with five, including 0+5 and 5+0. Answers: hidden counts 3, 4, 1 respectively. Record adult observations only; do not collect child identifiers.
- Adult feedback draft: Were materials/preparation clear? Could you start without asking for help? Which prompt confused you? Was ten minutes realistic? Would a sequenced follow-on be useful, and why? What would you pay, if anything? No outreach or data collection performed. Five-adult usability gate in the backlog is a proposed decision rule, not market evidence.
- Evidence versus assumptions: official Year 1 curriculum supports number bonds within 10 and o’clock learning, but does not establish buyer demand: https://www.gov.uk/government/publications/national-curriculum-in-england-mathematics-programmes-of-study/national-curriculum-in-england-mathematics-programmes-of-study . Buyer need, conversion and price all need validation.
- Hosting suitability: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits prohibits Pages use primarily for online business/e-commerce or facilitating commercial transactions. Preserve the free educational site; do not install checkout or publish a paid offer here. An independently hosted storefront is only a proposal requiring authorization and renewed suitability checks, not a hosting migration.
- Candidate route: Payhip Free Forever advertises $0/month plus 5% per transaction; Stripe/PayPal processing charges are additional (https://payhip.com/pricing, checked 19 October). Zero upfront price does not mean fee-free sales. No merchant account, terms, payment integration, affiliate link or sales obligation created.
- Next decision: validate an original sample with consenting adults only after outreach authorization; inspect any existing Search Console report if access becomes available. Keep selling drafts unpublished until hosting suitability, transaction fees and explicit authorization are resolved. Grok's schedule remains unverified and unchanged.
