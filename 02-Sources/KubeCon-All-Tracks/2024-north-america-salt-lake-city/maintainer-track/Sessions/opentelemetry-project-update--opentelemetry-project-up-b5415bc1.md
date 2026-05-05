---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Alolita Sharma", "Apple", "Juraci Paixão Kröhling", "Grafana Labs", "Ted Young", "ServiceNow", "Morgan Mclean", "Splunk", "Daniel Dyla", "Dynatrace"]
sched_url: https://kccncna2024.sched.com/event/1hovy/opentelemetry-project-update-alolita-sharma-apple-juraci-paixao-krohling-grafana-labs-ted-young-servicenow-morgan-mclean-splunk-daniel-dyla-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Project+Update+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OpenTelemetry Project Update - Alolita Sharma, Apple; Juraci Paixão Kröhling, Grafana Labs; Ted Young, ServiceNow; Morgan Mclean, Splunk; Daniel Dyla, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Alolita Sharma, Apple, Juraci Paixão Kröhling, Grafana Labs, Ted Young, ServiceNow, Morgan Mclean, Splunk, Daniel Dyla, Dynatrace
- Schedule: https://kccncna2024.sched.com/event/1hovy/opentelemetry-project-update-alolita-sharma-apple-juraci-paixao-krohling-grafana-labs-ted-young-servicenow-morgan-mclean-splunk-daniel-dyla-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+Project+Update+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OpenTelemetry Project Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hovy/opentelemetry-project-update-alolita-sharma-apple-juraci-paixao-krohling-grafana-labs-ted-young-servicenow-morgan-mclean-splunk-daniel-dyla-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+Project+Update+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wQ3ntXP8SSw
- YouTube title: OpenTelemetry: Project Updates, Next Steps, and AMA
- Match score: 0.817
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/opentelemetry-project-update/wQ3ntXP8SSw.txt
- Transcript chars: 28485
- Keywords: semantic, stable, collector, conventions, client, metrics, questions, support, trace, components, working, important, logging, please, probably, context, instrumentation, signals

### Resumo baseado na transcript

hi everyone good morning it's nice to see a nice full room especially for open Telemetry so today's uh session on the project uh is to give you an update on the open Telemetry project uh what's happening on the project what's completed give you kind of an overview of some of the key areas that the project has been working towards and then open it up for for the um you know audience to have actually ask the maintainers and the uh active contributors to the project um questions check us out on GitHub our organization is open- Telemetry you can find us on uh YouTube we have a demo that you can download and install um we have a end user working group who runs a lot of feedback sessions and other things

### Excerpt da transcript

hi everyone good morning it's nice to see a nice full room especially for open Telemetry so today's uh session on the project uh is to give you an update on the open Telemetry project uh what's happening on the project what's completed give you kind of an overview of some of the key areas that the project has been working towards and then open it up for for the um you know audience to have actually ask the maintainers and the uh active contributors to the project um questions right so with that said uh I'm Alita Sharma I'm part of the open telet governance committee I've also been involved on the project working on metrics uh uh OTP to Prometheus interoperability and as well as recently been working on llm uh semantic conventions for um open Telemetry and the spec of course with that said um again I'd like to introduce the others who are on the uh the from the GC today so yeah good morning everyone uh I'm s Norman based out of Germany I work for Cisco at the open source program office there and I'm as well part of the governance committee I'm also one of the co- maintainers of the Open telary document mentation so if you have any questions about that you can send me an issue on GitHub and I can help you there and I give it over to trusk thanks hi I'm tras stellmaker I'm a software engineer at Microsoft and a maintainer of the open pimary Java instrumentation project good morning my name is Daniel Gomez Blanco I'm a principal engineer SK sky scanner and I was super happy to have been elected to be part of the governance committee as a end user and trying to break that gap between end users and maintainers and making sure that we adob open Telemetry scale good morning there's some seats available up front if people want them I'm Austin Parker uh director of Open Source at honeycomb.io I've been a contributor uh to open Telemetry since before it was open Telemetry um I was an open tracing maintainer shout out to all my open tracing heads out in the audience tough crowd all right uh I'm also thank you I'm uh from North America and I am a maintainer of the open tet demo um among other responsibilities in the project all right so with that said again I'll hand it over to our first presenter severon and then we'll take turns awesome okay so let me move this a little bit uh before we talk about us we want to talk about you so I'm curious who of you is a real end user of open Telemetry so using open tele R in their production in their operations oh yeah that's real
