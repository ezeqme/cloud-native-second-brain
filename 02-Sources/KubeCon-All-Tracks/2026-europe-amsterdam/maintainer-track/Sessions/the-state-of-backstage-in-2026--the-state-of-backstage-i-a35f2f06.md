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
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Ben Lambert", "Patrik Oldsberg", "Spotify"]
sched_url: https://kccnceu2026.sched.com/event/2EF6r/the-state-of-backstage-in-2026-ben-lambert-patrik-oldsberg-spotify
youtube_search_url: https://www.youtube.com/results?search_query=The+State+of+Backstage+in+2026+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The State of Backstage in 2026 - Ben Lambert & Patrik Oldsberg, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ben Lambert, Patrik Oldsberg, Spotify
- Schedule: https://kccnceu2026.sched.com/event/2EF6r/the-state-of-backstage-in-2026-ben-lambert-patrik-oldsberg-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=The+State+of+Backstage+in+2026+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The State of Backstage in 2026.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6r/the-state-of-backstage-in-2026-ben-lambert-patrik-oldsberg-spotify
- YouTube search: https://www.youtube.com/results?search_query=The+State+of+Backstage+in+2026+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tFsp5bpKwdk
- YouTube title: The State of Backstage in 2026 - Ben Lambert & Patrik Oldsberg, Spotify
- Match score: 0.725
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-state-of-backstage-in-2026/tFsp5bpKwdk.txt
- Transcript chars: 32854
- Keywords: backstage, catalog, plugins, plug-in, actions, little, important, scaffolder, working, course, release, actually, pretty, context, support, backend, around, across

### Resumo baseado na transcript

Thank you for coming to see our talk today, the state of backstage in 2026, which is our maintain the track talk at CubeCon EU. Uh we were last here in Amsterdam three years ago uh when we first introduced the new backend system and there's a lot happened since then. Um they've both been working and contributing for many years at this point and between the two of them they are maintainers of five different project areas I think uh across tooling documentation community plugins core framework demo site list goes on and they've also Uh but the problem with that was that each maintainer just got a flood of PRs to handle and it was kind of tricky to focus uh the review effort. So another big challenge for us is to start replacing material UI with backstage UI uh our new design system. Uh but rather than talking about this uh let me jump into a quick demo to show you more.

### Excerpt da transcript

Thank you for coming to see our talk today, the state of backstage in 2026, which is our maintain the track talk at CubeCon EU. Uh we were last here in Amsterdam three years ago uh when we first introduced the new backend system and there's a lot happened since then. Uh we'd like to share today with you what we've been working on since CubeCon in Atlanta last year. So first off, some introductions. You might have seen us before. My name is Ben. I am a senior engineer at Spotify and a maintainer of Backstage. And I have with me, >> hello Patrick go by ragvip on GitHub and also those things. >> Cool. Um first off an agenda. Uh fallen over. Uh as always we're going to start off with some project updates. So some numbers to see how the relevant areas are ticking along. Uh as well as some highlights uh that we'd like to share with you. And then we're going to switch gears a little bit uh and talk about some exciting new updates with the front end system. Um, then we there's some fun things in the CLI uh with regards to authentication and new integrations that we've been working on and we're going to dive into those.

And of course, we're going to talk about back uh AI uh and what that means for backstage and how we think backstage is now more important than ever. And then finally, there's a road map slide uh just telling you what's next for you all and what's next for us, I guess. All right, so first off, some project updates. What has been happening around the project? So, let's start off with some numbers, some general product numbers. Uh we're up to over four. Oh wow, 4,000 adopters. Uh, which is great to see. Uh, the project continue to grow. We have now over 255 open source plugins across the ecosystem, which is really highlighting the extensibility of Backstage and the plug-in model and the strength of it. Uh, and of course the most important number, GitHub stars. We're up to 32.9,000 of those. Nearly 33,000. If everybody that's not start it can start it, we maybe get it over to 33,000 by the end of this talk. Maybe not. Uh um and now a quick look at the community plugins repository. Uh if you're not familiar with this uh this is where all the community maintained plugins live.

So previously the backstage backstage monor repo used to include both the core plugins like the catalog and the scaffolder as well as community contributed plugins too. Uh we've since moved them out into their own repository uh with dedicated tooling and a looser governance model
