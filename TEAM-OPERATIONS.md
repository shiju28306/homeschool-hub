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

## 2026-10-19 Grok content cycle
- Added Rhyme and Syllables: Listening Games, ages about 3–5: eight A4 picture-only pages (rhyme match, odd one out, rhyme cards, clap the syllables, clap-and-sort mat, parent note, answers); Quality passed sha256 f5fcfb88…; page, homepage card, ages 3–5 and 5–7 links and sitemap entry; inventory now 24 packs. Generator kept outside the repo at /workspace/printables/rhyme-syllables/make_rhyme_syllables.py.

## Reviewable business draft (not a published offer)
- Keep the existing narrow hypothesis: “10-minute Number Confidence”, ages about 4–6, for parents unsure how to progress beyond counting. Four weeks, 20 original sessions, readiness check, exact adult prompts, common-error support, worked answers and easier/stretch routes. Existing free packs stay free; the proposed paid value is guided progression. €9 remains an untested price hypothesis.
- Concrete sample session: “Hide five”. Materials: five large safe objects and an opaque cup, supervised by an adult. (1 min) Count all five together. (2 min) Show two, cover three; ask “There are five altogether. Two are here. How many are hiding?” (3 min) Uncover, count and explain “Two and three make five”; repeat with 1+4 and 4+1. (2 min) Let the child choose the hidden group. (2 min) Ask them to show a different way to make five. Easier: use three objects and uncover freely. Stretch: predict all ways with five, including 0+5 and 5+0. Answers: hidden counts 3, 4, 1 respectively. Record adult observations only; do not collect child identifiers.
- Adult feedback draft: Were materials/preparation clear? Could you start without asking for help? Which prompt confused you? Was ten minutes realistic? Would a sequenced follow-on be useful, and why? What would you pay, if anything? No outreach or data collection performed. Five-adult usability gate in the backlog is a proposed decision rule, not market evidence.
- Evidence versus assumptions: official Year 1 curriculum supports number bonds within 10 and o’clock learning, but does not establish buyer demand: https://www.gov.uk/government/publications/national-curriculum-in-england-mathematics-programmes-of-study/national-curriculum-in-england-mathematics-programmes-of-study . Buyer need, conversion and price all need validation.
- Hosting suitability: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits prohibits Pages use primarily for online business/e-commerce or facilitating commercial transactions. Preserve the free educational site; do not install checkout or publish a paid offer here. An independently hosted storefront is only a proposal requiring authorization and renewed suitability checks, not a hosting migration.
- Candidate route: Payhip Free Forever advertises $0/month plus 5% per transaction; Stripe/PayPal processing charges are additional (https://payhip.com/pricing, checked 19 October). Zero upfront price does not mean fee-free sales. No merchant account, terms, payment integration, affiliate link or sales obligation created.
- Next decision: validate an original sample with consenting adults only after outreach authorization; inspect any existing Search Console report if access becomes available. Keep selling drafts unpublished until hosting suitability, transaction fees and explicit authorization are resolved. Grok's schedule remains unverified and unchanged.

## 2026-10-24 three-day cycle: Day 1 complete, NOT LIVE
- Resource: Comparing Lengths with Equal Units, ages about 5-7, four A4 pages.
- Dedicated draft branch: codex/cycle-2026-10-24-comparing-lengths. Base main: 8b05b5f1704aaf8b300754661c104af34f14afc9. Resume this branch's latest commit; do not restart or merge before Day 3.
- Main inventory 24 packs; recent history includes Grok's Euro Coins and Rhyme/Syllables; no open PRs or other branches at initial inspection. No AGENTS.md or custom workflow in recursive tree. No existing measurement pack. No Grok work changed.
- Exact paths: assets/Kids-Comparing-Lengths-Pack.pdf; assets/comparing-lengths-preview.png; packs/comparing-lengths.html; tools/generate_length.py. Generator uses ReportLab and installed DejaVu Sans. Rerun from any directory; output resolves relative to generator.
- Exact PDF SHA-256: 959356a0cf4d8e6d161dc64b825fd7af8ff713d7da76d2851c48f3312524b5c6.
- Preview SHA-256: 7dcc56753fff3ae0fb93eb09ba01ca10dea4a3f9561312797ff29f279241a155.
- Research specialist verified DfE Year 1 guidance supports comparison and non-standard measurement: https://www.gov.uk/government/publications/national-curriculum-in-england-mathematics-programmes-of-study/national-curriculum-in-england-mathematics-programmes-of-study . This supports skill selection, not market demand or a claim of Irish curriculum coverage.
- Marketing specialist: first measuring activity for children who can count; descriptive title/meta and links to numbers-1-10 and shapes. Four pages in final copy (supersedes initial three-page brief).
- Independent quality specialist preliminary review: all answers checked, all four rendered pages inspected. Fixed irregular Helvetica spacing by embedding DejaVu; clarified question 4 Yes/No instruction. Re-rendered all pages and reviewer found no clipping, overlaps or unclear diagrams. This Day 1 review is NOT a substitute for Day 2 or publication approval.
- Lead checks: PDF opens as four A4 pages; extracted all text; counted diagrams from generator; relative page targets exist in current tree/new assets; #packs and #newsletter anchors exist. External font URLs inherited unchanged; not revalidated. Browser pack-page layout not yet checked.
- Day 2 (25 October target): retrieve exact draft branch and hash, independently recheck every answer, language, originality/age scope; render and inspect EVERY page, fixing and repeating affected checks. Persist review evidence and new hashes if changed. Include Sunday recap from fresh repository history.
- Day 3 (26 October target): fresh main/branches/PRs/required-check inspection; detect any new duplicate or overlapping Grok work. Add homepage card, ages 5-7 link, resource count and sitemap using fresh main only at this stage. Those integration edits are deliberately pending today. Validate ALL new links and final page/print files. Publish only exact approved bytes, obey protection/checks, verify deployment and live PDF checksum. Delay if any gate fails.
- Publication state: DRAFT ONLY. No new live URL; intended eventual path /homeschool-hub/packs/comparing-lengths.html must not be reported live.
- Cost: only existing included tools and local installed libraries; branch-only Git data storage, no custom Actions workflows, deployment, purchases or metered service added. No billing settings inspected/changed.
- Measurement: current homepage still has no searched analytics/Search Console marker; account/DNS verification unknown. Visits/download interest/sales remain unknown. Business hypothesis remains the earlier Number Confidence draft; no paid offers or outreach. No unsupported demand claims.
- Remaining work: Day 2 independent review, Day 3 fresh final/integration checks and live verification. Do not compress stages on a retry; Day 1 is already complete.

## 2026-10-25 three-day cycle: Day 2 review PASSED, NOT LIVE
- Resumed exact draft commit 428f1fa8b7b54ffe566ba0a4c6dbb8567d5bccc3 on codex/cycle-2026-10-24-comparing-lengths, PR https://github.com/shiju28306/homeschool-hub/pull/1. Fresh main remains 8b05b5f1704aaf8b300754661c104af34f14afc9; only this PR and draft branch are open. No AGENTS.md or custom workflow in current tree. Older local uncommitted work was left untouched; used a separate clean checkout.
- Independent quality specialist rendered and visually inspected EVERY page (4 A4 pages, 1400-pixel renders). Readable monochrome layout, aligned endpoints, consistent equal units, no clipping, overlaps or ambiguous diagrams. No correction required.
- Educational check: page 2 answers B, B, A, Yes; page 3 A=3, B=5, C=8, D=6; longest C, shortest A; B-A=2. Parent model 4 versus 6 and optional 7-5=2 checked. Instructions, spelling, adult-read/spoken-answer support and count-to-8 prerequisite suit approximate ages 5-7. Research confirms no equivalent measurement pack among the 24 existing resources; this is repository distinctness, not a global originality claim.
- Exact approved PDF bytes unchanged: SHA-256 959356a0cf4d8e6d161dc64b825fd7af8ff713d7da76d2851c48f3312524b5c6. Preview unchanged: 7dcc56753fff3ae0fb93eb09ba01ca10dea4a3f9561312797ff29f279241a155. Generator and pack page unchanged.
- Lead checked all 9 relative href/src targets including PDF, preview, stylesheet, related packs, homepage and #packs/#newsletter anchors. All resolve. PDF text bounding boxes fit margins on every page; minimum font 9pt in footer. Marketing independently checked descriptive title/meta/canonical/OG URLs, preview alt text and parent copy; no blocker.
- Day 3 remains pending: fresh main/branches/PRs/protection/checks inspection; homepage card, ages 5-7 navigation, count 24 to 25, sitemap entry; final links/printable verification; publish only exact checked files; verify deployment, live page and live PDF hash. Browser pack-page layout remains unverified. Do not merge early or claim a live resource.
- Next backlog candidate after this cycle publishes: Read a Picture Graph to 5, three categories, one symbol per item, count/most/least/equal. No equivalent found. Not drafted this run.
- Sunday recap from fresh main history, 19-25 October: 19 October added Telling Time to the Hour (b740dcc) and Rhyme and Syllables (8b05b5f), taking inventory to 24. No main commits 20-25 October as of this review. Length-comparison draft saved 24 October and independently reviewed 25 October; neither counts as published content. For an inclusive 18-25 October view, 18 October also added Euro Coins, subitising guidance and the visual redesign.
- Costs and business: only included specialist/GitHub tools, local rendering and a draft-branch documentation update; no added workflows, deployments, paid operations, tracking or outreach. No searched analytics/Search Console marker; account/DNS verification unknown. Visits, downloads and sales remain unknown. Paid-product proposal unchanged and unpublished.
- Status: Day 2 COMPLETE; no detected PDF/content/link defect. Day 3 final integration and deployment checks are the remaining gates, target 26 October subject to passing. No live change this run.

