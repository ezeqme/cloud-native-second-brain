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
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Friedrich Gonzalez", "Adobe", "Alan Protasio", "Amazon Web Services"]
sched_url: https://kccnceu2023.sched.com/event/1HyT9/cortex-how-to-run-a-rock-solid-multi-tenant-prometheus-friedrich-gonzalez-adobe-alan-protasio-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Cortex%3A+How+to+Run+a+Rock+Solid+Multi-Tenant+Prometheus+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cortex: How to Run a Rock Solid Multi-Tenant Prometheus - Friedrich Gonzalez, Adobe & Alan Protasio, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Friedrich Gonzalez, Adobe, Alan Protasio, Amazon Web Services
- Schedule: https://kccnceu2023.sched.com/event/1HyT9/cortex-how-to-run-a-rock-solid-multi-tenant-prometheus-friedrich-gonzalez-adobe-alan-protasio-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Cortex%3A+How+to+Run+a+Rock+Solid+Multi-Tenant+Prometheus+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cortex: How to Run a Rock Solid Multi-Tenant Prometheus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyT9/cortex-how-to-run-a-rock-solid-multi-tenant-prometheus-friedrich-gonzalez-adobe-alan-protasio-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Cortex%3A+How+to+Run+a+Rock+Solid+Multi-Tenant+Prometheus+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Pl5hEoRPLJU
- YouTube title: Cortex: How to Run a Rock Solid Multi-Tenant Prometheus - Friedrich Gonzalez, Adobe & Alan Protasio
- Match score: 0.815
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cortex-how-to-run-a-rock-solid-multi-tenant-prometheus/Pl5hEoRPLJU.txt
- Transcript chars: 27074
- Keywords: cortex, prometheus, instance, thanos, another, sharding, engine, limits, series, questions, question, multiple, important, problems, tenant, features, tenants, everything

### Resumo baseado na transcript

okay hi hi everyone um okay we still have one more minute uh but maybe I can ask a question who's here for cortex to and just to make sure everybody's in the right building okay good um who's here um to see AI generated pictures of puppies ah nobody oh right cool okay good so we I guess we have to do both um we have to do cortex and AI generated pictures of puppies um yeah okay we're gonna talk um on cortex and how to run a

### Excerpt da transcript

okay hi hi everyone um okay we still have one more minute uh but maybe I can ask a question who's here for cortex to and just to make sure everybody's in the right building okay good um who's here um to see AI generated pictures of puppies ah nobody oh right cool okay good so we I guess we have to do both um we have to do cortex and AI generated pictures of puppies um yeah okay we're gonna talk um on cortex and how to run a rock solid multi-tenant Prometheus um and how do we do how do we do that with cortex right on the agenda um we're gonna do we're gonna do a bit of introduction on cortex for those that are not familiar very quick then we're going to talk about what is latest on cortex uh we just released something and then we're going to go in some of it of drillability in cortex and having users in mind you're gonna see what that is about and then we're going to see a specific on cortex what is the secret sauce of Cortex um we're gonna get that and then then we're going to talk what's coming up for cortex in in the pipeline and then we're going to do some questions right um cortex is a horizontally scalable highly available long-term storage for Prometheus um it's a cncf project it's an integrating project is not a new project it started 2016.

um it had since a lot of contributors over the years lots of maintainers um uh if we even change at some point The Backs back in storage but we're going to talk a bit on what's like last year a bit um so my name is fedris Gonzalez I'm a software engineer at Adobe in here with me is um hey uh I'm Alan I'm also a software engineer on AWS yeah so and then we also have some other members of the team that we surely value Alvin a software development manager who's also a maintainer and we also have Ben from Amazon as well um also we have maintainers on the health chart we also want to mention they do a great work on the home chart these are the faces sorry Nicholas I didn't get your picture for the talk but yeah you do good work and these are the people have been working uh a lot on cortex lately um some of the key contributes that we have in cortex are on this slide um yeah if you it might be that you made some comic on cortex you're not in this ladder probably this is like if you more make more than one comment your show um so sorry um but we want to thank them all because these are the people that we're gonna talk about when we talk about all these features that we're going to do the talk right so but why is cortex
