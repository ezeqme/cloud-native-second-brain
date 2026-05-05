---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability"]
speakers: ["Jamie Danielson", "Honeycomb.io"]
sched_url: https://kccncna2023.sched.com/event/1R2oA/build-in-observability-while-developing-jamie-danielson-honeycombio
youtube_search_url: https://www.youtube.com/results?search_query=Build+in+Observability+While+Developing+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Build in Observability While Developing - Jamie Danielson, Honeycomb.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Jamie Danielson, Honeycomb.io
- Schedule: https://kccncna2023.sched.com/event/1R2oA/build-in-observability-while-developing-jamie-danielson-honeycombio
- Busca YouTube: https://www.youtube.com/results?search_query=Build+in+Observability+While+Developing+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Build in Observability While Developing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oA/build-in-observability-while-developing-jamie-danielson-honeycombio
- YouTube search: https://www.youtube.com/results?search_query=Build+in+Observability+While+Developing+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TXO_d594Ri8
- YouTube title: Build in Observability While Developing - Jamie Danielson, Honeycomb.io
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/build-in-observability-while-developing/TXO_d594Ri8.txt
- Transcript chars: 36294
- Keywords: little, instrumentation, logs, looking, working, locally, honeycomb, actually, automatic, feature, collector, information, important, adding, getting, trace, someone, attributes

### Resumo baseado na transcript

uh thanks everyone for your patience uh also this is exciting I don't know show of hands anyone else their first time at cucon me yeah wow a lot so uh a lot of excitement hopefully we can have some fun during the session uh thanks everyone for joining I know some of you may have just been hanging around after Charity's talk but I appreciate you staying comfortable and hanging out for me um so yeah hopefully uh you'll get something out of this you'll learn a little bit

### Excerpt da transcript

uh thanks everyone for your patience uh also this is exciting I don't know show of hands anyone else their first time at cucon me yeah wow a lot so uh a lot of excitement hopefully we can have some fun during the session uh thanks everyone for joining I know some of you may have just been hanging around after Charity's talk but I appreciate you staying comfortable and hanging out for me um so yeah hopefully uh you'll get something out of this you'll learn a little bit more about how to make observability a regular part of your development workflow um and you'll take away some tips on how to get into that so a little bit about me uh I'm Jamie Danielson I work at honeycomb uh I am a Telemetry engineer so I work in the instrumentation libraries and I'm an approver on open Telemetry JavaScript so I apologize in advance for any of the groans I know I'll probably hear later a lot of the examples are in JavaScript but it is applicable to many the other languages um so kind of we'll we'll go through a lot of general concepts if you uh practice practical applications uh and keep in mind that even though a lot of it is Javascript um it will be applicable to other languages like go or python or anything like that so the biggest thing that we kind of want to get out of the way is that if you know how to log you know how to trace now most people are using logging of some form today whether that's your local console logging or printing to your terminal or you have some other kind of logs that are being aggregated and sent somewhere and there's this thought of how do I make that leap how do I get from logs to traces I've heard that maybe traces are good but it seems like a really big deal and I don't know how to get everyone behind me on making this big change but what I'm here to hopefully tell you a little bit about is that it's not as big of a leap as you might think that it is so something like this uh might look a little bit familiar where you just have all of these logs and you know these logs are just sort of generally maybe a request to an endpoint handling that request looking up an item things like that there's a lot of useful info information in here and I'm not going to tell you that it's not useful in fact this is a lot of really important information the hard part about it is there's a lot of free text it can be hard to see how these different logs maybe correlate with each other how they're affecting other logs other things that are happening and when it c
