# HTML Content Board

A reusable skill for turning transcripts, PDFs, PowerPoint files, Word documents, Markdown, notes, screenshots, research, and existing HTML into polished, responsive HTML content experiences.

## What this skill is for

Use it to create:

- Transcript boards
- Video / course recaps
- Tutorials and SOPs
- Training materials
- Research reports
- Executive briefs
- Customer cases
- Product knowledge pages
- Internal knowledge pages
- Source-file-to-HTML conversions
- Improvements to existing HTML

## Core idea

This is not a slide generator.

It is designed for long-form, responsive web reading:

- Desktop / tablet / mobile reflow
- Natural vertical scrolling
- Source-faithful content
- Text and visuals designed together
- Useful chapter navigation
- Local opening without a build system when possible
- Visual QA before delivery

## Main files

- `SKILL.md` — primary workflow and decision logic
- `STYLE_PRESETS.md` — visual systems for different content types
- `CONTENT_RULES.md` — source fidelity, transcript cleanup, links, tables, translation
- `COMPONENTS.md` — reusable content patterns
- `html-template.md` — base HTML architecture
- `responsive-base.css` — responsive CSS foundation
- `animation-patterns.md` — restrained motion guidance
- `QA_CHECKLIST.md` — final validation checklist
- `scripts/validate_html.py` — lightweight static validator

## Default task modes

The skill detects one primary mode:

1. Transcript Board
2. Tutorial / Training Guide
3. Research / Report
4. Knowledge Page / Case / Product Content
5. Source Conversion
6. Existing HTML Enhancement

Mixed tasks can combine modes. For example:

`transcript + PPT + links` → Transcript Board as primary mode + Source Conversion support.

## Recommended output structures

For small or medium projects:

```text
output.html
```

For media-heavy projects:

```text
output/
├── index.html
└── assets/
    ├── images/
    ├── slides/
    └── media/
```

Keep paths relative so the result can open locally.

## Design priorities

1. Source fidelity
2. Information architecture
3. Readability
4. Visual integration
5. Responsive behavior
6. Accessibility
7. Distinctive design
8. Motion only when useful

## Notes about the original fork

This repository was originally forked from `zarazhangrui/frontend-slides` and is being repurposed into a long-form HTML content skill. Some upstream presentation assets may remain in legacy folders for reference, but the active workflow is defined by the root files listed above.

## Typical example

Input:

- Video transcript
- PDF/PPT deck
- Screenshots
- Key links

Output:

- Clear chapter structure
- Lightly cleaned transcript
- Relevant deck pages matched to the right sections
- Key takeaways and quotes
- Useful source links
- Responsive HTML that works on desktop and mobile
