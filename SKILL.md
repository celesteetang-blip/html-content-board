---
name: html-content-board
description: Create polished, responsive HTML content experiences from transcripts, PDFs, PowerPoint files, Word documents, Markdown, notes, images, screenshots, research, and existing HTML. Use for transcript boards, tutorials, training materials, reports, knowledge pages, customer cases, workflow guides, source conversion, and long-form visual content.
---

# HTML Content Board

Create responsive, browser-based content experiences that combine source-faithful text, visuals, navigation, and useful interactions. The goal is not merely to convert files into HTML. The goal is to turn source material into a clear, visual, durable reading experience.

## Core Principles

1. **Source Fidelity First** — Never invent facts, links, quotations, timestamps, statistics, people, citations, product claims, or source material that are not supported by the user's files or approved research.
2. **Content and Visuals Are Designed Together** — Do not build a text-only page first and decorate it later. Slides, screenshots, diagrams, charts, photos, and text should shape the information architecture together.
3. **Responsive Reading Experience (NON-NEGOTIABLE)** — Pages must reflow naturally across desktop, tablet, and mobile. Never force long-form content into a fixed presentation canvas.
4. **Distinctive but Readable** — Avoid generic AI-looking layouts, but never sacrifice comprehension, reading comfort, or source clarity for decoration.
5. **Show, Don't Tell** — When visual direction is genuinely ambiguous, show a small number of real visual previews instead of asking the user to describe abstract design preferences.
6. **Progressive Disclosure** — Read only the supporting rules and templates needed for the current task. Do not load every template, style reference, or optional component by default.
7. **Inspect Before Asking** — If the user already supplied source files, inspect them before asking questions. Do not ask for information that can be inferred from the sources.
8. **Preserve Useful Detail** — Do not silently delete important source content to make the page look cleaner. Reorganize, summarize carefully, add navigation, or move secondary detail into expandable sections.
9. **Zero-Build First** — Prefer standard HTML/CSS/JS that opens locally without a build step. Use a framework only when the requested functionality clearly benefits from it.
10. **Visual QA Is Mandatory** — Render and inspect the final page before delivery whenever the environment supports it. Static code review alone is not enough for layout-sensitive work.

---

## Design Aesthetics

Design must support understanding first and visual distinction second. The page should feel intentionally designed for its specific content, but never sacrifice readability for decoration.

Focus on:

- **Typography** — Build a clear hierarchy for title, section heading, subheading, body, captions, quotes, code, tables, and metadata. Choose fonts that work well for the document language; for multilingual or CJK content, prioritize reliable glyph coverage and reading comfort.
- **Color & Theme** — Use a cohesive palette and CSS variables. Color should clarify hierarchy, chapters, callouts, evidence, and navigation rather than decorate every element.
- **Motion** — Use restrained motion for orientation and emphasis. Prefer subtle section reveals, navigation feedback, and purposeful transitions. Do not animate every card or paragraph.
- **Backgrounds** — Use atmosphere selectively. Long reading sections should remain calm and comfortable. Decorative backgrounds must never reduce text contrast.
- **Components** — Use cards, timelines, quotes, comparison blocks, diagrams, tables, media panels, source notes, and callouts only when they improve information structure.
- **Visual Rhythm** — Alternate text, imagery, whitespace, callouts, and section transitions so long pages remain easy to scan.
- **Source Visuals** — Treat screenshots, PowerPoint pages, diagrams, charts, or photos as primary content when they carry information.

Avoid:

- Purple-gradient-on-white defaults
- Endless rounded cards with identical visual weight
- Dashboard layouts for content that is actually an article, tutorial, transcript, or report
- Excessive pills, badges, glassmorphism, shadows, or floating panels
- Repeating the same two-column layout for every section
- Oversized hero areas that consume most of the first screen without adding information
- Low-contrast text
- Decorative animation that slows reading
- Visual effects unrelated to the content
- Tiny screenshots that cannot be inspected

The goal is not maximum decoration. The goal is a page that feels authored, clear, memorable, and appropriate to the material.

---

## Responsive Layout Rules

These rules apply to every HTML content board:

1. **Natural document flow** — Long-form pages may scroll vertically. Never force them into 16:9 or any other fixed presentation stage.
2. **Responsive reflow** — Layouts must adapt across desktop, tablet, and mobile. Multi-column layouts should collapse intelligently rather than simply shrink.
3. **Readable line length** — Long-form body text should normally stay within a comfortable reading width. Use wider containers only for media, diagrams, tables, galleries, or comparisons.
4. **Mobile-first safety** — At narrow widths, default to a clear single-column flow unless a component genuinely requires another structure.
5. **No accidental horizontal overflow** — The document itself must not create horizontal scrolling. Wide tables, code blocks, and special comparisons may use their own controlled scroll containers.
6. **Responsive type and spacing** — Use fluid CSS such as `clamp()` where useful. Never make mobile text unreadably small to preserve a desktop composition.
7. **Adaptive navigation** — Desktop may use sticky side navigation or a sticky top table of contents. On mobile, convert complex navigation into a compact, collapsible, or horizontally manageable form.
8. **Image integrity** — Never stretch or distort source images. Screenshots, slides, charts, and diagrams normally use `object-fit: contain`; decorative photography may use `cover` when intentional.
9. **Media hierarchy** — Important screenshots and slides must be large enough to inspect. Do not hide critical content in tiny thumbnails.
10. **Tables and dense data** — On smaller screens, use controlled horizontal scrolling, stacked records, or responsive transformations rather than compressing columns until text becomes unreadable.
11. **Touch targets** — Interactive controls must remain comfortably usable on touch devices.
12. **Accessibility** — Maintain strong contrast, semantic heading order, visible focus states, meaningful link text, and useful alt text when context allows.
13. **Reduced motion** — Respect `prefers-reduced-motion`.
14. **Section rhythm** — Long pages need obvious chapter boundaries, whitespace, heading hierarchy, and orientation cues.
15. **Print/PDF sanity** — If the user may print or export the page, avoid layouts that collapse badly in print. Use print CSS when appropriate.

When generating final HTML, read `responsive-base.css` and adapt its rules to the chosen style.

---

## Content Density Modes

Infer the most appropriate density from the task and source material. Do not ask unless the correct mode is genuinely ambiguous.

| Density mode | Best for | Design behavior |
| --- | --- | --- |
| **Immersive / Visual** | Video tutorials, visual walkthroughs, transcript boards, event recaps | Larger media, shorter text blocks, strong chapter moments, key quotes, screenshots, step sequences, generous whitespace |
| **Editorial / Balanced** | Training materials, customer cases, knowledge articles, workflow guides | Balanced text and visuals, comfortable reading width, clear chapter navigation, callouts and media where useful |
| **Research / Reference** | Research reports, detailed analysis, technical material, source-heavy documents | Higher information density, tables, citations, annotations, structured evidence, restrained decoration, efficient scanning |

Defaults:

- Transcript + slides + screenshots → **Immersive / Visual**
- Training guide or customer case → **Editorial / Balanced**
- Research or data-heavy report → **Research / Reference**

Density changes spacing and presentation, not factual completeness.

---

# Phase 0 — Detect Task Mode

Determine the user's primary task before planning the page. Choose one primary mode and borrow rules from secondary modes as needed.

## Mode A — Transcript Board

Use for video, meeting, course, webinar, interview, or podcast transcripts, especially when combined with slides, screenshots, video frames, or links.

Primary goal: turn chronological spoken content into a structured, visual, readable HTML experience.

Typical structure:

- Title and context
- Short overview or key takeaways
- Chapter navigation
- Lightly cleaned transcript
- Relevant slide pages, screenshots, or video frames near the related transcript section
- Key points and quotes
- Tools, websites, documents, or links mentioned in the material
- Timestamps when available and useful

Rules:

- Preserve the speaker's meaning, order, and level of certainty.
- Light editing for readability is allowed: remove filler, repair obvious transcription fragments, normalize punctuation, and split paragraphs.
- Do not rewrite the transcript into a different article unless explicitly requested.
- Match slides and screenshots semantically and chronologically; do not attach visuals randomly.
- If a deck is missing but video frames are available, representative frames may be used as visual anchors.

Default density: **Immersive / Visual**.

## Mode B — Tutorial / Training Guide

Use for step-by-step tutorials, SOPs, workflows, software training, internal training materials, process explanations, course notes, and operational playbooks.

Primary goal: make it obvious what to do, in what order, and why.

Prefer:

- Clear step numbering
- Screenshots near the relevant step
- Before/after examples
- Checklists
- Warnings and common mistakes
- Decision points
- Copyable commands, prompts, or templates when useful
- Expected outcome or success check after major steps

Do not bury actions inside long prose.

Default density: **Editorial / Balanced**.

## Mode C — Research / Report

Use for market analysis, industry analysis, executive or government briefings, technical research, source-heavy reports, and data-heavy documents.

Primary goal: make evidence easy to understand, verify, and navigate.

Prefer:

- Executive summary
- Clear section hierarchy
- Key findings
- Tables and charts where they improve comprehension
- Evidence and source attribution
- Comparison blocks
- Data notes and methodology notes when relevant
- References / further reading

Do not invent missing data or unsupported conclusions.

Default density: **Research / Reference**.

## Mode D — Knowledge Page / Case / Product Content

Use for customer cases, product knowledge, company knowledge, internal reference pages, topic explainers, business cases, project documentation, and durable knowledge pages.

Primary goal: create a reference page that is easier to understand and revisit than the original source files.

Choose density from the source:

- Visual story or case → **Immersive / Visual**
- General knowledge page → **Editorial / Balanced**
- Technical reference → **Research / Reference**

## Mode E — Source Conversion

Use when the main task is converting existing material into HTML, including PDF, PowerPoint, Word, Markdown, notes, or multiple files.

Source conversion is not mechanical format conversion. First determine:

1. What information exists
2. Which visuals belong with which content
3. What hierarchy the source implies
4. What can be reorganized for better reading
5. What must remain faithful to the source

Preserve source meaning, facts, important tables, visuals, and useful links. Do not reproduce a poor original layout merely because it existed in the source file.

## Mode F — Existing HTML Enhancement

Use when the user already has an HTML page and wants it improved, expanded, corrected, or redesigned.

Before modifying:

1. Inspect the existing HTML structure, CSS, JS, assets, and working interactions.
2. Identify what is already correct and should remain unchanged.
3. Understand the requested change before restructuring unrelated sections.
4. Preserve working functionality unless explicitly asked to replace it.
5. Reuse the existing visual system when appropriate instead of introducing an unrelated design language.

After modification, verify desktop, tablet, mobile, navigation, links, images, tables, overflow, and interactive controls.

## Mixed-Mode Tasks

Examples:

- Transcript + PPT + links → primary **Transcript Board**, secondary **Source Conversion**
- PDF research report + request for a better web presentation → primary **Research / Report**, secondary **Source Conversion**
- Existing HTML + new transcript chapter → primary **Existing HTML Enhancement**, secondary **Transcript Board**

Do not ask the user to classify the mode when it can be inferred confidently from the supplied material.

---

# Phase 1 — Source Inspection and Inventory

If source files are already present, inspect them before asking questions.

## 1.1 Build a source inventory

Identify all available source types:

- PDF
- PPT/PPTX
- DOC/DOCX
- Markdown / TXT
- Spreadsheet / CSV
- Images and screenshots
- Existing HTML/CSS/JS
- Transcript files
- Video or audio when extractable
- User-provided URLs or references

For each source, note:

- What it contains
- Whether it is primary evidence, supporting context, or decoration
- Whether text extraction is reliable
- Whether visual inspection is needed
- Whether links or citations are embedded
- Whether there are duplicates or alternate versions

## 1.2 Read before asking

Do not ask questions such as "What is the title?", "How many sections?", or "Do you have content?" if the answer is already visible in the sources.

Ask only for genuinely unresolved choices that materially affect the output, such as:

- Target audience when impossible to infer
- Whether the user wants a faithful transcript vs a heavily rewritten article
- Whether private/sensitive source details should be omitted
- Whether a specific existing brand system must be followed

If those choices are not essential, proceed with sensible defaults and state them briefly at delivery.

## 1.3 Image and visual evaluation

For each relevant visual, determine:

- What it shows
- Whether it is readable at useful display size
- Which section it supports
- Whether cropping is acceptable
- Whether it should be shown full-width, paired with text, placed in a gallery, or excluded

Do not include low-value duplicates merely because they exist.

For more detailed source-handling rules, read `CONTENT_RULES.md`.

---

# Phase 2 — Build the Information Architecture

Create the content structure before coding the full page.

## 2.1 Identify the reader's path

Determine what the reader should understand first, next, and last.

A strong long-form structure often includes:

- Title / context
- Short summary or key takeaways
- Table of contents when useful
- Logical chapters
- Relevant media near the text it supports
- Key insights or callouts
- Sources / links / further reading when supplied
- Clear ending or next-step section when appropriate

Do not mechanically force every page to contain all sections.

## 2.2 Preserve source truth while improving structure

You may:

- Reorder sections for comprehension when chronology is not essential
- Merge redundant source sections
- Split overloaded sections
- Add descriptive headings
- Add concise summaries that are clearly supported by the source
- Convert repeated facts into a table

You may not:

- Invent missing evidence
- Upgrade uncertainty into certainty
- Create fake quotations or links
- Silently omit a major source section merely because it is visually inconvenient

## 2.3 Transcript + deck matching

When a transcript and deck are both present:

1. Identify deck page topics.
2. Identify transcript topic boundaries.
3. Match pages to the nearest related transcript chapter using semantic topic and chronology.
4. Avoid repeating the same slide excessively unless the conversation returns to it meaningfully.
5. If a slide contains critical text, include enough context in HTML that the reader does not need perfect eyesight to understand the point.

---

# Phase 3 — Choose Visual Direction

Read `STYLE_PRESETS.md`.

## 3.1 When previews are useful

Generate up to three small real HTML previews only when:

- The user has not supplied a visual reference
- The source does not imply a strong style
- Visual direction materially affects the result

Previews should use real content from the user's material, not diagnostic labels or fake placeholder copy.

## 3.2 When not to ask for a style choice

Do not stop for style selection when:

- The user already supplied a reference page or screenshot
- The existing HTML has a clear design system that should be preserved
- The task is routine internal documentation and a sensible professional style is obvious
- The user explicitly said to proceed without questions

In these cases, choose an appropriate preset and continue.

## 3.3 Visual reference priority

Use this priority order:

1. Explicit user reference or existing brand system
2. Existing HTML design language
3. Source material's tone and audience
4. Best-fit preset from `STYLE_PRESETS.md`
5. Custom design when no preset fits well

---

# Phase 4 — Generate the HTML

Before generating, read:

- `responsive-base.css`
- `html-template.md`
- `COMPONENTS.md`
- `animation-patterns.md` only if motion is useful

## 4.1 Output architecture

Default to one of two delivery forms:

### Portable single-file HTML

Use when:

- The page is small to medium
- There are few lightweight images
- Easy sharing matters more than file size

Inline CSS and JS. Embed small assets only when practical.

### Folder package

Use when:

- There are many screenshots, slide images, or media assets
- Embedding would create a huge HTML file
- The user wants a maintainable project

Recommended structure:

```text
output/
├── index.html
└── assets/
    ├── images/
    ├── slides/
    └── media/
```

Use relative paths so `index.html` opens locally.

Do not introduce npm, bundlers, or a server unless needed.

## 4.2 Semantic HTML

Prefer semantic elements such as:

- `header`
- `nav`
- `main`
- `section`
- `article`
- `figure` / `figcaption`
- `aside`
- `footer`

Use meaningful IDs for chapter anchors.

## 4.3 Navigation

For long pages:

- Provide a table of contents when it improves scanning.
- Use anchor links to real section IDs.
- Highlight the current section when feasible.
- Ensure sticky navigation does not cover headings after anchor jumps.
- On mobile, navigation must remain compact and usable.

## 4.4 Content components

Choose components from `COMPONENTS.md` based on information need, not decoration.

Examples:

- Summary strip
- Chapter header
- Media + text pair
- Transcript segment + slide
- Step sequence
- Quote block
- Evidence callout
- Comparison table
- Timeline
- Source links
- Expandable secondary detail

Avoid using cards for every paragraph.

## 4.5 Links

- Preserve useful links supplied in the source.
- Use descriptive link text.
- Do not invent URLs.
- External links may open in a new tab when appropriate; if using `target="_blank"`, include `rel="noopener noreferrer"`.
- For local files, use valid relative paths.

## 4.6 Images

- Preserve aspect ratio.
- Add useful alt text when the image meaning can be determined.
- Use captions when provenance or explanation matters.
- Do not place text over busy images unless contrast is guaranteed.
- Do not make source screenshots decorative backgrounds if readers need to inspect them.

## 4.7 Tables and code

- Wrap wide tables in controlled horizontal scroll containers.
- Keep headers visible when useful for long tables.
- Do not shrink text excessively.
- Preserve code whitespace and provide copy affordances when useful.

## 4.8 Multilingual content

- Set the document `lang` appropriately.
- Preserve Unicode text.
- Use font stacks that support the language.
- For mixed Chinese/English pages, avoid layout assumptions based only on Latin word length.
- Preserve proper nouns and source terminology unless the user requests translation.

---

# Phase 5 — QA and Validation

Read `QA_CHECKLIST.md`.

QA is not optional.

## 5.1 Static checks

Check:

- Valid document structure
- `<title>` exists
- viewport meta exists
- `lang` exists
- No duplicate IDs
- No empty anchor targets
- Local asset paths resolve
- Images have appropriate alt text where possible
- No unsupported source claims were introduced

If available, run `scripts/validate_html.py` against the final file.

## 5.2 Visual checks

When browser rendering is available, inspect at minimum:

- Desktop around 1440 px wide
- Tablet around 768–1024 px wide
- Mobile around 375–430 px wide

Look for:

- Horizontal overflow
- Text clipping
- Overlapping sticky elements
- Tiny screenshots
- Distorted images
- Broken media
- Unreadable tables
- Broken navigation
- Excessive empty space
- Visually repetitive sections

## 5.3 Content completeness check

Compare the output against the source inventory:

- Were all major source sections represented?
- Were important visuals used or intentionally excluded for a clear reason?
- Were links preserved?
- Were transcript sections accidentally dropped?
- Were tables or facts altered?

If uncertain, prefer a clearly marked `Need Manual Check` note over invention.

---

# Phase 6 — Delivery

Deliver the finished HTML, not merely a plan.

Briefly report:

- Output file or folder
- Primary task mode used
- Any important assumptions
- Any `Need Manual Check` items
- QA status

Do not overwhelm the user with internal implementation details unless asked.

If the user requested a local file, ensure the delivered package can be opened locally without a development server unless the requested functionality makes that impossible.

---

# Modification Rules for Existing HTML

When editing an existing page:

- Change only what is necessary to satisfy the request.
- Preserve working interactions and source data.
- Avoid full rewrites when a focused modification is safer.
- If a redesign is requested, preserve content and functionality first, then change the visual system.
- Before removing CSS or JS, verify that it is not used elsewhere.
- After every structural change, repeat responsive and interaction checks.

---

# Quality Standard

A successful HTML Content Board should be:

- **Faithful** — source meaning and evidence are preserved
- **Readable** — comfortable on desktop and mobile
- **Visual** — images and media are integrated with purpose
- **Structured** — chapters, navigation, and hierarchy are obvious
- **Useful** — readers can learn, review, or act without returning constantly to the raw files
- **Portable** — opens locally when that is the user's goal
- **Maintainable** — structure and naming remain understandable for future edits
- **Verified** — the page has been checked, not merely generated
