---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["David Ko", "SUSE"]
sched_url: https://kccnceu2024.sched.com/event/1YhgL/longhorn-intro-deep-dive-and-qa-david-ko-suse
youtube_search_url: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Longhorn: Intro, Deep Dive and Q&A - David Ko, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: David Ko, SUSE
- Schedule: https://kccnceu2024.sched.com/event/1YhgL/longhorn-intro-deep-dive-and-qa-david-ko-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Longhorn: Intro, Deep Dive and Q&A.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhgL/longhorn-intro-deep-dive-and-qa-david-ko-suse
- YouTube search: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZZblyTjrEwA
- YouTube title: Longhorn: Intro, Deep Dive and Q&A - David Ko, SUSE
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/longhorn-intro-deep-dive-and-q-a/ZZblyTjrEwA.txt
- Transcript chars: 27998
- Keywords: engine, volume, replica, manager, release, support, understand, voling, performance, resource, important, backup, target, create, already, course, actually, remote

### Resumo baseado na transcript

okay uh I think we can get start uh hello everyone I am DAV co uh senior engine manager asusa okay I'm a co-owner of long home project and leading the team to work on Long home we also have uh many contribution from external to help with long home grow okay so today I will talk about uh long home briefly as usual and deep dive and also go into the current status and the future plan for Long home and Q&A okay so uh L home I believe

### Excerpt da transcript

okay uh I think we can get start uh hello everyone I am DAV co uh senior engine manager asusa okay I'm a co-owner of long home project and leading the team to work on Long home we also have uh many contribution from external to help with long home grow okay so today I will talk about uh long home briefly as usual and deep dive and also go into the current status and the future plan for Long home and Q&A okay so uh L home I believe some of you already using L home but I want to overview uh do a overview again to let everybody know more about L itself okay so the agenda uh the first I will go through the long home high level View and project and release updates and also then go into the L details what L suppos and how L works and and how the L inside components work exactly and what the new V2 data engine we are working on and of course IO performance between the V1 and V2 data engine and lastly is what's new in 1. 6 the latest release we just released in February and also what's next Al our long is a ctive distributed uh Bar St system based on KU netics uh it's raw kuber netics as well so it does not need any external dependency to make you able to run L home on kuber netics so it's just based on kuber netics control plan control P patterns and also customer resource let's it and he provide highly available Precision volume so all stuff uh including steady provision or dynamic provision or follower standard nothing different and the important parts long Maring is based on snot Chan so he is a copy and right incremental snot this in cluster but out of Cl we also support remote backup so basically you can set up a remote backup Target and back up your volum use the different patterns periodically or on demand backup and also we know about uh users care about how how to handle this s recovery happen to your volum or even your cluster so cross cluster disas cover or Disaster Recovery we also have a solution for that we call volum and about the installation Lo Target is not just a very strict area with one long can run anywhere so I call here is a pray for agnostic installation so no matters on PR uh cloud or age we also want to Target for that and we also doing some some improvement I will share more later and last is open source own by cnfe R now incubating and we try to Target to graduation so really respect for looking for forward to everyone contribute to Long home as well and high level view are some pillars we are focusing on when we develop long home the
