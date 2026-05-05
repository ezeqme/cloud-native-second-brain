---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["AI ML", "Observability", "GitOps Delivery"]
speakers: ["Juraci Paixão Kröhling", "OllyGarden", "Elena Kovalenko", "Delivery Hero"]
sched_url: https://kccnceu2026.sched.com/event/2CW6M/day-2-reality-check-taming-wasteful-telemetry-juraci-paixao-krohling-ollygarden-elena-kovalenko-delivery-hero
youtube_search_url: https://www.youtube.com/results?search_query=Day-2+Reality+Check%3A+Taming+Wasteful+Telemetry+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Day-2 Reality Check: Taming Wasteful Telemetry - Juraci Paixão Kröhling, OllyGarden & Elena Kovalenko, Delivery Hero

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Juraci Paixão Kröhling, OllyGarden, Elena Kovalenko, Delivery Hero
- Schedule: https://kccnceu2026.sched.com/event/2CW6M/day-2-reality-check-taming-wasteful-telemetry-juraci-paixao-krohling-ollygarden-elena-kovalenko-delivery-hero
- Busca YouTube: https://www.youtube.com/results?search_query=Day-2+Reality+Check%3A+Taming+Wasteful+Telemetry+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Day-2 Reality Check: Taming Wasteful Telemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6M/day-2-reality-check-taming-wasteful-telemetry-juraci-paixao-krohling-ollygarden-elena-kovalenko-delivery-hero
- YouTube search: https://www.youtube.com/results?search_query=Day-2+Reality+Check%3A+Taming+Wasteful+Telemetry+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cpB5NTtUdwQ
- YouTube title: Day-2 Reality Check: Taming Wasteful Telemetry - Juraci Paixão Kröhling & Elena Kovalenko
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/day-2-reality-check-taming-wasteful-telemetry/cpB5NTtUdwQ.txt
- Transcript chars: 26994
- Keywords: instrumentation, application, attributes, logs, vendor, information, observability, course, wasteful, create, better, instance, frequently, sometimes, attribute, collector, interesting, applications

### Resumo baseado na transcript

I'm very glad and very proud that you are here uh that you survived uh 2 and a half days or almost 3 days. Um and I I promise that we will keep it uh interesting and relatively short I suppose. It's convenient to use auto instrumentation and this is something that many people defer to uh uh at day one or uh day zero but then afterwards it creates a problem on its own. The decisions about things like observability are frequently being made uh locally and this creates a problem of telemetry governance where uh every part of the company uh writes telemetry that does not um have a common schema and this uh creates then problems uh We have this philosophy a few years ago as well within open tracing even. A lot of that telemetry is not very useful and uh but when we try to fix that problem or whenever we we think about removing the that the user instrumentation that user telemetry that we have we end up thinking h what if I

### Excerpt da transcript

Hello everyone. That's long. Um hello everyone and welcome to the very last session of CubeCon. I'm very glad and very proud that you are here uh that you survived uh 2 and a half days or almost 3 days. It's been a long week. Um and I I promise that we will keep it uh interesting and relatively short I suppose. Uh but we have time. Yeah. Let's see. Let's see how it goes. So welcome today to reality tech uh taming wasteful telemetry. Yeah. Hi everyone. Uh my name is Edina. I'm principal engineer from delivery hero and uh I have been taming wasteful telemetry for the past uh 5 years at least. >> Yeah. And my name is Jasi Pashan Kurving. I'm a software engineer and co-founder at creating that planetary for so many years now. >> Shame. Shame. >> Yeah. Sorry. >> So uh let me guide you through the agenda that we have prepared for you today. First we are going to look at the social and environmental factors that make us create bad telemetry at day zero at day one. And also we're going to have a look at the exact examples of this bad telemetry.

And then in the very last step we're going to provide a set of simple solutions that everyone can implement and make your telemetry a little bit better. Let's go. >> Right. So let's get started with the roots of all evil. So when I develop my first applications or when I start developing applications even today I I try to make it work first right so I do the my software I get it working I deploy that software and then I hope that everything works eventually things don't actually work so I need to understand what's going on uh and the way that we can do things nowadays at least I mean back then I would open the application add some logging to that and watch what's going on but nowadays what we would do is whenever we need to observe Oberve what our application is doing. We would um perhaps get some vendor to help us there. Do a PC and perhaps start doing some instrumentation in our applications. Um so u imagine a situation that you are at a loud party or actually don't imagine anything. just remember how you were sitting at CubeCon this time and were listening to a keynote in this large auditorium and then suddenly um you start hearing the thoughts of everybody else around you and in the beginning it is exciting it is interesting you're overwhelmed and you're thinking oh maybe I can listen to something interesting from a person I consider interesting but then there is so much noise and there are so many other thoughts and t
