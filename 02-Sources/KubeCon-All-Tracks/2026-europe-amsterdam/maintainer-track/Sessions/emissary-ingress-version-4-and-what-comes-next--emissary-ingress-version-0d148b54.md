---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccnceu2026.sched.com/event/2EF4L/emissary-ingress-version-4-and-what-comes-next-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+What+Comes+Next+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Emissary-ingress: Version 4 and What Comes Next - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Flynn, Buoyant
- Schedule: https://kccnceu2026.sched.com/event/2EF4L/emissary-ingress-version-4-and-what-comes-next-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+What+Comes+Next+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Emissary-ingress: Version 4 and What Comes Next.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4L/emissary-ingress-version-4-and-what-comes-next-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+What+Comes+Next+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LIlW-iYpB1k
- YouTube title: Emissary-ingress: Version 4 and What Comes Next - Flynn, Buoyant
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/emissary-ingress-version-4-and-what-comes-next/LIlW-iYpB1k.txt
- Transcript chars: 9914
- Keywords: emissary, version, company, release, envoy, actually, anybody, pretty, better, probably, conversion, webhook, datawire, couple, upgrade, security, everything, already

### Resumo baseado na transcript

All right, I think we can go ahead and get started because I don't want to be in between anybody in their flight home or anything like that. There are not going to be a lot of people here, I suspect, it being 3:15 p.m. We know has security flaws and there will not be another Emissary 3 release full stop ever again. Um the challenge with the conversion webhook, as always, is that the API server is fairly unhappy if you try to delete old stored versions before you know that those versions are no longer stored. >> [sighs] >> Raise your hand if you've taken a look at the storage version migrator at any point? Um the storage version migrator is a controller that's supposed to run and migrate storage versions for you.

### Excerpt da transcript

All right, I think we can go ahead and get started because I don't want to be in between anybody in their flight home or anything like that. There are not going to be a lot of people here, I suspect, it being 3:15 p.m. on the last day. So, please feel free, move on up front so I feel a little bit less like I'm just lecturing. Um but yeah, we'll just go through a couple of things pretty quickly. First question, is there anybody in the room who is new to the concept of Emissary and wants me to go through the whole what the point is and why we're doing things? No? I didn't think so. All right. Um you know who I am, I'm sure. I'm Flynn. I'm at Buoyant these days. This is the most relevant point in this slide. Emissary 4 is out. It's uh 4.0.1 because we ran into a CID glitch on 4.0.0. If you try to do a Helm install on 4.0.0, it will work. You'll get images that claim to be 4.0.0.rc.2. Um it's the the binaries are identical to the ones for 4.0.1 GA. If you want to use 4.0.0 and understand that the RC will label itself, um feel free.

But otherwise, you can use 4.1 and it should be great and it should call itself 4.0.1 and that will make people happy. If you are still using Emissary, I would really love it if you would upgrade to V4. The reason is that 3.10 is a lot which was the last Emissary 3 that we did is using a version of Envoy that we know has bugs in it. We know has security flaws and there will not be another Emissary 3 release full stop ever again. So, go to 4, your life will be better. Big thanks to the folks who helped out with this thing, especially Mark S and Phil Pevler. Those are a couple of maintainers of ours. Uh but also Jeremy Dental was extremely helpful on doing some production testing before we actually rolled everything out and that made a huge difference. That was lovely. Um this is the other obvious bit that I wanted to encourage here. Uh 4.0 has taken a long time in part because a very small number of people are working on it. So, come and help if you want to keep using this. If you don't want to keep using it, let me know that you don't want to keep using it and then we can go and turn it off, right?

Um I am going to skip all of these just for a moment cuz y'all already know about them. So, let's talk about this stuff instead. The point of Emissary version 4 is in fact getting to a place where it is easy to go and consume new releases of Envoy and easy to do dependency updates and easy to build new releases so that the project as a
