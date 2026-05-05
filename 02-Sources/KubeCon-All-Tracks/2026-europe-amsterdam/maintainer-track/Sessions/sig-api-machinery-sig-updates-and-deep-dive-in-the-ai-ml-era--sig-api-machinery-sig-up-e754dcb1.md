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
themes: ["AI ML", "Community Governance"]
speakers: ["Stefan Schimanski", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2EF4a/sig-api-machinery-sig-updates-and-deep-dive-in-the-aiml-era-stefan-schimanski-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=SIG+API+Machinery%3A+SIG+Updates+and+Deep+Dive+in+the+AI%2FML+Era+CNCF+KubeCon+2026
slides: []
status: parsed
---

# SIG API Machinery: SIG Updates and Deep Dive in the AI/ML Era - Stefan Schimanski, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Stefan Schimanski, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2EF4a/sig-api-machinery-sig-updates-and-deep-dive-in-the-aiml-era-stefan-schimanski-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+API+Machinery%3A+SIG+Updates+and+Deep+Dive+in+the+AI%2FML+Era+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre SIG API Machinery: SIG Updates and Deep Dive in the AI/ML Era.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4a/sig-api-machinery-sig-updates-and-deep-dive-in-the-aiml-era-stefan-schimanski-nvidia
- YouTube search: https://www.youtube.com/results?search_query=SIG+API+Machinery%3A+SIG+Updates+and+Deep+Dive+in+the+AI%2FML+Era+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Or19H4ExOPE
- YouTube title: SIG API Machinery: SIG Updates and Deep Dive in the AI/ML Era - Stefan Schimanski, NVIDIA
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sig-api-machinery-sig-updates-and-deep-dive-in-the-ai-ml-era/Or19H4ExOPE.txt
- Transcript chars: 27165
- Keywords: server, objects, memory, everything, course, basically, second, already, actually, admission, version, feature, paging, request, client, controller, better, clusters

### Resumo baseado na transcript

So, I have a larger part today about the work of the recent releases and future which enables AI workloads and everything is of course about API server and APIs, but there's a special part about that topic. Um but I'm the only one this this this time in Europe who participate, so I'm alone here on the stage. It's also quite an internal thing for managed Kubernetes to um survive updates in a better way. Probably, maybe you have noticed them in in performance, or you saw press announcements by cloud providers running giant clusters, and this is the topic here. So, it's very very hard to uh stay on the safe side, to not uh damage performance, and at the same time get enough consistency. And lots of the features we will see now are critical, are essential to get to that to that scale.

### Excerpt da transcript

All right. Welcome to the sick update API machinery. So, we have a special subtitle today, deep dive into the AI ML era. So, I have a larger part today about the work of the recent releases and future which enables AI workloads and everything is of course about API server and APIs, but there's a special part about that topic. And so, we're representing the sick here. There are a couple of more people, of course. There are two more leads. This is our chair. Um but I'm the only one this this this time in Europe who participate, so I'm alone here on the stage. Um many of you have seen this before. So, in every sick update, we have this overview slide basically what we are doing. Like what is the sick? And obviously, it's about API handling mechanics in the API server. Versioning, serialization, rest mechanics, everything like that. Um everything which is about resource definitions, open API, CRDs, what is kind of what are the features in APIs in the API metadata. Then on the left here, I skip scalability for a second.

Extensibility is CRDs. Mainly, it's admission, of course, as well. And we own that. We own everything in the client mechanics and the core controller mechanics, especially in the uh controller manager. And the last thing here is scalability, but this is kind of a shared owned um topic. There's a sick about scalability as well, and um the sick, of course, has a focus just on the API server, but um it's fluent. Um people work on both sides, of course. What API machinery is not, it's not about like we don't um do API reviews as an API review team in the project. It's not the machinery itself. And we don't own the APIs. We don't own deployments or anything like that. Of course, we own some APIs like admission, everything around admission, but not in general. And um same thing, we we don't own many of the controllers, right? We have some, but many about workloads, especially, we don't own. And kubectl, same same thing. There's a CLI sick and etcd also has its own sick, so um But yeah, this is the overview what we are doing, and updates.

So, let's uh look on the current version, 1.35 1.35, and uh in April there will likely be 1.36, and um there are a couple of caps being promoted and started. And yeah, you see it here in the last column, and we will talk about some of them. Uh a lot of the topics have been started. They haven't been promoted, but it doesn't mean there hasn't been work. It's just like um there are still things missing for GA release.
