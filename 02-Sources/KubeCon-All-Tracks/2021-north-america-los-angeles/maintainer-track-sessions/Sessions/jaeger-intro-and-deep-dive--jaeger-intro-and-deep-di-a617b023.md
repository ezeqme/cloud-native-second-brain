---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Jonah Kowall", "Logz.io"]
sched_url: https://kccncna2021.sched.com/event/lV9k/jaeger-intro-and-deep-dive-jonah-kowall-logzio
youtube_search_url: https://www.youtube.com/results?search_query=Jaeger%3A+Intro+and+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Jaeger: Intro and Deep Dive - Jonah Kowall, Logz.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Jonah Kowall, Logz.io
- Schedule: https://kccncna2021.sched.com/event/lV9k/jaeger-intro-and-deep-dive-jonah-kowall-logzio
- Busca YouTube: https://www.youtube.com/results?search_query=Jaeger%3A+Intro+and+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Jaeger: Intro and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9k/jaeger-intro-and-deep-dive-jonah-kowall-logzio
- YouTube search: https://www.youtube.com/results?search_query=Jaeger%3A+Intro+and+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Wyrcik2XbgE
- YouTube title: Jaeger: Intro and Deep Dive - Jonah Kowall, Logz.io
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/jaeger-intro-and-deep-dive/Wyrcik2XbgE.txt
- Transcript chars: 32142
- Keywords: jaeger, operator, sampling, metrics, collector, basically, actually, trace, running, traces, prometheus, definitely, essentially, create, deploy, search, support, together

### Resumo baseado na transcript

thank you everyone for coming in person and this is cool to see everyone together a lot of the talks and the observability track have been virtual unfortunately i hope it changes but i'm glad to get everyone together and and showing up and meeting and talking uh today i'm actually the title's a little misleading but this talk is going to be about jager and we're going to dig into the jaeger operator which is a really cool piece of technology that's part of the project and then we're

### Excerpt da transcript

thank you everyone for coming in person and this is cool to see everyone together a lot of the talks and the observability track have been virtual unfortunately i hope it changes but i'm glad to get everyone together and and showing up and meeting and talking uh today i'm actually the title's a little misleading but this talk is going to be about jager and we're going to dig into the jaeger operator which is a really cool piece of technology that's part of the project and then we're going to talk about some of the metrics work that's been going on in yeager uh the first part of the talk about the operator uh joe elliott actually put the slides together and he was unable to make it last minute he's one of the maintainers as well he's over at grafana labs and he's the person responsible for tempo for those of you that are maybe using that he's a great engineer sorry he's not with us today my name is jonah cowell i'm the cto at logs i o i do a lot of work on jaeger open telemetry and open search which is the new open source fork of elasticsearch um and i'm happy to be here when i'm not working at the computer or maybe playing a little video games i spend a lot of time underwater uh it's been nice and covered because you're very isolated that way so i do a lot of diving that's my passion for the last several years and explore a lot of cool places where i live in south florida and all over the world so if you want to talk diving that's definitely another thing besides observability that i like to talk about and my company is a sas observability company there are many out there i can see many of you representing other ones we focus on an open source based platform and jager is part of our platform uh so it's the same ui the same usability with a bunch of other stuff around it um and jager is a is a great cncf project it's been graduated for quite some time uh for those of you that are not familiar with jaeger it's and you're maybe using open telemetry or looking at it the collector component of jager was actually forked to create the open telemetry collector and we're starting to bring some of that back into jaeger and we're essentially going to just be consuming upstream collector and that's the plan so jaeger is basically a storage format and a ui and a bunch of other pieces around it in order to scale it out but in general we build things in a very different way they're very componentized it's designed to run on kubernetes and this is something that uber crea
