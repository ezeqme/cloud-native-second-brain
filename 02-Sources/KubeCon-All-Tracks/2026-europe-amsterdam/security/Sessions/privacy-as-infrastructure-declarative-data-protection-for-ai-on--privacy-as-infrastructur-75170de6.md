---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["AI ML", "Security", "Storage Data", "Kubernetes Core"]
speakers: ["Joaquin Rodriguez", "Microsoft", "Krishnendu Dasgupta", "AXONVERTEX AI"]
sched_url: https://kccnceu2026.sched.com/event/2CVzv/privacy-as-infrastructure-declarative-data-protection-for-ai-on-kubernetes-joaquin-rodriguez-microsoft-krishnendu-dasgupta-axonvertex-ai
youtube_search_url: https://www.youtube.com/results?search_query=Privacy+as+Infrastructure%3A+Declarative+Data+Protection+for+AI+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Privacy as Infrastructure: Declarative Data Protection for AI on Kubernetes - Joaquin Rodriguez, Microsoft & Krishnendu Dasgupta, AXONVERTEX AI

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joaquin Rodriguez, Microsoft, Krishnendu Dasgupta, AXONVERTEX AI
- Schedule: https://kccnceu2026.sched.com/event/2CVzv/privacy-as-infrastructure-declarative-data-protection-for-ai-on-kubernetes-joaquin-rodriguez-microsoft-krishnendu-dasgupta-axonvertex-ai
- Busca YouTube: https://www.youtube.com/results?search_query=Privacy+as+Infrastructure%3A+Declarative+Data+Protection+for+AI+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Privacy as Infrastructure: Declarative Data Protection for AI on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzv/privacy-as-infrastructure-declarative-data-protection-for-ai-on-kubernetes-joaquin-rodriguez-microsoft-krishnendu-dasgupta-axonvertex-ai
- YouTube search: https://www.youtube.com/results?search_query=Privacy+as+Infrastructure%3A+Declarative+Data+Protection+for+AI+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mkAaguXm1ag
- YouTube title: Privacy as Infrastructure: Declarative Data Protection fo... Joaquin Rodriguez & Krishnendu Dasgupta
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/privacy-as-infrastructure-declarative-data-protection-for-ai-on-kubern/mkAaguXm1ag.txt
- Transcript chars: 30305
- Keywords: privacy, actually, security, everything, running, gpu, llm, pipeline, policy, threat, developer, sandbox, entire, working, environment, architecture, models, observability

### Resumo baseado na transcript

I'm a founder of Axon Vortex AI very focused on decentralized intelligence and healthcare. >> And this is uh privacy infrastructure the clear of data protection for AI on Kubernetes. Uh what we want is an architecture that can prevents us uh to keep that you know privacy um in in place. So uh Kubernetes uh what we're going to be showing today is a Kubernetes first architecture uh for privacy enforcement. uh we're going to be talking about observability and Prometheus uh audit tables and some um thread patterns. xc has full access to the pi you know if you have one crash it's going to crash all the services you know all of these have a shared PIP environment uh it's very difficult to scale uh without a GPU uh there's no network

### Excerpt da transcript

Good afternoon everybody. Uh my name is Hain Rodriguez. Um I'm a software engineer uh with Microsoft. >> And hi, good afternoon everybody. My name is Krishna Dazgupta Kish. I'm a founder of Axon Vortex AI very focused on decentralized intelligence and healthcare. >> And this is uh privacy infrastructure the clear of data protection for AI on Kubernetes. So let's start with the core uh problem right. So as many of you uh might be aware we're in living in a day that we're using a lot of AI and LLMs and you know there's a big problem that is going on that um you know sometimes we intentionally or intentionally send PI data to LLMs and when this happens um there's no you know detection there's no masking there's no isolation or there's no edit trail. So the that that information just goes straight to to the LM and that can pose um a security risk. Um some examples uh for example uh we have a developer that is working on some uh customer complaint and accidentally um past that support case into the LLM and that social security number uh might run into the um you know the code generation uh to solve the bug and somehow it it makes through uh the GitHub um commit.

So obviously that's not something that that we we don't want. Um also uh we can have uh components that share credentials. So you're thinking about you know uh an LLM that is generating code but at the same time is sharing uh the same uh libraries as uh something that accesses like a database for example, you know. So you don't want that to you know be shared in the same running environment. Um so at this point like what you know what what is actually needed is not a library or a filter. Uh what we want is an architecture that can prevents us uh to keep that you know privacy um in in place. So uh Kubernetes uh what we're going to be showing today is a Kubernetes first architecture uh for privacy enforcement. Uh and we're going to be talking a lot um around too many components. Uh focus on Kubernetes. Uh we're going to be talking about compute scheduling uh some open source secure reasoning models and some framework for frameworks such as like NI NISAT OASP and myestro um all of this will be across 23 containers, eight pipelines.

uh we're going to be talking about observability and Prometheus uh audit tables and some um thread patterns. So uh on this slide on the left you can see one process um everything is imported together. Um sorry you okay sorry and on the right you're going to well so everything'
