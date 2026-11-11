# Details that get lost between a design and an app

Go through this for every screen, against the board, before handing the feature over.

## Look
- Every block present, in the board's order; nothing added the board does not have.
- Type: family, size, weight, line height, letter spacing, italics inside a title.
- Colour of every text, surface, border, shadow, the pressed and disabled states.
- Spacing and radii between and inside blocks; card overlaps (a card rising over art).
- Icons: the same glyph, size and stroke; decorative art (scenery, illustrations) ported,
  not simplified.
- Motion that means something: what moves with the time of day, progress that fills,
  sheets that rise, a press that shrinks; durations and easing; reduced motion respected.

## Behaviour
- Every control does what the board's logic does: what opens, what it contains, where
  focus goes, what the back gesture does, what is saved and still there after a reload.
- Each state the board draws: empty, loading, error, long text (Polish and Ukrainian run
  longer), one item / many items, a role that sees less (child, guest).
- Refusals: the words, where they show, what the person can do next.
- Touch targets at least 44 px; nothing scrolls sideways; the keyboard does not cover the
  field being typed in.

## Words
- Every string from the locales, in every language, with plural forms; dates and numbers
  in the person's format. No promise the product cannot keep.

## Widths and devices
- Phone first, then each wider width from `stack.md`: a centred column or a sensible
  two-column layout, never a stretched phone.
- On the phone builds: safe areas, the status bar colour, camera and photo permissions,
  the back gesture, the keyboard.
