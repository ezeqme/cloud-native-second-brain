---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Observability"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8Y/opentelemetry-opentelemetry-in-five-minutes-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry%3A+OpenTelemetry+in+Five+Minutes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OpenTelemetry: OpenTelemetry in Five Minutes | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8Y/opentelemetry-opentelemetry-in-five-minutes-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry%3A+OpenTelemetry+in+Five+Minutes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OpenTelemetry: OpenTelemetry in Five Minutes | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8Y/opentelemetry-opentelemetry-in-five-minutes-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry%3A+OpenTelemetry+in+Five+Minutes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l8xiNOCIdLY
- YouTube title: OpenTelemetry: OpenTelemetry in Five Minutes | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/opentelemetry-opentelemetry-in-five-minutes-project-lightning-talk/l8xiNOCIdLY.txt
- Transcript chars: 5573
- Keywords: source, instrumentation, neutral, metrics, pillars, export, observability, portable, actually, ubiquitous, implementation, configure, believe, opentelemetry, minutes, member, governance, committee

### Resumo baseado na transcript

hello Salt Lake City I got a few of you with that one um this is open Telemetry in five minutes approximately I'm Austin Parker director of Open Source at honeycomb.io and a member of the open Telemetry governance committee hello I'm Dan I'm a principal engineer at Skyscanner and also member of the governance committee so today we're going to tell you about open Telemetry who knows what open Telemetry is show a hands wow how many of you like open Telemetry all right you don't have to lie

### Excerpt da transcript

hello Salt Lake City I got a few of you with that one um this is open Telemetry in five minutes approximately I'm Austin Parker director of Open Source at honeycomb.io and a member of the open Telemetry governance committee hello I'm Dan I'm a principal engineer at Skyscanner and also member of the governance committee so today we're going to tell you about open Telemetry who knows what open Telemetry is show a hands wow how many of you like open Telemetry all right you don't have to lie um how many people find open Telemetry easy to use and understand all right so which is interesting right because on the website it says our mission is to enable effective observability by making high quality portable Telemetry ubiquia but what does that actually mean in practice what does open Telemetry mean to you there's a lot of different things that go into open telemetry you have the API you have semantic inventions you have profiling instrumentation packages tracing metrics logs OTP agents there's so many things it's hard to really say what is open Telemetry and how does it actually kind of fit together so what we want to do is we want to really narrow in on what does it mean to have high quality instrumentation anyway what is our goal um as a project so we have a vision right and that Vision says that Telemetry to be effective for observability needs to be sparse it needs to be highly dimensional everything in the system needs to participate in Telemetry generation that generated Telemetry needs to have a sufficient variety of Dimensions that can be adaptable to different use cases Telemetry is not three pillars or four pillars or five pillars or any number of discrete pillars Telemetry is one single interrelated braid of data that is self-referential and that means that the analysis that data cannot be isolated either it has to be part of this entire you know this one hole and it has to be meaningful data it has to have structure it has to have schema that can help you interpret and understand the meaning of the Telemetry and then um Telemetry also needs to be portable and ubiquitous and you probably know that open Telemetry is vendon neutral you can take your Telemetry and then integrate it with uh many open source backends open t also provides otop that protocol that efficiently um is able to encode and transport your Telemetry not to just open source backends but also to most observability vendors these days and that makes your Telemetry portable you basically
