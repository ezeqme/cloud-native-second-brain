---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Juraci Paixão Kröhling", "OllyGarden", "Michele Mancioppi", "Dash0"]
sched_url: https://kccncna2025.sched.com/event/27FWx/instrumentation-score-the-difference-between-telemetry-and-good-telemetry-juraci-paixao-krohling-ollygarden-michele-mancioppi-dash0
youtube_search_url: https://www.youtube.com/results?search_query=Instrumentation+Score%3A+The+Difference+Between+Telemetry+and+Good+Telemetry+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Instrumentation Score: The Difference Between Telemetry and Good Telemetry - Juraci Paixão Kröhling, OllyGarden & Michele Mancioppi, Dash0

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Juraci Paixão Kröhling, OllyGarden, Michele Mancioppi, Dash0
- Schedule: https://kccncna2025.sched.com/event/27FWx/instrumentation-score-the-difference-between-telemetry-and-good-telemetry-juraci-paixao-krohling-ollygarden-michele-mancioppi-dash0
- Busca YouTube: https://www.youtube.com/results?search_query=Instrumentation+Score%3A+The+Difference+Between+Telemetry+and+Good+Telemetry+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Instrumentation Score: The Difference Between Telemetry and Good Telemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWx/instrumentation-score-the-difference-between-telemetry-and-good-telemetry-juraci-paixao-krohling-ollygarden-michele-mancioppi-dash0
- YouTube search: https://www.youtube.com/results?search_query=Instrumentation+Score%3A+The+Difference+Between+Telemetry+and+Good+Telemetry+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kdzeUiMI_t4
- YouTube title: Instrumentation Score: The Difference Between Telemetr... Juraci Paixão Kröhling & Michele Mancioppi
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/instrumentation-score-the-difference-between-telemetry-and-good-teleme/kdzeUiMI_t4.txt
- Transcript chars: 32648
- Keywords: instrumentation, actually, semantic, logs, conventions, laughter, observability, important, perhaps, instance, having, number, course, talking, reality, applications, points, attributes

### Resumo baseado na transcript

Um my name is Judas and Mikuel we are going to introduce you today uh to the instrumentation score. So if you are in Berlin in a couple weeks time you're all invited to hotel night. true like that >> credit card numbers always a hit >> yeah uh but I think the biggest problem is really uh the amount of data like up to 90% of the telemetry is just junk and this is not a madeup number this is And uh let's say that for example, you want to have an overview of uh the performance of your HTTP API in serving requests. There are people that are not listening because literally every one of you is using logs at one point or another. In your heart of hearts in the middle of the night, can you tell in conscience that you're you're emitting debug logs only when you're debugging?

### Excerpt da transcript

Hello everyone. Um my name is Judas and Mikuel we are going to introduce you today uh to the instrumentation score. >> I am Mikuel uh head of product at Dura. I am an open telemetry maintainer for the auto injector. >> And my name is Julie. I'm a software engineer at Olig Garden. Um I'm member of the governance committee for open telemetry. I help organize or I organize the hotel night in Berlin. So if you are in Berlin in a couple weeks time you're all invited to hotel night. Um and uh on my free time I like to create content around observability or focus on open telemetry under the brand telemetry drops and you can find it on linkin and YouTube. And for the next 30 minutes or so we're going to talk about um telemetry bet telemetry. So we had a session yesterday focused on what is bad telemetry. Uh and today we're going to focus more on instrumentation score. So what is instrumentation score? We're going to give you a spec overview. Um what are how are the rules structured uh and uh some examples of those rules and we should be having a few minutes towards the end for Q&A.

>> So um raise your hands please for me if you have software running in production right now. [laughter] Keep your hands up if you care about the software. >> Oh yeah. >> Oh you don't. Okay. So, do you have a clean conscience about your observability? Do you know what's going on that sir putting your hands down there? I appreciate your cander. So, when I actually go and uh uh try to explain people what I do for a living uh usually documents say observe what and uh for the purpose of this talk we are going to use a pretty commonplace definition of observability. Meaning a system is observable if you can figure out what the hell it is doing and why it is doing stuff that it should not be doing. And the way that people actually go about observability is uh to collect data called telemetry so that you can figure out what's going on. And there are several ways of collecting telemetry. Uh both and I are very much in open telemetry. So we're going to talk mostly about that. Uh technically it's you can monitor things on top only with open telemetry.

There are other projects. The way that you do it in open telemetry is usually a combination of different instrumentations. For example, you may use the open telemetry Java agent and add it to your Java application. All of a sudden you have a whole bunch of spans and logs and metrics. Or you may go and code in your application against the open tele
