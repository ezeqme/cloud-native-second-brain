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
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Wojciech Tyczyński", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF5M/what-happens-in-kubernetes-sig-scalability-intro-+-deepdive-wojciech-tyczynski-google
youtube_search_url: https://www.youtube.com/results?search_query=What+Happens+in+Kubernetes+SIG+Scalability%3A+Intro+%2B+DeepDive+CNCF+KubeCon+2026
slides: []
status: parsed
---

# What Happens in Kubernetes SIG Scalability: Intro + DeepDive - Wojciech Tyczyński, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Wojciech Tyczyński, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF5M/what-happens-in-kubernetes-sig-scalability-intro-+-deepdive-wojciech-tyczynski-google
- Busca YouTube: https://www.youtube.com/results?search_query=What+Happens+in+Kubernetes+SIG+Scalability%3A+Intro+%2B+DeepDive+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre What Happens in Kubernetes SIG Scalability: Intro + DeepDive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5M/what-happens-in-kubernetes-sig-scalability-intro-+-deepdive-wojciech-tyczynski-google
- YouTube search: https://www.youtube.com/results?search_query=What+Happens+in+Kubernetes+SIG+Scalability%3A+Intro+%2B+DeepDive+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QxeklaQkgUY
- YouTube title: What Happens in Kubernetes SIG Scalability: Intro + DeepDive - Wojciech Tyczyński, Google
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/what-happens-in-kubernetes-sig-scalability-intro-deepdive/QxeklaQkgUY.txt
- Transcript chars: 25708
- Keywords: actually, scalability, pretty, request, single, effectively, memory, cluster, feature, server, working, requests, little, ensure, primary, multiple, whatever, actual

### Resumo baseado na transcript

I'm one of the um TLS of six scalability and in this talk I'm going to to talk a little bit what is happening um in the sik and what we are primarily focused on these days. Um so let's start with like a short introduction um of what the SIG actually is is is doing in general. Um so okay so let's talk a little bit about like what scalability really means for Kubernetes. Um like in fact that Kubernetes scalability is really like multi-dimensional problem with like many dimensions really dozens of dimensions. So like uh we you should like when thinking about scalability we should actually think about like all of those um together to to to realize like how what it means for the performance of the cluster. So um you can see the like the the first definition from like the beginning of the project from 2015 like how it was defined and the problem with that definition is that like um the exact same system or the exact same system depending

### Excerpt da transcript

Okay. Hello everyone. Uh my name is Voytech Tachinski. I'm one of the um TLS of six scalability and in this talk I'm going to to talk a little bit what is happening um in the sik and what we are primarily focused on these days. Um so let's start with like a short introduction um of what the SIG actually is is is doing in general. Um so there are like five main themes that uh we are we are involved in or we are working on like first one is like defining what scalability of Kubernetes really is um and like what are the goals what should be the goals from the scalability perspective for for for our community. Um so how far should we go what should be the the the current goals and so on. Um the second one is um oops sorry um monitoring and measuring the performance of the system and the scalability to ensure that um things that we work on actually have the impact that we expect them to be. Um and what is tightly uh coupled with that is um um preserving the the and monitoring if we are not actually regressing the system in the meantime.

either we or like someone else by by um introducing new features that accidentally or not accidentally accidentally actually um affect the scalab negatively affect the scalability of the system. Um the fourth thing is probably the most interesting one which is um making the actual improvements and that is something that I'm going to talk more um in the second part of the presentation. what exactly are the top like improvements that we are or we've been working on and are either delivered or like um in progress. Um and the fifth thing is like working with the community and ensuring that uh they understand the best practices they understand how to ensure that features that they work um will be scalable and so on and so on. Um so okay so let's talk a little bit about like what scalability really means for Kubernetes. Um in general like the the the primary thing that we want or the primary principle that we that we want um that we follow through that we follow with is u is to ensure that we are not optimizing things for the sake of optimization.

like it should always be driven in like real user requirements because every um every optimization brings or almost every optimization brings additional complexity to the system. So we don't want to like introduce additional complexity if no one really cares about that. Um so when we when you ask users about like um if they want really scalability the answer is like of course we we do but
