# Maintaining the VideoWeb edition

## Before merging

```sh
python3 scripts/build_catalog.py
python3 scripts/build_showcase.py
python3 scripts/check_content.py
python3 scripts/build_catalog.py --check
python3 scripts/build_showcase.py --check
git diff --check
```

`prompts/` contains the 120 upstream briefs plus six clearly labeled practice briefs. Build downloads from those category files; do not hand-edit downloads. `data/x-cases.json` records external sources, author, prompt availability, media links and known limits. Set each case’s `practice_id` to an existing exercise anchor and update the visible case counts in the English and Chinese READMEs when adding a case. Generate `guides/x-community-showcase.md` with `scripts/build_showcase.py`; do not hand-edit it.

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
