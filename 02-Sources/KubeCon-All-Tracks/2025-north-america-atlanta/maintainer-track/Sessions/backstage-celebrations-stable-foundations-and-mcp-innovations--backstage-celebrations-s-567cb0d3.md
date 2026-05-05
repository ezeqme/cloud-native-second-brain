---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Ben Lambert", "Patrik Oldsberg", "Spotify"]
sched_url: https://kccncna2025.sched.com/event/27NoR/backstage-celebrations-stable-foundations-and-mcp-innovations-ben-lambert-patrik-oldsberg-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Backstage+Celebrations%3A+Stable+Foundations+and+MCP+Innovations+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Backstage Celebrations: Stable Foundations and MCP Innovations - Ben Lambert & Patrik Oldsberg, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Ben Lambert, Patrik Oldsberg, Spotify
- Schedule: https://kccncna2025.sched.com/event/27NoR/backstage-celebrations-stable-foundations-and-mcp-innovations-ben-lambert-patrik-oldsberg-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Backstage+Celebrations%3A+Stable+Foundations+and+MCP+Innovations+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Backstage Celebrations: Stable Foundations and MCP Innovations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoR/backstage-celebrations-stable-foundations-and-mcp-innovations-ben-lambert-patrik-oldsberg-spotify
- YouTube search: https://www.youtube.com/results?search_query=Backstage+Celebrations%3A+Stable+Foundations+and+MCP+Innovations+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=evmmr-uxNsc
- YouTube title: Backstage Celebrations: Stable Foundations and MCP Innovations - Ben Lambert & Patrik Oldsberg
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/backstage-celebrations-stable-foundations-and-mcp-innovations/evmmr-uxNsc.txt
- Transcript chars: 28435
- Keywords: backstage, plugins, actions, little, scaffolder, plug-in, backend, easier, action, cubecon, catalog, support, cursor, called, framework, create, course, plugin

### Resumo baseado na transcript

Welcome to our maintainer track talk uh for backstage in uh Atlanta 2025. Um the talk title is backstage celebrations stable foundations and MCP innovations. Uh so it was a big driver for the design of our current backstage uh backend system uh which is now fully rolled out. So it really has been a bigger challenge uh to enable declarative integration in the front end system. Now there's some demo magic going on here, but that's all in the control panel. So the demo I just showed only uses plugins that natively support the new front end system.

### Excerpt da transcript

Hello everybody. Welcome to our maintainer track talk uh for backstage in uh Atlanta 2025. Um the talk title is backstage celebrations stable foundations and MCP innovations. I really picked the hardest thing to say on stage over a talk title. Um first off some introductions. Uh my name is Ben. I am a senior engineer at Spotify and a core maintainer of Backstage. and I've been working on it from pretty much day one since we open sourced it I think into the community and today I have with me >> Yep. Hello my name is Patrick uh I am also all of those things and I go by Ragbit on GitHub. >> Cool. Um let's just dive into a little bit of an agenda and what we're going to be covering today. So first off we're going to dive into some project updates just a little bit of numbers slide just to kind of get you all familiar with the project a little bit. Uh and then we're going to jump into a section called project maturity which is more around like the front end and backend systems and a little bit of an update as to where we are where we're at with those.

Um then we have a section just called new stuff. So that's kind of everything that we've been working on since last CubeCon in Europe. And then a road map uh kind of round off at the end just to kind of set the scene for what's hopefully going to come next year or in the next CubeCon. Uh so first off project updates. So, we are at 3 and a half thousand adopters, uh, over 250 open source plugins, and 31.8,000 stores on GitHub. Uh, I updated this yesterday cuz it was 31.7. So, now we've we've jumped a little number that was great. Um, and then for the community plugins repository. So, if people don't know what the community plugins repo is, um, we used to have like one big monor repo just backstage backstage and that contained all of the core framework and all of the plugins that we had. Um, but that kind of didn't really scale. we had a lot of uh traction and a lot of people wanting to contribute plugins um and we needed to come up with a little plan. I think we announced um community plugins in like Detroit maybe Chicago.

Um but some numbers from that repository we have over 200 packages being published from that repository as well as 100 workspaces and most importantly we have 60 people or 60 maintainers over working in that repository to help ship these plugins which is great. Uh I just want to quickly also touch on um some tooling that we've built to improve issue quality. So we notice that there's quite a lo
