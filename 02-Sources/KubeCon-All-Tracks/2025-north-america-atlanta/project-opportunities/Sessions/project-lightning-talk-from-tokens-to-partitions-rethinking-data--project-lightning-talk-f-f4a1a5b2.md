---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Daniel Blando", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5s/project-lightning-talk-from-tokens-to-partitions-rethinking-data-distribution-in-cortex-daniel-blando-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+From+Tokens+To+Partitions%3A+Rethinking+Data+Distribution+In+Cortex+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: From Tokens To Partitions: Rethinking Data Distribution In Cortex - Daniel Blando, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Daniel Blando, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5s/project-lightning-talk-from-tokens-to-partitions-rethinking-data-distribution-in-cortex-daniel-blando-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+From+Tokens+To+Partitions%3A+Rethinking+Data+Distribution+In+Cortex+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: From Tokens To Partitions: Rethinking Data Distribution In Cortex.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5s/project-lightning-talk-from-tokens-to-partitions-rethinking-data-distribution-in-cortex-daniel-blando-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+From+Tokens+To+Partitions%3A+Rethinking+Data+Distribution+In+Cortex+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hlDqFMdXPQ8
- YouTube title: Project Lightning Talk: From Tokens To Partitions: Rethinking Data Distribution In... Daniel Blando
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-from-tokens-to-partitions-rethinking-data-distr/hlDqFMdXPQ8.txt
- Transcript chars: 6516
- Keywords: gestures, cortex, request, information, series, basically, actually, receive, partition, tokens, partitions, prometheus, distributor, gesture, cluster, approach, chances, trying

### Resumo baseado na transcript

I'm going to try to dive deep in one of the problems that we are we have. Uh just an overview because I want to talk about Cortex and what we do. So it's a a huge receive this data and it basically is a storage layer. So we have each one go to three random in gestures which works fine for us but the problem comes when we have two in gestures down for example. The problem here with this token approach is when we are talking about a cluster with 500 million time series, which a request comes with 5,000 time series and we have a thousand in gestures. So, and what's neat about this is with scale and that's the idea of cortex when you're scaling Prometheus when you start to add partitions when you start to add in gestures your chances of going down actually decreases a lot because you have more

### Excerpt da transcript

My name is Daniel. I'm one of the maintainers of Cortex. And I want to try something different here. I'm going to try to dive deep in one of the problems that we are we have. We have a bunch of challenge in Cortex. I want to see if you guys get interested of what we are doing there. Uh just an overview because I want to talk about Cortex and what we do. Cortex uh I don't know how much of guys are familiar with Prometheus. Prometheus is a very well-known CNSF project for handling metrics. It has a injection matrix. It has a query metric that you can use promql and cortex is basically a scalable promethus. That's what we are trying to achieve. Uh we have high availability. We have multenants and we have long-term storage in cortex. Uh which on top of promeus. We actually use promeus a lot as engine for ourselves. So how does cortex works and that's maybe be a bunch uh but what we try to do is is split promeus in a lot of micros microservices. So we have a bunch of microser for each for each type of request that you are doing.

Uh I want to focus here in the remote write path which is basically the remote right for prometheus. So in cortex we have main uh two services two microservices for that area which we call distributor and in gestures. The distributor is basically a proxy uh you can take a look at as that it receives a request. It shards the information and inside gestures. The in gesture is normally a fleet. When you're when you're talking about flips, we are saying that a cluster cluster core text can receive 500 millions one billion time series. So it's a a huge receive this data and it basically is a storage layer. So it's receive the data and putting on disk and the way that they communicate is using this ring which is in the middle like thing. Uh so what what happens is inest when it joins it's putting in the ring distributor looks at the ring and knows where to send the data. So how this ring looks like? So right now we use tokens in the ring. So when we in gestures is starting uh we add tokens for it. We generate random tokens for that in gestures.

Let's say token four here. And in gestures one itself adds itself to the ring and it basically owns that part of the ring. That's that's basically how it works. And when distributor receive information, it hash that information with that hash. It looks at the ring to see which injector should receive that information. So let's say that you have hash three that information go to inesture one and so on
