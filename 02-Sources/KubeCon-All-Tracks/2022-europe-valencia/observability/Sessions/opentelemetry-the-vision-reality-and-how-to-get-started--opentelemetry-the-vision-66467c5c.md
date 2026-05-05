---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Dotan Horovits", "Logz.io"]
sched_url: https://kccnceu2022.sched.com/event/ytob/opentelemetry-the-vision-reality-and-how-to-get-started-dotan-horovits-logzio
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Vision%2C+Reality%2C+and+How+to+Get+Started+CNCF+KubeCon+2022
slides: []
status: parsed
---

# OpenTelemetry: The Vision, Reality, and How to Get Started - Dotan Horovits, Logz.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Dotan Horovits, Logz.io
- Schedule: https://kccnceu2022.sched.com/event/ytob/opentelemetry-the-vision-reality-and-how-to-get-started-dotan-horovits-logzio
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Vision%2C+Reality%2C+and+How+to+Get+Started+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre OpenTelemetry: The Vision, Reality, and How to Get Started.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytob/opentelemetry-the-vision-reality-and-how-to-get-started-dotan-horovits-logzio
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Vision%2C+Reality%2C+and+How+to+Get+Started+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qE1ggEmvz2Y
- YouTube title: OpenTelemetry: The Vision, Reality, and How to Get Started - Dotan Horovits, Logz.io
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/opentelemetry-the-vision-reality-and-how-to-get-started/qE1ggEmvz2Y.txt
- Transcript chars: 27518
- Keywords: collector, logs, metrics, traces, prometheus, important, observability, components, across, protocol, instrumentation, essentially, specification, actually, around, collect, logging, platform

### Resumo baseado na transcript

hello everyone glad to be here and uh amazing to see a full house there are a few uh seats in the at the front so if you can get some more people uh there are definitely more seats but amazing to see everyone here and a full house uh shame we can't see the people there on the virtual platform and really excited to be here at kubecon and today i'd like to talk to you about open telemetry a project that i'm very passionate about the vision the

### Excerpt da transcript

hello everyone glad to be here and uh amazing to see a full house there are a few uh seats in the at the front so if you can get some more people uh there are definitely more seats but amazing to see everyone here and a full house uh shame we can't see the people there on the virtual platform and really excited to be here at kubecon and today i'd like to talk to you about open telemetry a project that i'm very passionate about the vision the reality and how to get started with it let's start with a question how many tools does a company use on average to collect telemetry data from its systems many think about logs metrics traces think about your front-end app your back end up your infrastructure everything how many tools any other guesses well recent surveys show that companies use on average between 5 to 10 different tools to collect telemetry data from its from the systems five to ten you can reduce it to one unified standard platform that's the story of open telemetry i'm dutan horvitz i'm the principal developer advocate at logs.io at logsio we provide essentially cloud native observability platform that's based on popular open source tools such as prometheus and jaeger and obviously open telemetry and other projects i'm an advocate of open source and communities in general and the cncf in particular that's why it's very exciting to be here on the kubecon stage i co-organized the local cncf chapter in tel aviv i uh organize devops days i have a podcast open observability talks on open source devops and observability so if your podcast fans do check it out and in general you can find me everywhere at horvitz and let's talk about observability as you all know observability is essentially the ability to understand the state of our system based on the telemetry data that it emits and the vision talks about unified observability across different signal types classically the three pillars logs metrics and traces but also across different sources so again think about your front-end code your back-end code your kafka red these other open source projects cloud services essentially just fusing all of these together to gain insights and observability into your system that's the vision the reality however is much more fragmented and the reason is exactly what we asked at the beginning the reason is that we use so many different tools for our observability and each tool and each vendor has its own api and sdk for instrumenting different programming languages and t
