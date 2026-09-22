# Your first Wan 3.0 video on VideoWeb AI

[中文](videoweb-workflow.zh-CN.md) · [Home](../README.md) · [120 briefs](../prompts/README.md) · [X videos](x-community-showcase.md)

## Choose the right starting point

| What you have | What to do | First brief |
|---|---|---|
| Only an idea | Choose text input; describe one event | Copy the example below |
| A product photo | Choose image input; upload your own clear photo; describe motion | [Product briefs](../prompts/ads-and-products.md) |
| A designed opening and ending | Use separate start/end fields only when shown | [Production control](../prompts/production-control.md) |
| A reference clip or an existing video to edit | Check for the appropriate mode before using it; do not paste a URL into an image field | [Compatibility notes (Chinese)](model-capabilities.md) |

## Make one short shot

1. Open [Wan 3.0 on VideoWeb AI](https://videoweb.ai/model/wan-3-0/). Sign in if the generator requires it and confirm the selected model name.
2. For the example below, keep the **Video → Text / Image to Video** mode and leave **Start Frame** empty. For image input, click **Choose Start Frame** and use an image you own or have permission to upload.
3. Open the resolution/duration/ratio button and select **10 seconds, 16:9** if offered. Use an available lower-cost resolution for the first attempt. The form controls determine the actual settings; writing “10 seconds” in a prompt does not override them.
4. Paste the brief, review the displayed charge, and generate. Audio instructions apply only when the selected mode supports sound.
5. Watch the entire clip. Check whether the lid opens once, the camera stays fixed, the mug keeps its shape, and steam rises without a jump cut.
6. If it fails, change one item: reduce the lid movement, remove sound, or simplify the action. Keep the original prompt and result for comparison.

```text
10 seconds, 16:9. A plain ceramic travel mug sits on a wooden kitchen counter beside a bright window. The camera stays fixed at tabletop height. During seconds 0–2 the closed mug remains still. During seconds 2–6 an adult hand lifts the hinged lid once and moves out of frame. During seconds 6–10 a thin curl of steam rises while the mug stays completely still. Soft morning light, realistic ceramic texture. If audio is supported: one gentle lid click and quiet room ambience. Preserve mug shape, handle position and lid hinge. No logos, writing, extra fingers, camera cuts or melting objects.
```

This is an untested editorial brief. It is not the prompt used for any linked community video.

<a id="adapt-settings"></a>

## Adapt a longer or more advanced brief

In the source templates, T2V means text-to-video, I2V means image-to-video, and R2V means reference-to-video. These are workflow labels, not necessarily buttons or modes available on VideoWeb.

- **Unsupported duration:** the inspected text-mode form offered 5, 10, 15, 20, 25 and 30 seconds. For an 8- or 12-second source brief, choose a suitable offered duration and retime every beat; prompt text cannot create a missing duration option.
- **Unsupported aspect ratio:** choose an available ratio, keep the important action away from the edges, then crop in an editor. A brief requesting 2.39:1 does not mean the form offers it.
- **Too many shots:** split a 30-second montage into three 10-second tasks; repeat the subject description and edit the results together.
- **No reference or video-edit mode:** use an owned still in image mode, or rewrite the event as text. This is a new generation, not a faithful edit of the original clip.
- **No end-frame field:** describe the desired final composition, but do not claim the ending is locked.
- **No native sound:** create the visual clip and add licensed audio in an editor.

## Keep a useful test record

Copy [the result template](../templates/generation-record.md). Record the exact prompt, date, platform/model label, input roles, settings, charge, result URL and failures. Never record API keys or private account details. A single attractive frame does not prove the motion, dialogue or product continuity worked.

The [brand model page](https://videoweb.ai/model/wan-3-0/) and its public form were checked on 2026-09-22. This guide documents a browser workflow, not a tested API integration or an uptime guarantee. Costs and available controls must be checked in the actual form. For broader directing advice, see the [prompting guide (Chinese)](prompting-guide.md) and [troubleshooting handbook (Chinese)](troubleshooting.md).
