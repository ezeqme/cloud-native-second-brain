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
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Ted Young", "Lightstep", "Ludmila Molkova", "Microsoft"]
sched_url: https://kccncna2021.sched.com/event/lV8I/native-instrumentation-for-open-source-software-with-opentelemetry-ted-young-lightstep-ludmila-molkova-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Native+Instrumentation+for+Open+Source+Software+with+OpenTelemetry+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Native Instrumentation for Open Source Software with OpenTelemetry - Ted Young, Lightstep & Ludmila Molkova, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Ted Young, Lightstep, Ludmila Molkova, Microsoft
- Schedule: https://kccncna2021.sched.com/event/lV8I/native-instrumentation-for-open-source-software-with-opentelemetry-ted-young-lightstep-ludmila-molkova-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Native+Instrumentation+for+Open+Source+Software+with+OpenTelemetry+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Native Instrumentation for Open Source Software with OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8I/native-instrumentation-for-open-source-software-with-opentelemetry-ted-young-lightstep-ludmila-molkova-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Native+Instrumentation+for+Open+Source+Software+with+OpenTelemetry+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6UqCo32vdeI
- YouTube title: Native Instrumentation for Open Source Software with OpenTelemetry - Ted Young & Ludmila Molkova
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/native-instrumentation-for-open-source-software-with-opentelemetry/6UqCo32vdeI.txt
- Transcript chars: 17370
- Keywords: library, context, instrumentation, application, libraries, dependencies, observability, create, stable, logs, semantic, implicit, source, usually, dependency, tracing, solution, conflict

### Resumo baseado na transcript

so let me introduce myself i'm ludmila i work for microsoft i work on azure sdks and observability uh later on i will tell you about our experience with instrumentation with open telemetry uh the ups and downs of it um and share some practical information and yeah yeah great hi and i'm ted uh one of the co-founders of the open telemetry project and uh i work at lightstep maybe we should do that yes alrighty so yeah let's get started uh so normally when i give talks about

### Excerpt da transcript

so let me introduce myself i'm ludmila i work for microsoft i work on azure sdks and observability uh later on i will tell you about our experience with instrumentation with open telemetry uh the ups and downs of it um and share some practical information and yeah yeah great hi and i'm ted uh one of the co-founders of the open telemetry project and uh i work at lightstep maybe we should do that yes alrighty so yeah let's get started uh so normally when i give talks about how open telemetry provides value usually uh it's some slides like this talking about tracing metrics logs how they're all braided together and how that uh brings a lot of value but that's not what we're going to talk about today today instead i want to focus on this other problem which is that instrumenting open source software sucks like let's say your library wants to log into error sounds like it would be so easy but it's this surprisingly difficult journey you don't know what the application owner picked but the only option you have to pick generally is standard out and that's probably not right especially for their metrics so what do you do right the real problem is that your library needs to support many applications and so when it comes to picking a solution uh you have to defer to the application itself the application owner is the person who picks where the data went and there's no one right answer for that so since all of the data needs to go to the same place each individual library can't pick a solution for instrumentation and observability because the instrumentation is usually tied to a particular data system so you instrument with a particular library and that tends to pick a particular format sends the data to a particular place and every library can't pick a different solution there so life is terrible uh but that's not the only problem the other problem is that open source libraries have to compose well with other libraries which means they have to be very picky about their dependencies right libraries don't get to synchronize with each other so the dependencies that one library takes on might conflict with the dependencies that another library takes on and those dependencies might have dependencies with which conflict with each other so since instrumentation is always going to be out of date somewhere uh version sku can be a big poisonous effort here plus any other dependencies that you might have uh if you're hauling in say like a big implementation when you haul in th
