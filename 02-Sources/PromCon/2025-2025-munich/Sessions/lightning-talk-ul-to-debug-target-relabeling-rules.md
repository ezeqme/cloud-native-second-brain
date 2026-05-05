---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=g_v02cTviVU"
youtube_id: "g_v02cTviVU"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 45
speakers: ["Julius Volz"]
topics: ["Metrics"]
keywords: ["prometheus", "dropped", "target", "hopefully", "targets", "visualizer", "reabeling", "changed", "lightning", "relabeling", "julius", "though", "awesome", "briefly", "request", "improve", "server", "discovers", "endpoints", "monitored", "discovery", "adding", "happening", "discover"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-ul-to-debug-target-relabeling-rules/g_v02cTviVU.txt"
transcript_chars: 1508
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Ul To Debug Target Relabeling Rules - Julius Volz

## Metadata

- YouTube: https://www.youtube.com/watch?v=g_v02cTviVU
- Playlist: PromCon EU 2025
- Speakers: Julius Volz
- Topics: [[Metrics]]

## Transcript

Do I see it though? >> Yeah. So, you see it here. >> Awesome. Okay. Very briefly. Yeah. I just have a pull request out to improve some people's lives. Um hopefully. So, this Prometheus server has like it discovers three demo endpoints, but only one is being monitored. And I'm like, why? And then I check service discovery and I see some targets that dropped. And you used to not be able to see why they're dropped. And I'm adding like a visualizer here that shows you all the reabeling steps that are happening to a discover target. Um, so you get like the initial discovered labels. Then they go through the first reabeling rule. Then you get like some changed label and shows you the diffs and like oh no an added label, a changed label, removed label and you have something that you know in the end this target is actually kept. Um, and then you have another target that's dropped, for example, because there's an hash mod going on.

Um, and you can now debug this um, with this visualizer. Um, for example, in the end here, it tells you like this keep action doesn't match the right temporary hash of the reabel hashmod. Um, and so the target gets dropped. So, I hope this will help people like debug why their cover targets are getting dropped or not dropped or labeled incorrectly. Um, and yeah, I had this as a standalone tool before at relabeler.promlabs.com, but now I just yeah had like two hours of spare time and uh added that to Prometheus and hopefully it's going to be merged soon. Thank you.


## Related keywords

[[prometheus]] [[dropped]] [[target]] [[hopefully]] [[targets]] [[visualizer]] [[reabeling]] [[changed]] [[lightning]] [[relabeling]] [[julius]] [[though]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
