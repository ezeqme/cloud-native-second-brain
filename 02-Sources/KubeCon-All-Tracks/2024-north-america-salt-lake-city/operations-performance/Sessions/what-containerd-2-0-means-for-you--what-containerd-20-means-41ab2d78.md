---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Samuel Karp", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7qL/what-containerd-20-means-for-you-samuel-karp-google
youtube_search_url: https://www.youtube.com/results?search_query=What+Containerd+2.0+Means+for+You+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What Containerd 2.0 Means for You - Samuel Karp, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Samuel Karp, Google
- Schedule: https://kccncna2024.sched.com/event/1i7qL/what-containerd-20-means-for-you-samuel-karp-google
- Busca YouTube: https://www.youtube.com/results?search_query=What+Containerd+2.0+Means+for+You+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What Containerd 2.0 Means for You.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qL/what-containerd-20-means-for-you-samuel-karp-google
- YouTube search: https://www.youtube.com/results?search_query=What+Containerd+2.0+Means+for+You+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fDDSg2NVwO4
- YouTube title: What Containerd 2.0 Means for You - Samuel Karp, Google
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/what-containerd-2-0-means-for-you/fDDSg2NVwO4.txt
- Transcript chars: 33625
- Keywords: container, actually, containerd, little, images, changes, version, around, anything, change, schema, upgrade, support, plugins, removed, available, default, implementation

### Resumo baseado na transcript

thanks for making it all the way to the last day of cucon and uh hopefully sticking it out for uh the full day of content that we've got today um I really appreciate you coming here uh my name is Sam I'm a software engineer at Google I'm also a container D maintainer and uh today we're going to be talking about what containerd 2.0 means for you so uh with that said containerd 2.0 is now available um we released it last week it was a long time

### Excerpt da transcript

thanks for making it all the way to the last day of cucon and uh hopefully sticking it out for uh the full day of content that we've got today um I really appreciate you coming here uh my name is Sam I'm a software engineer at Google I'm also a container D maintainer and uh today we're going to be talking about what containerd 2.0 means for you so uh with that said containerd 2.0 is now available um we released it last week it was a long time coming but uh we're really happy it's finally out now um and we're going to spend you know this whole session talking about it so uh I'm excited I hope you are too um what we're going to do is we're going to talk a little bit through the changes that have happened in container d22 container D20 um also we're going to touch on uh why it's a major version why we move from 1.x to 2.0 and what that means in terms of some uh deprecations and removals you know effectively breaking changes that are there uh then we'll talk about um how you can prepare to upgrade what you can do to find out if you're going to be affected by any of the changes that have been made uh and how you can remediate anything where you can find help and and then sort of directionally what's going on next um I'm going to try to have some time for Q&A at the end so I would ask you to please hold your questions until then um also all these slides are going to be online um so don't feel like you need to copy everything down or read every word while I'm talking um because it'll all be available for you to look at later as well so uh with that said let's move on on to what's new um we do have a whole bunch of new stuff in container d2o we've got new features we've got things that were previously experimental in containerd 1.7 that we've now stabilized uh we've got some defaults that have changed a little bit um I'm not going to go through everything that's on this list but I want to touch on a couple things and then we'll have some some deeper highlights um first thing the the transfer service and the sandbox service these were experimental uh things that we actually launched in containerd 1.7 and we have uh now gone through and stabilized them and they're ready for for people to start really using um we've got some improvements in performance in terms of things like image extraction uh some changes and how you can configure otel um we've also got some new defaults like uh NRI turned on by default CDI enabled by default uh and we have support for username sp
