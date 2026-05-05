---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["GitOps Delivery", "Runtime Containers"]
speakers: ["Kevin Hoffman", "Cosmonic"]
sched_url: https://kccnceu2023.sched.com/event/1Hycy/distributed-event-sourcing-with-wasmcloud-kevin-hoffman-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Distributed+Event+Sourcing+with+WasmCloud+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Distributed Event Sourcing with WasmCloud - Kevin Hoffman, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[GitOps Delivery]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kevin Hoffman, Cosmonic
- Schedule: https://kccnceu2023.sched.com/event/1Hycy/distributed-event-sourcing-with-wasmcloud-kevin-hoffman-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Distributed+Event+Sourcing+with+WasmCloud+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Distributed Event Sourcing with WasmCloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hycy/distributed-event-sourcing-with-wasmcloud-kevin-hoffman-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Distributed+Event+Sourcing+with+WasmCloud+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=llIiUYocYcw
- YouTube title: Distributed Event Sourcing with WasmCloud - Kevin Hoffman, Cosmonic
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/distributed-event-sourcing-with-wasmcloud/llIiUYocYcw.txt
- Transcript chars: 21707
- Keywords: sourcing, webassembly, events, source, application, applications, actually, command, assembly, wasm, having, actors, aggregate, commands, wasmcloud, capability, server, number

### Resumo baseado na transcript

all right so a couple things before I get started first I just want to thank everybody for coming out um this is definitely the biggest uh crowd I've ever seen for a web assembly talk you are all here for web assembly right it's not you're okay just making sure you're not in the wrong room uh let's see second I apologize if the reflection off my head is uncomfortable for some of you the the lights here are pretty intense wasn't counting on that all right so uh

### Excerpt da transcript

all right so a couple things before I get started first I just want to thank everybody for coming out um this is definitely the biggest uh crowd I've ever seen for a web assembly talk you are all here for web assembly right it's not you're okay just making sure you're not in the wrong room uh let's see second I apologize if the reflection off my head is uncomfortable for some of you the the lights here are pretty intense wasn't counting on that all right so uh my name is Kevin Hoffman I'm the CTO and co-founder of cosmonic which is a webassembly Paz I created the web web assembly open source project called wasmcloud uh wrote a couple of books and I'm very easily nerd sniped all you have to do is say one or two distributed systems buzzwords and I'll wake up a week later with a thousand open browser tabs so my goal for this session is to hopefully make it so that you will want to leave and go and start playing with this stuff and explore it so that's that's the goal so basically going to go through some layers at the base layer I'm going to talk about what web assembly is so actually I need to pause before that uh I checked that you're all in the right room but how many of you have used webassembly that is insane okay how many of you are sick of hearing about webassembly a couple in the back I see you um so another goal is to hopefully try and convince you that all of the hype around webassembly isn't just hype and there's actually some meat on this so after I go through webassembly we'll talk about wasm Cloud that'll talk about how you can build all sorts of things on top of the wasm cloud and the thing that I'm going to talk about today is event sourcing uh and then hopefully I'll be able to get to the demos fairly quickly so we can get to QA um I can I'm going to skim through this fairly quickly uh webassembly is an open standard uh and the usual buzzwords are that it's safe and secure it's fast and efficient uh polyglot and portable wasmcloud is how many of you have heard of wasmcloud okay that's also insane great um cloud is an open source runtime that sits on top of webassembly and adds what amounts to you an orchestration layer in an application runtime it gives you secure access to capabilities and I'll talk about what capabilities are in a minute it's horizontally and vertically scalable but the thing that I think is most important about was and cloud is that it moves the decision about the size and shape of your application from design and compile
