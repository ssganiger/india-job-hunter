# Review of the original skill

## What worked

- Resume-led title discovery avoided a fixed role or employer list.
- Direct career pages, ATS boards, portal results, and recruiter posts gave a useful coverage strategy.
- The original prohibited invented listings and resume facts and preferred direct apply links.
- A tracker, fit analysis, and coverage report made the output useful beyond search.
- The shared `SKILL.md` plus a plain prompt served both file-based skills and assistants without skill support.

## Gaps addressed

| Original behavior | Risk | Revision |
| --- | --- | --- |
| Promised “every” relevant role and typically 40+ searches | An unprovable completeness claim and wasted work | Adaptive search with explicit coverage and stopping criteria |
| Required answers and profile confirmation before any search | A needless stall when the user wants results now | Optional intake, stated defaults, and immediate progress |
| Mandated Research or maximum reasoning settings | These modes vary by product and account | Use available live tools; disclose when browsing is unavailable |
| Forced a long fallback ladder for every blocked source | Low-value retries could dominate the sweep | Targeted retry for promising roles, then a coverage note |
| Scored company quality and compensation even when evidence was absent | Subjective or invented precision | Evidence-based rubric; salary is a separate known-range filter |
| Did not clearly distinguish a search hit from an open role | Stale or closed jobs could appear verified | Explicit verified versus lead status and checked date |
| Repeated the full skill and source appendix in the paste prompt | Drift and maintenance burden | Short standalone prompt with the same core rules |
| Vague repeat-sweep behavior | Duplicate roles or overwritten application statuses | Stable deduplication key and changed/closed/new reporting |
| Installation and privacy claims were overbroad | Users could assume all ChatGPT surfaces load standalone skills or that data never leaves the app | Surface-specific setup and careful privacy guidance |

This is a prompt and packaging review. It does not establish that any job board is always accessible or that live searches will find every vacancy.
