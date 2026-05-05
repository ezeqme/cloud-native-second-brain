---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: []
sched_url: https://kccnceu2023.sched.com/event/1HyU7/kyverno-introduction-and-deep-dive-charles-edouard-breteche-nirmata-jinhong-brejnholt-saxo-bank
youtube_search_url: https://www.youtube.com/results?search_query=Kyverno%C2%A0Introduction%C2%A0and%C2%A0Deep%C2%A0Dive%C2%A0-%C2%A0Charles-Edouard%C2%A0Br%C3%A9t%C3%A9ch%C3%A9%2C%C2%A0Nirmata%C2%A0%26%C2%A0Jinhong%C2%A0Brejnholt%2C%C2%A0Saxo+Bank+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kyverno Introduction and Deep Dive - Charles-Edouard Brétéché, Nirmata & Jinhong Brejnholt, Saxo Bank

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: N/A
- Schedule: https://kccnceu2023.sched.com/event/1HyU7/kyverno-introduction-and-deep-dive-charles-edouard-breteche-nirmata-jinhong-brejnholt-saxo-bank
- Busca YouTube: https://www.youtube.com/results?search_query=Kyverno%C2%A0Introduction%C2%A0and%C2%A0Deep%C2%A0Dive%C2%A0-%C2%A0Charles-Edouard%C2%A0Br%C3%A9t%C3%A9ch%C3%A9%2C%C2%A0Nirmata%C2%A0%26%C2%A0Jinhong%C2%A0Brejnholt%2C%C2%A0Saxo+Bank+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kyverno Introduction and Deep Dive - Charles-Edouard Brétéché, Nirmata & Jinhong Brejnholt, Saxo Bank.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyU7/kyverno-introduction-and-deep-dive-charles-edouard-breteche-nirmata-jinhong-brejnholt-saxo-bank
- YouTube search: https://www.youtube.com/results?search_query=Kyverno%C2%A0Introduction%C2%A0and%C2%A0Deep%C2%A0Dive%C2%A0-%C2%A0Charles-Edouard%C2%A0Br%C3%A9t%C3%A9ch%C3%A9%2C%C2%A0Nirmata%C2%A0%26%C2%A0Jinhong%C2%A0Brejnholt%2C%C2%A0Saxo+Bank+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Es_JgpR0wbg
- YouTube title: Kyverno Introduction and Deep Dive - Charles-Edouard Brétéché, Nirmata & Jinhong Brejnholt
- Match score: 1.024
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kyverno-introduction-and-deep-dive-charles-edouard-br-t-ch-nirmata-jin/Es_JgpR0wbg.txt
- Transcript chars: 22756
- Keywords: policy, kivano, cluster, policies, resource, admission, signature, kimono, validate, create, engine, resources, cosine, created, security, verification, validating, support

### Resumo baseado na transcript

hello everyone Welcome to our section yeah welcome thank you so welcome everyone um session for today is called kivano and production and deep dive uh we will be two co-presenters on stage today so please let us introduce ourselves briefly and we can look at the session agenda and start the talk so my name is Charlize I've been a kivano maintainer for one year and a half now I recently joined yamata the company that created and open source kivano so since then working on kivano has been

### Excerpt da transcript

hello everyone Welcome to our section yeah welcome thank you so welcome everyone um session for today is called kivano and production and deep dive uh we will be two co-presenters on stage today so please let us introduce ourselves briefly and we can look at the session agenda and start the talk so my name is Charlize I've been a kivano maintainer for one year and a half now I recently joined yamata the company that created and open source kivano so since then working on kivano has been my full-time job and you can contact me on Gita about or LinkedIn and the edit Charlie nickname it's a little bit inconvenient apology for that we will get more we can go more fluent afterwards my name is I'm the chief Club architect and product owner from saxo bank I'm also one of the organizers from cloud native Copenhagen meetup group so if you have a good talks please contact me in linding and that's also my Handler for for GitHub for today's section we have packed agenda for you so in the beginning share Edward will give you guys a great intro on kimono where it is and what can you use it for afterwards I will talk about the use case we have for sexual bank and the vlogs and we end up with a child while to bring you guys to some Advanced features gonna come in the coming weeks thanks General so we're going to start with a kivano introduction but first I'd like to Recall why we need a policy engine so why do we need a policy engine fortunately there are a lot of good answers to that question so the first good entry should be for security reasons and to ensure that for example containers don't run as roots in a cluster to prevent improperly signed container images or things like this another good reason would be to enable collaboration and Military tenancy inside the cluster and I think General will talk about that in more details later or it could be used to implement a sort of cost control system to prevent every service to allocate a new load balancer or things like this or to validate for CPU and memory request or these kind of things and it probably can be used for plenty of other things too just because every company will want to validate and enforce different things so policy engine quickly becomes necessary at this point and it's exactly what kirano is and does so kivano is an open source kubernetes native policy engine it allows you to create validate and enforce policies for requester the advantage of kivano is that it doesn't require any specific programming l
