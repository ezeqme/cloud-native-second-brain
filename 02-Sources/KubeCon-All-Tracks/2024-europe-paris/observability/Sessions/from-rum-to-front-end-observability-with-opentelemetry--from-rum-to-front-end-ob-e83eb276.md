---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Observability"
themes: ["Observability"]
speakers: ["Purvi Kanal", "Honeycomb"]
sched_url: https://kccnceu2024.sched.com/event/1YeOH/from-rum-to-front-end-observability-with-opentelemetry-purvi-kanal-honeycomb
youtube_search_url: https://www.youtube.com/results?search_query=From+RUM+to+Front-End+Observability+with+OpenTelemetry+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From RUM to Front-End Observability with OpenTelemetry - Purvi Kanal, Honeycomb

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: France / Paris
- Speakers: Purvi Kanal, Honeycomb
- Schedule: https://kccnceu2024.sched.com/event/1YeOH/from-rum-to-front-end-observability-with-opentelemetry-purvi-kanal-honeycomb
- Busca YouTube: https://www.youtube.com/results?search_query=From+RUM+to+Front-End+Observability+with+OpenTelemetry+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From RUM to Front-End Observability with OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOH/from-rum-to-front-end-observability-with-opentelemetry-purvi-kanal-honeycomb
- YouTube search: https://www.youtube.com/results?search_query=From+RUM+to+Front-End+Observability+with+OpenTelemetry+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l2_wsvv-Rhs
- YouTube title: From RUM to Front-End Observability with OpenTelemetry - Purvi Kanal, Honeycomb
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-rum-to-front-end-observability-with-opentelemetry/l2_wsvv-Rhs.txt
- Transcript chars: 33002
- Keywords: instrumentation, browser, document, little, important, loaded, front-end, pretty, information, backend, javascript, actually, resource, website, events, observability, instrumentations, whether

### Resumo baseado na transcript

um so when I got a talk accepted to cucon about the browser I was honestly pretty surprised and seeing a a a room full of of of folks excited to chat about the browser at cucon and cloudnativecon it's not something I expected so um I'm curious who here identifies as primarily a front-end developer working on browsers okay I see a few hands who is more like I'm a full stack Dev I work I work on everything okay lot more hands Sr Ops okay gotcha amazing well call and the rest of your distributed tracing um and this to me is is really really powerful because you never have to wonder is it my front end or is it something in my back end you can answer that question really really easily

### Excerpt da transcript

um so when I got a talk accepted to cucon about the browser I was honestly pretty surprised and seeing a a a room full of of of folks excited to chat about the browser at cucon and cloudnativecon it's not something I expected so um I'm curious who here identifies as primarily a front-end developer working on browsers okay I see a few hands who is more like I'm a full stack Dev I work I work on everything okay lot more hands Sr Ops okay gotcha amazing well I'm excited to talk to the browser talk about the browser to y'all today um my name is pvi canel I've worked with browsers for a large part of my career and I'm really interested in getting front-end observability to a higher standard especially for Ops folks and backend folks we're used to really good tooling um and I really want to see the the browser front-end World catch up to that I work at honeycomb and we're trying to solve this problem there I'm also an approver on the open Telemetry JS project with a special interest in web apis So today we're just going to be going through the current state of real user monitoring and general front-end monitoring tools um we'll talk about a quick introduction to open Telemetry and how it can also be a a browser monitoring tool we'll talk about the automatic instrumentation that comes out of the box with open Telemetry that requires no not a lot of configuration to get started and then we'll jump into how manual instrumentation can really supercharge your um your journey of front-end observability so let's jump into it there's a lot of tools out there today for around real user monitoring and general front-end monitoring tools but how did we get here there was a time where the web wasn't that complicated it was a time to just truly like have fun express yourself on your homepage and talk about your favorite bands or sign up for Neopets um which is you know a lot of where I spent my time on the earlier internet and it really wasn't that complicated it was a server served up some HTML um you know we barely used JavaScript unless you wanted to play an MP3 or or something similar even blinking and Marquee was like all built into to HTML so we didn't really have a lot of like complexity going on over time though using the web has become no longer optional especially since the pandemic more and more of our critical services are accessed online getting vaccine appointments government services and lots of other really really basic needs are accessed through online portal
