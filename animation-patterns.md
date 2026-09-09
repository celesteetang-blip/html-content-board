# Animation Patterns for HTML Content Boards

Motion should support orientation, hierarchy, and feedback. It should not compete with reading.

## Core Rules

- Prefer CSS-only motion for simple effects.
- Respect `prefers-reduced-motion`.
- Keep durations short and purposeful.
- Do not animate every paragraph, card, or table row.
- Avoid scroll-jacking and forced full-screen section transitions.
- Core content must remain readable if animation or JavaScript fails.

## Recommended Patterns

### 1. Section reveal

Use a subtle fade/translate when a major chapter first enters view.

Good for:
- Chapter headers
- Major media blocks
- Key callouts

Avoid applying it to every line of text.

### 2. Active table-of-contents state

Highlight the navigation item for the section currently in view.

Use IntersectionObserver when JavaScript is available.

### 3. Expand/collapse secondary detail

Use for:
- Long source notes
- Optional technical detail
- Supplementary transcript material
- FAQ-style detail

Prefer native `<details>` / `<summary>` where possible.

### 4. Copy feedback

For copyable commands, prompts, code, or templates:
- Provide a clear copy button
- Change the button label briefly after success
- Keep feedback non-blocking

### 5. Media expansion

For screenshots or slide images that need inspection, a click-to-expand lightbox may be useful.

Requirements:
- Keyboard closable
- Visible close control
- Preserve image aspect ratio
- Do not make the image impossible to inspect without JavaScript; the inline version must still be useful

### 6. Sticky navigation transition

Sticky TOC/header state changes may use subtle shadow, border, or background transitions when scrolling.

## Avoid

- Auto-advancing carousels for important source content
- Constant parallax
- Large looping decorative motion
- Animated gradients behind long body text
- Excessive stagger delays that make readers wait for content
- Motion that changes layout enough to cause content jumps

## Reduced Motion

Include a reduced-motion fallback such as:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Use smooth scrolling only when it does not harm accessibility or navigation clarity.
