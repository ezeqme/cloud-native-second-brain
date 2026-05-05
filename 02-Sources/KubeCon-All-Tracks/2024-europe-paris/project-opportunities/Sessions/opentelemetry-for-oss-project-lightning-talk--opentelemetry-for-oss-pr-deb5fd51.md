---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Observability"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQh4/opentelemetry-for-oss-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+for+OSS%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OpenTelemetry for OSS! | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQh4/opentelemetry-for-oss-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+for+OSS%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OpenTelemetry for OSS! | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQh4/opentelemetry-for-oss-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+for+OSS%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yjVCOhxJH-0
- YouTube title: OpenTelemetry for OSS! | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/opentelemetry-for-oss-project-lightning-talk/yjVCOhxJH-0.txt
- Transcript chars: 5510
- Keywords: library, software, instrumentation, libraries, observability, applications, production, realistic, experts, issues, provide, write, parameters, maintain, playbooks, common, questions, lightning

### Resumo baseado na transcript

Al righty alrighty hello everybody uh we are from the open Telemetry project and uh we're going to give a brief talk today about a lesser discussed form of observability which is observing open-source software specifically libraries my name is Ted Ted Su on the internet I'm one of the co-founders of open Telemetry and this is I'm tras stal naker a a software engineer of Microsoft and a maintainer of the open Telemetry Java instrumentation yes and instrumentation is what we want to talk about here so what is

### Excerpt da transcript

Al righty alrighty hello everybody uh we are from the open Telemetry project and uh we're going to give a brief talk today about a lesser discussed form of observability which is observing open-source software specifically libraries my name is Ted Ted Su on the internet I'm one of the co-founders of open Telemetry and this is I'm tras stal naker a a software engineer of Microsoft and a maintainer of the open Telemetry Java instrumentation yes and instrumentation is what we want to talk about here so what is the whole goal the goal is observing our applications right um we run applications we run services in production however these applications are built out of libraries it's third-party open-source software libraries that do most of the heavy lifting in our applications so when we say we want to observe our applications what we really mean is we want to observe our libraries however there's a problem which is most libraries don't provide any observ observability directly they don't have any instrumentation built into them uh instead what happens is people like tras here write their own instrumentation and then inject that instrumentation into the library through something like a Java agent so this does work this is the way we have been doing things since before time was time but this does create some problems which have only been getting worse uh with the recent acceleration of uh software development uh the first problem being there is too much software when instrumenting rails was enough to give you observability across like all of Ruby it was fine but now there's a new JavaScript framework uh getting minted every single week uh there is too much software in the world and so the idea that you can have a central repository maintained by a small group of people who are going to write and keep up todate all of the software instrumentation in the universe is not realistic it is not realistic to centralize this effort it's also not realistic that we the open Telemetry maintainers would be incredible experts at every single software Library out there that we need to provide instrumentation for if we happen to be users of a library that's great we might have some insight as to specifically what you would want out of that library but we're not going to be users of every piece of software that everyone else wants to use so it's just not realistic that we would would be the experts at individual libraries we're experts at observability but not at libraries who ar
