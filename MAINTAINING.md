# Maintaining the VideoWeb edition

## Before merging

```sh
python3 scripts/build_catalog.py
python3 scripts/build_showcase.py
python3 scripts/check_content.py
python3 scripts/test_content.py
python3 scripts/build_catalog.py --check
python3 scripts/build_showcase.py --check
git diff --check
```

`prompts/` contains the 120 upstream briefs plus six clearly labeled practice briefs. Build downloads from these files; do not hand-edit downloads. Preserve the core prompt text when adding source attribution or settings guidance outside its code block. Every core brief needs a nearby settings-guide link; each category needs source attribution and its untested status.

`data/x-cases.json` is the source for the gallery and both expanded homepage case sections. It records source URLs, author, prompt availability, media, limitations and localized `homepage` copy. Each case needs a unique `homepage.order` and English/Chinese title, heading, learning point and description. Put uncertainty about model attribution and missing inputs in the visible descriptions. When facts or prompt status change, review both localized descriptions too. Complete-prompt counts are derived from current source status; do not keep a case marked complete merely to preserve a historical count.

Run `python3 scripts/build_showcase.py` to refresh the gallery and the regions between `BEGIN GENERATED X CASES` and `END GENERATED X CASES` in both homepages, including navigation counts. Do not hand-edit those regions or the gallery. Keep the full-width previews expanded. The checks reject stale generated sections, broken explicit case/prompt/settings anchors and missing local Markdown or HTML image paths. They do not test remote image availability or native X playback.

The 13 localized comparison scenes use `<!-- comparison-example-status: untested -->` plus a visible status sentence in their own language. English and Simplified Chinese use the same status convention for their different dialogue examples. Preserve source text in code blocks; have a fluent speaker review edited prose.

## Add an X case

1. Locate the creator's original post, not just a repost or another prompt gallery.
2. Confirm the author's model label and whether the media is a multi-model comparison. Preserve uncertainty.
3. Follow prompt replies. Distinguish complete prompt, partial prompt, external unverified link and demo-only. Missing reference assets or seeds must remain unknown.
4. Record date, canonical URL, actual retrieval method, author and external video URLs. Do not download/relicense third-party media without permission.
5. Explain one useful technique. Original practice briefs must not be described as the source prompt or proven to match the video.
6. Run checks and manually open the preview and original post. If a link expires, retain attribution and mark the result unavailable until repaired.

## Refresh upstream and brand pages

Compare the pinned commit in [UPSTREAM.md](UPSTREAM.md) with the source repository. Preserve VideoWeb links, assets and contribution routing. Recheck model and affiliate pages before changing availability, price or commission claims. Never copy another provider's API limits into the VideoWeb guide.

For reader review, follow: homepage → language entry → use case → complete brief → supported mode → result video → provenance → contribution form. Checks validate files and catalog consistency; they do not validate video quality or platform uptime.

In multilingual review, distinguish inherited material from new work. Check the counts of 120 core briefs, six exercises, one new cover and seven inherited illustrations. Do not call the inherited collection newly authored by VideoWeb. Scene instructions asking for an original character are unrelated and should remain intact.
