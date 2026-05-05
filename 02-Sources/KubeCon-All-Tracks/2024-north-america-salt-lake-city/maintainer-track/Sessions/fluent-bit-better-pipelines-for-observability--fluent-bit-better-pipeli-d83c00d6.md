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
speakers: ["Eduardo Silva", "Chronosphere"]
sched_url: https://kccncna2024.sched.com/event/1hoxB/fluent-bit-better-pipelines-for-observability-eduardo-silva-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Better+Pipelines+for+Observability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fluent Bit: Better Pipelines for Observability - Eduardo Silva, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Eduardo Silva, Chronosphere
- Schedule: https://kccncna2024.sched.com/event/1hoxB/fluent-bit-better-pipelines-for-observability-eduardo-silva-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Better+Pipelines+for+Observability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fluent Bit: Better Pipelines for Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxB/fluent-bit-better-pipelines-for-observability-eduardo-silva-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Better+Pipelines+for+Observability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XCaA6eXsztE
- YouTube title: Fluent Bit: Better Pipelines for Observability - Eduardo Silva, Chronosphere
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fluent-bit-better-pipelines-for-observability/XCaA6eXsztE.txt
- Transcript chars: 28136
- Keywords: fluent, profiles, logs, traces, called, schemas, content, information, filters, processor, running, plugin, course, important, support, format, processors, output

### Resumo baseado na transcript

I think that the title for this session is called better pipelines for observability and usually in every Cube con happens something really interesting and we have observability day which is our collocated event on the first day before cucon and we always get ton of feedback and we get a sense that ER hey maybe the title for the talk is might need to be adjusted of the content because the type of questions that we get from the audience attendees and users change over time okay so my two we Shi the new open Telemetry envelope for Matrix so imagine that you're receiving Matrix over stat Z over a UDP Port right you can convert that to open Telemetry without any problem and once you convert the data to Hotel you can H and we got a couple of them and I will try to go to the latest slides and then jump into the demo and the hands on demo okay we talk about processors and the new experimental features this is really I I know know performance every use case is different every every workload is different so run your own tooling with your own numbers and take your best decision what I'm going to show here is what we found in our case very simple bench Mark reading a huge

### Excerpt da transcript

I think that the title for this session is called better pipelines for observability and usually in every Cube con happens something really interesting and we have observability day which is our collocated event on the first day before cucon and we always get ton of feedback and we get a sense that ER hey maybe the title for the talk is might need to be adjusted of the content because the type of questions that we get from the audience attendees and users change over time okay so my name is Ardo Silva there you got my email you can contact me anytime and I would like to try to to help you out with many things around observability in general but specifically around locks metros and traces I have been in this space H for a while I would say almost 10 years uh have been part of the fluent D team I created fluent bed almost 10 years ago next year is 10 years and today I'm a software engineer at chronosphere and I have been with the cncf from the early Beginnings okay so from a landscape perspective and in observability you know that we have projects are are in in sandbox incubation and graduated fluent bet and fluent D are in graduation status together with pritus jger and of course kubernetes and when talking about the project it's always good to understand why it exists and what is the vision about it um fluent bit has been designed from 10 years ago with the same principles that drives the road map today which is let's have an agent that allow us to move data from point A to point B plus processing that is really high performance but also with low resource usage which is really important and actually we didn't took this kind of Mantra when we created the project at the beginning because we knew that kubernetes going to be the big thing because it was just lucky that we wanted to have something for embedded Linux and this is mandatory but somehow today we still uh in that scope H also it's really important that any Telemetry agent or any solution needs to be vendor neutral because in production you don't want to get to a phase where you get married with a technology and at some point you want to test it out other things and you feel block right that's is the whole concept of bendor neutrality and also it's really important that every piece of software that you deploy should be able to integrate or talk speak to others right and and that's bed and one of the main problems that we solve is like we are in a world world we have many sorts of data of information
