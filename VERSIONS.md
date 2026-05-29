# Version History

A durable log of named snapshots you can rewind to. Each entry pins a commit
SHA on `main` so any future session can look it up and restore that state.

## How to rewind to a version

```bash
# inspect a version without changing anything
git checkout <sha>

# or hard-reset a branch back to it
git reset --hard <sha>
```

---

## v1 — pre-vibe-coding baseline

- **Commit:** `99af907` (`Remove Double Exposure label from homepage bottom separator (#1)`)
- **Date recorded:** 2026-05-29
- **Note:** This version is the one before vibe coding started. Clean Webflow
  export baseline (only change from the original export is the removal of the
  "Double Exposure" label at the bottom of the homepage). Rewind here to undo
  all later experimentation.

## v2 — performance pass, before masonry rethink

- **Commit:** `0bc4054` (`Prefetch fullscreen previews as thumbnails enter the viewport (#10)`)
- **Date recorded:** 2026-05-29
- **Note:** The masonry gallery is being rethought from here. This version is
  the stable checkpoint at the end of the performance pass — WebP everywhere,
  responsive `sizes`, above-the-fold priority, lightbox previews at 2000px
  WebP, hover/touch + viewport + neighbor prefetching, and font loading
  prioritized over images across all pages. Rewind here to get the working,
  optimized site before any masonry gallery architecture changes.
