---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Vineeth Pothulapati", "Timescale Inc"]
sched_url: https://kccncna2022.sched.com/event/182Ib/tips-and-tricks-to-successfully-migrate-from-jaeger-to-opentelemetry-vineeth-pothulapati-timescale-inc
youtube_search_url: https://www.youtube.com/results?search_query=Tips+And+Tricks+To+Successfully+Migrate+From+Jaeger+To+OpenTelemetry+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tips And Tricks To Successfully Migrate From Jaeger To OpenTelemetry - Vineeth Pothulapati, Timescale Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Vineeth Pothulapati, Timescale Inc
- Schedule: https://kccncna2022.sched.com/event/182Ib/tips-and-tricks-to-successfully-migrate-from-jaeger-to-opentelemetry-vineeth-pothulapati-timescale-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Tips+And+Tricks+To+Successfully+Migrate+From+Jaeger+To+OpenTelemetry+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tips And Tricks To Successfully Migrate From Jaeger To OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ib/tips-and-tricks-to-successfully-migrate-from-jaeger-to-opentelemetry-vineeth-pothulapati-timescale-inc
- YouTube search: https://www.youtube.com/results?search_query=Tips+And+Tricks+To+Successfully+Migrate+From+Jaeger+To+OpenTelemetry+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6Vnuu2oVEMA
- YouTube title: Tips And Tricks To Successfully Migrate From Jaeger To OpenTelemetry - Vineeth Pothulapati
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tips-and-tricks-to-successfully-migrate-from-jaeger-to-opentelemetry/6Vnuu2oVEMA.txt
- Transcript chars: 25516
- Keywords: collector, instrumentation, traces, applications, application, client, context, publisher, migration, storage, basically, metrics, tracing, configure, formatter, propagation, instrumented, tracer

### Resumo baseado na transcript

hello everyone uh thanks for joining today's session and today's session is about tips and tricks to migrate from eager to open Telemetry so first things first how many of you are using eager already okay open Telemetry have you started using open telemetry nice okay then I think you will understand most of the eager parts and open Telemetry parts that I'll be discussing today so the agenda for today is prerequisites first setting the ground correct first like what are the expectations from the talk and other things

### Excerpt da transcript

hello everyone uh thanks for joining today's session and today's session is about tips and tricks to migrate from eager to open Telemetry so first things first how many of you are using eager already okay open Telemetry have you started using open telemetry nice okay then I think you will understand most of the eager parts and open Telemetry parts that I'll be discussing today so the agenda for today is prerequisites first setting the ground correct first like what are the expectations from the talk and other things and why we have to migrate and we will also go through a brief architectural overview of both eager and open Telemetry and we will be talking about levels of migration and I also have a demo on how we migrate an application and the last one is eager and open Telemetry boundaries so today everyone is a bit uh uh why are you didn't confuse that how how and where do I plug agar over open telemetry so about me my name is vinit potlapati I'm a product manager at timescale I work on the observability products at time scale primarily focused on Prom scale and tops I'm also a maintainer of open Telemetry operator so if you're already using an open Telemetry operator would love to hear out your experience and if you would like to check out the products that I work from skill and tops they are open source so the links are shared at the bottom uh it's time scale slash prom scale and time skill slash tops okay so the prerequisites so throughout the session I'll also be using Tom as Hotel so open Telemetry synonym or a short form is Hotel so the commonly used phrase so I'll be using that more often and the stock is focused on traces so open Telemetry is also getting into metrics logs and other things but we will be confined and focusing on traces the stock isn't intended to push the migration or I'm not selling anything here I'll just share what are the ways how you can mix and match the things and what are the upsides of migrating and let's understand the components first before we get into the talk so we know there are multiple components involved in tracing both in eager and open Telemetry so the instrumentation layer usually has API and SDK so in eager we use open tracing API and the SDK is eager client libraries and the agent and collector is uh all eager so eager also has an agent and collector and it also offers some native storage options within the collector uh like Cassandra elasticsearch and there is a grpc based uh mechanism to plug the external
