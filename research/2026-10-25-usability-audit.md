# Navigation, consistency and curriculum audit

## Goal and method

Make Waylantern usable by a reader who does not know technology job titles, prerequisites or the difference between a repository, a course and a learning sequence. The user also requested a learning recipe for every listed profession.

The review inspected the actual generated pages, source metadata, eleven first-project guides, all six profession groups and the generator. Independent review passes covered novice navigation, taxonomy, resource metadata, prerequisites and code contracts. We checked realistic reading journeys and the generated link graph. This was a repository inspection and heuristic usability review, not a study with recruited users.

## Findings and implemented changes

| Finding | Evidence before the change | Change |
|---|---|---|
| Too many initial decisions | The README had 141 links and presented eleven routes, nineteen areas, six intentions and seven formats. | Four primary doors: first step, understand professions, follow a curriculum, find a resource. The detailed indexes moved to their own pages. |
| Large, poorly prioritised profession index | The profession index listed 133 roles, had 183 links and began with architecture; group pages lacked a local index. | Six plainly described groups in an editorial order, local role tables, direct recipe links and experience labels. Source reference details have their own page. |
| Learning recipes absent | Ninety profiles lacked even a short starting guide. The existing guides were small projects, while another page called third-party material “full paths” and a “free university”. | Every profile has an editorial curriculum with prerequisites, ordered topics, practical work and checkpoints. Short first-project guides, external programmes and profession curricula now have distinct labels and destinations. |
| Prerequisites hidden at the point of choice | Introductory Python, React, Node, pandas and pytest resources required prior skills despite the global claim that beginner meant no prior knowledge. Architecture needed an automated test that Path 0 did not teach explicitly. | Topic-relative level labels, explicit prerequisites for those resources, entry metadata for every guide and a testing bridge before architecture. |
| Advanced repositories appeared before guidance | Web highlighted Type Challenges and Cypress before the first-project route; several selections omitted their difficulty before linking outside the directory. | First-project orientation and curriculum access precede expandable repository selections; level and access remain visible with each selection. |
| Inconsistent Spanish orientation | The Spanish home prescribed two weeks and linked to a vague English “Start here”, while the English guide used checkpoints without deadlines. | Both generated home pages expose the same four destinations and checkpoint-based progress. The Spanish page states which detailed pages are in English. |
| Ambiguous free and total labels | API-dependent examples had free reading access; the headline called the English subset the total. | Access refers to material/software, with running costs visible in resource details. Totals explicitly distinguish the whole catalogue, English availability and other languages. |
| Misleading resource metadata | MIT OCW described itself as a collection requiring the reader to assemble a route, but was categorised as a full path. The Spanish freeCodeCamp edition counted as English because an English edition existed separately. Tiimo language metadata was based on a site footer. | MIT OCW moved to reference; the Spanish publication is recorded as Spanish; Tiimo is narrowed to confirmed English source content with the app-language limitation preserved. |
| Source checks hard to inspect | Dates and source notes were kept in YAML but largely absent from the area tables. Profession pages repeated long source-status text hundreds of times. | Expandable resource details expose dates, methods, notes, costs and requirements. Profession sources remain separately inspectable with their original statuses and legacy anchors. |
| Fragile Markdown tables and repository links | A valid description containing a literal pipe could add a table column. GitLab subgroups were truncated. | Table cells escape pipes and line breaks; repository links preserve GitLab subgroups. Regression tests cover both. |

## Learning recipes for all profiles

The six curriculum source files cover all 133 profile IDs exactly once, with 532 ordered stages. Every stage has a practical task and an observable checkpoint. The sequences distinguish entry from zero, stated foundations and work that requires prior practical experience. The senior and management recipes do not imply that reading replaces professional responsibility.

These are Waylantern editorial recipes. They are not verified institution-issued curricula, nor a claim that completing four stages supplies every qualification for a profession. The related official academic recommendations, skills frameworks, vendor courses and certification objectives retain their separate type and source-inspection status.

Resource coverage is explicit: 203 stages currently record a missing or incomplete learning reference. Some are independent capstone tasks whose exact combined project has no dedicated source; others are substantive gaps in specialised topics such as physical hardware, finance, legal/compliance work, healthcare data or advanced management. The recipe shows the task and the exact missing coverage instead of assigning an unrelated Python or security resource. Filling these source gaps is further research work.

## Content and compatibility preserved

- All 325 resource records remain in the catalogue.
- Current language metadata yields 314 entries available in English and 11 in other languages; the earlier English count was 315.
- The eleven first-project guide slugs, six profession-group slugs, role anchors and source anchors are preserved.
- Old home-page fragment links lead to the corresponding secondary indexes.
- Profession profiles link to their recipes, and recipes link back to the profile, related sources and resource details.
- Resource details retain the original source-check dates; an editorial metadata correction is not a new external verification.

## Validation and limits

Unit tests cover complete recipe coverage, unknown resources, invalid data, missing checkpoints, explicit resource gaps, experience gates, navigation, source status, table formatting and safe generation. Site-level checks follow generated internal links and anchors and ensure the generated pages are reachable from the home page. Invalid curriculum data must prevent writes or deletion of existing documentation.

The review did not run all external learning projects, conduct accessibility testing of third-party sites, measure employment outcomes or resolve the blocked academic-source verification recorded in the earlier research. Source and content gaps remain visible; they are not converted into passing claims.

[Open the new home page](../README.md) · [Compare curricula](../docs/curricula.md) · [Browse resources](../docs/catalogue.md)
