# HTML Content Board — Base Template

Use this as an architectural reference. Adapt structure and visual styling to the task; do not mechanically copy every section.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="color-scheme" content="light dark" />
  <title>Content Board</title>
  <style>
    /* Start from responsive-base.css, then add task-specific styling. */
  </style>
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>

  <header class="site-header">
    <div class="container header-inner">
      <div class="brand-block">
        <p class="eyebrow">Context / category</p>
        <h1>Page title</h1>
        <p class="lede">A concise source-faithful summary.</p>
      </div>
    </div>
  </header>

  <nav class="toc" aria-label="Table of contents">
    <div class="container toc-inner">
      <a href="#overview">Overview</a>
      <a href="#chapter-1">Chapter 1</a>
      <a href="#chapter-2">Chapter 2</a>
    </div>
  </nav>

  <main id="main-content">
    <section id="overview" class="section">
      <div class="container reading-width">
        <h2>Overview</h2>
        <div class="summary-grid">
          <article class="summary-item">
            <h3>Key takeaway</h3>
            <p>Supported summary text.</p>
          </article>
        </div>
      </div>
    </section>

    <section id="chapter-1" class="section section-alt">
      <div class="container">
        <header class="section-heading reading-width">
          <p class="eyebrow">Chapter 01</p>
          <h2>Chapter heading</h2>
          <p>Short context paragraph.</p>
        </header>

        <div class="media-text">
          <figure class="media-panel">
            <img src="assets/images/example.png" alt="Describe what the source visual shows" />
            <figcaption>Source-aware caption when useful.</figcaption>
          </figure>

          <article class="reading-width prose">
            <h3>Subtopic</h3>
            <p>Body text...</p>
          </article>
        </div>
      </div>
    </section>

    <section id="chapter-2" class="section">
      <div class="container reading-width prose">
        <h2>Another chapter</h2>

        <aside class="callout" aria-label="Key insight">
          <strong>Key insight</strong>
          <p>Use callouts only when they improve scanning or emphasis.</p>
        </aside>

        <div class="table-scroll" role="region" aria-label="Comparison table" tabindex="0">
          <table>
            <thead>
              <tr><th>Item</th><th>Details</th></tr>
            </thead>
            <tbody>
              <tr><td>A</td><td>Example</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container reading-width">
      <p>Sources, notes, or further reading when provided.</p>
    </div>
  </footer>

  <script>
    // Add only useful interactions: TOC state, disclosure controls, copy buttons, etc.
    // Keep the page fully readable if non-essential JavaScript fails.
  </script>
</body>
</html>
```

# Architecture Rules

## Container strategy

Use at least two conceptual widths:

- **Reading width** for paragraphs and long-form copy
- **Content/media width** for screenshots, diagrams, tables, galleries, and comparisons

Do not force everything into one narrow column or one full-width canvas.

## Section IDs

- Use stable, meaningful IDs such as `overview`, `workflow`, `qa-release`, or `chapter-03`.
- Anchor links must point to real IDs.
- Apply `scroll-margin-top` so sticky navigation does not cover headings.

## Progressive enhancement

The page should remain understandable without complex JavaScript. JavaScript may enhance:

- Active table-of-contents state
- Collapsible secondary details
- Copy buttons
- Lightbox or image expansion
- Search/filter for large reference pages

Do not make the core content dependent on a heavy JS runtime.

# Common Content Patterns

## Transcript segment + visual

```html
<section class="transcript-section" id="chapter-03">
  <header class="section-heading">
    <p class="timestamp">12:40–18:15</p>
    <h2>Finding decision makers</h2>
  </header>

  <div class="media-text">
    <figure class="media-panel">
      <img src="assets/slides/slide-07.png" alt="Slide showing decision-maker research workflow" />
      <figcaption>Related deck page</figcaption>
    </figure>

    <article class="transcript-copy prose">
      <p>Lightly cleaned transcript...</p>
    </article>
  </div>
</section>
```

## Tutorial step

```html
<article class="step" id="step-03">
  <div class="step-number" aria-hidden="true">03</div>
  <div class="step-body">
    <h3>Connect the source</h3>
    <p>Explain the action and reason.</p>
    <figure>
      <img src="assets/images/step-03.png" alt="Screenshot showing the source connection screen" />
    </figure>
    <p class="success-check"><strong>Success check:</strong> The source appears in the connected list.</p>
  </div>
</article>
```

## Source links

```html
<ul class="source-links">
  <li><a href="https://example.com">Descriptive source title</a></li>
</ul>
```

Never fabricate missing URLs.

# Packaging Guidance

For a **single-file deliverable**, inline CSS and JS and embed only practical-size images.

For an **asset-heavy board**, prefer:

```text
output/
├── index.html
└── assets/
    ├── images/
    ├── slides/
    └── media/
```

Keep paths relative so the project opens locally.
