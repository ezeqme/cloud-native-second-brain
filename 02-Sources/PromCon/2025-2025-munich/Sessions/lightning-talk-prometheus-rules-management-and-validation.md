---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=DIcVPx0J7rQ"
youtube_id: "DIcVPx0J7rQ"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 26
speakers: ["Hervé Nicol"]
topics: ["Collectors", "Metrics", "SLOs", "Kubernetes", "AI Observability"]
keywords: ["prometheus", "clusters", "kubernetes", "cluster", "pipeline", "checks", "prompt", "actually", "validation", "manage", "repository", "package", "deploys", "created", "syntax", "output", "lightning", "management", "wanted", "little", "primeituous", "secret", "behind", "differently"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-prometheus-rules-management-and-validation/DIcVPx0J7rQ.txt"
transcript_chars: 2718
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Prometheus Rules management and validation - Hervé Nicol

## Metadata

- YouTube: https://www.youtube.com/watch?v=DIcVPx0J7rQ
- Playlist: PromCon EU 2025
- Speakers: Hervé Nicol
- Topics: [[Collectors]], [[Metrics]], [[SLOs]], [[Kubernetes]], [[AI Observability]]

## Transcript

So hello. Um I wanted to talk about a little different topic primeituous rules. Um because I okay we talk a lot about them but so far I'm not sure how people manage their rules. Looks like there's something some secret behind that. I don't know. So I can talk about what we are doing at James Swam. And if you were doing differently, please come to me and give me some new ideas. Um, so yeah, the question is about how do you manage Prometheus rules? Who stores their their rules in a g repository? Okay, so far we're all good. Who runs CI tests on their rules? Oh, quite nice. Um so at J and Swam yeah we store our rules in the repository we package them as a Helm chart. Um oh so and we validate them with some CI we package them as a Helm chart we flux deploys them on our on our different clusters where we have some monitoring and and alloy deploys them from from the resources created on Kubernetes to the rulers.

Um so for validation we are using different tools. We are using pines from cloudflare which is really really great in my opinion. We use it so it checks the syntax first of all. Okay. Um it checks for label aggregations. For instance we want for each each aggregation we want to keep the cluster name and stuff like that and team name. So it checks that we keep them. So if someone write the rules and forgets to to group by team or whatever our pipeline fi fails it check that we have some required annotations like the runbook which has to be indicated in each alert and then we also run prompt tool. So um prompt tool does also the syntax check and it runs some unit tests on the rules. So I don't know um who uses pint here. Oh okay. And who who uses prom tool? So I guess all of the others that did some CI checks. Maybe there are some other tools that we I don't know about and I'd love to know about. Um so a bit more about prom tool which was quite of a painoint for some stuff.

So okay so you already answered that. Fine. Um the result of the of the of prompt tool um is a pain to me. I don't know what what's wrong there. How can I find it out? Quite often I had to copy it in a in two separate files to do a proper div. Okay. Useless. And so the an idea that we had um it was two years ago. We did a small hackathon at Jensen Swarm and and we just created this diff output that shows exactly what is wrong in the output. And so we did I I participated it. I was part of it. We pushed a pull request. And the magic thing is that yesterday when I wrote the slide, I saw that this PR had actually been rewrited by my colleague who worked on it with me and was actually merged where I thought it was still pending. So I saw that it's actually available. So yeah, thank you very much. Nice.


## Related keywords

[[prometheus]] [[clusters]] [[kubernetes]] [[cluster]] [[pipeline]] [[checks]] [[prompt]] [[actually]] [[validation]] [[manage]] [[repository]] [[package]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
