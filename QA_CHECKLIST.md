# QA Checklist

Use this checklist before delivery.

## Source fidelity

- [ ] Major source sections are represented
- [ ] No unsupported facts were introduced
- [ ] No fabricated URLs, citations, quotations, or timestamps
- [ ] Important caveats and uncertainty are preserved
- [ ] Tables retain correct values, units, and meaning
- [ ] Transcript cleanup did not change the speaker's meaning
- [ ] Important visuals are included or intentionally excluded for a clear reason

## Structure

- [ ] Page title is clear
- [ ] Heading hierarchy is semantic and logical
- [ ] Long pages have useful navigation when appropriate
- [ ] Anchor links point to real IDs
- [ ] Sticky navigation does not cover target headings
- [ ] Important actions are not buried inside long prose

## Responsive layout

Inspect at minimum around:
- [ ] 1440 px desktop
- [ ] 768–1024 px tablet
- [ ] 375–430 px mobile

Check:
- [ ] No document-level horizontal overflow
- [ ] Multi-column sections collapse correctly
- [ ] Body text remains readable
- [ ] Images preserve aspect ratio
- [ ] Screenshots and slides remain inspectable
- [ ] Tables remain usable
- [ ] Sticky elements do not overlap content
- [ ] Touch targets remain comfortable

## Assets

- [ ] All local image/media paths resolve
- [ ] No broken images
- [ ] No accidental absolute local machine paths
- [ ] Relative asset paths work from `index.html`
- [ ] Alt text is useful where context allows
- [ ] Captions are present when provenance or explanation matters

## Links

- [ ] No empty `href` values intended as real links
- [ ] No fabricated destination URLs
- [ ] External links use descriptive text
- [ ] `target="_blank"` links include `rel="noopener noreferrer"`

## Accessibility

- [ ] `<html lang>` is set appropriately
- [ ] Viewport meta is present
- [ ] Text contrast is strong
- [ ] Focus states are visible
- [ ] Heading order is logical
- [ ] Interactive controls have accessible names
- [ ] `prefers-reduced-motion` is respected

## Visual quality

- [ ] Design fits the content type
- [ ] Not every paragraph is boxed into a card
- [ ] Section rhythm is varied enough for scanning
- [ ] Decorative effects do not reduce readability
- [ ] Hero area is informative, not merely oversized
- [ ] Callouts are used selectively
- [ ] Repeated layouts do not make the page monotonous

## Technical

- [ ] `<title>` exists
- [ ] No duplicate IDs
- [ ] No obvious malformed HTML
- [ ] No unnecessary framework dependency
- [ ] Page opens locally if local opening is the delivery goal
- [ ] Core content remains readable if optional JavaScript fails

## Delivery

- [ ] Output file/folder is clearly named
- [ ] QA status is reported briefly
- [ ] Any unresolved items are marked `Need Manual Check`
