---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Morgan McLean", "Splunk", "Daniel Dyla", "Dynatrace", "Ted Young", "Lightstep", "Alolita Sharma", "Apple"]
sched_url: https://kccncna2022.sched.com/event/182On/opentelemetry-meet-the-community-build-the-roadmap-morgan-mclean-splunk-daniel-dyla-dynatrace-ted-young-lightstep-alolita-sharma-apple
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry%3A+Meet+the+Community%2C+Build+the+Roadmap+CNCF+KubeCon+2022
slides: []
status: parsed
---

# OpenTelemetry: Meet the Community, Build the Roadmap - Morgan McLean, Splunk; Daniel Dyla, Dynatrace; Ted Young, Lightstep; Alolita Sharma, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Morgan McLean, Splunk, Daniel Dyla, Dynatrace, Ted Young, Lightstep, Alolita Sharma, Apple
- Schedule: https://kccncna2022.sched.com/event/182On/opentelemetry-meet-the-community-build-the-roadmap-morgan-mclean-splunk-daniel-dyla-dynatrace-ted-young-lightstep-alolita-sharma-apple
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry%3A+Meet+the+Community%2C+Build+the+Roadmap+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre OpenTelemetry: Meet the Community, Build the Roadmap.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182On/opentelemetry-meet-the-community-build-the-roadmap-morgan-mclean-splunk-daniel-dyla-dynatrace-ted-young-lightstep-alolita-sharma-apple
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry%3A+Meet+the+Community%2C+Build+the+Roadmap+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7mYNLafiaOk
- YouTube title: OpenTelemetry: Meet the Community, Build the Roadmap - Morgan, Daniel, Ted, Alolita
- Match score: 0.874
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/opentelemetry-meet-the-community-build-the-roadmap/7mYNLafiaOk.txt
- Transcript chars: 37926
- Keywords: actually, metrics, working, observability, client, already, languages, roadmap, tracing, collector, instrumentation, across, wanted, started, infrastructure, logs, components, storage

### Resumo baseado na transcript

okay good evening everyone welcome to the last session of the day before we go on to the cncf event party I'm alelita Sharma and I would like to introduce fellow members of the GC as well as maintainers on the open Telemetry project um Ted would you like to go first sure my name's Ted Young I work at lightstep but I'm a open Telemetry Governors committee murder and one of the co-founders my name is Morgan McLean I'm also one of the co-founders of open Telemetry also in

### Excerpt da transcript

okay good evening everyone welcome to the last session of the day before we go on to the cncf event party I'm alelita Sharma and I would like to introduce fellow members of the GC as well as maintainers on the open Telemetry project um Ted would you like to go first sure my name's Ted Young I work at lightstep but I'm a open Telemetry Governors committee murder and one of the co-founders my name is Morgan McLean I'm also one of the co-founders of open Telemetry also in the governor's committee I'm a director of PMS Splunk my name is Dan Dila I work at dynatrace I am a maintainer of the open telemetry.js client and on the governance committee cool and again just complete my introduction [Music] on member of the open Telemetry governance committee have been contributing to the project for multiple years now and I also Lead Series observability at Apple so um super happy to be here today all right so with that said again I wanted to kind of run through what we have accomplished on the project in the last year we gave an update at Valencia earlier this year uh in the spring and as many of you who may have attended that session or not we in last year started working on logging which was a big you know pillar for the project as well as going Beyond traces and Metric support we also last year you know kicked off the Prometheus open metrics Hotel interrupt group where we actually worked through making sure that the otlp protocol was fully compatible with open metrics as a metric standard as well as Prometheus which also uses open metrics as the Baseline and we've made good progress there tracing was also G8 last year in October and again you know that was functionality that we had inherited from open tracing and open census but then we also actually did a fundamental amount of work on open tracing uh on tracing itself in order to not only Harden The Collector but also complete the implementation in the apis and sdks we also started working on Telemetry schemas specifically the open Telemetry specification as many of you who may be using open Telemetry or have looked at the project the specification again provides a requirement spec for the project to implement both on the collector agent as well as the 11 language apis and sdks that exist on the project for instrumentation of your applications and then going on from there we also start ensured stability of the logs data model which was also announced at the Valencia kubecon conference earlier this spring going for
