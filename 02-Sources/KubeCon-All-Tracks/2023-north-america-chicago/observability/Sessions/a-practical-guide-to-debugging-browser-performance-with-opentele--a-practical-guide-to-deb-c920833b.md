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
themes: ["Observability", "SRE Reliability"]
speakers: ["Purvi Kanal", "Honeycomb"]
sched_url: https://kccncna2023.sched.com/event/1R2m6/a-practical-guide-to-debugging-browser-performance-with-opentelemetry-purvi-kanal-honeycomb
youtube_search_url: https://www.youtube.com/results?search_query=A+Practical+Guide+to+Debugging+Browser+Performance+with+OpenTelemetry+CNCF+KubeCon+2023
slides: []
status: parsed
---

# A Practical Guide to Debugging Browser Performance with OpenTelemetry - Purvi Kanal, Honeycomb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Purvi Kanal, Honeycomb
- Schedule: https://kccncna2023.sched.com/event/1R2m6/a-practical-guide-to-debugging-browser-performance-with-opentelemetry-purvi-kanal-honeycomb
- Busca YouTube: https://www.youtube.com/results?search_query=A+Practical+Guide+to+Debugging+Browser+Performance+with+OpenTelemetry+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre A Practical Guide to Debugging Browser Performance with OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2m6/a-practical-guide-to-debugging-browser-performance-with-opentelemetry-purvi-kanal-honeycomb
- YouTube search: https://www.youtube.com/results?search_query=A+Practical+Guide+to+Debugging+Browser+Performance+with+OpenTelemetry+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0J1z599tmfY
- YouTube title: A Practical Guide to Debugging Browser Performance with OpenTelemetry - Purvi Kanal, Honeycomb
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/a-practical-guide-to-debugging-browser-performance-with-opentelemetry/0J1z599tmfY.txt
- Transcript chars: 33189
- Keywords: actually, performance, website, important, browser, instrumentation, little, trying, measure, loaded, backend, pretty, metrics, getting, largest, element, sampling, content

### Resumo baseado na transcript

hello everyone welcome to coupon um my name is purvy hi I work at honeycom um I've worked with browsers for a really large part of my career and I'm really interested in getting frontend observability to a standard that's on par with the kind of observability we have for backend systems today as I mentioned I work at honeycomb where we're trying to solve this problem and I'm an approver on the open Telemetry JS project with a special interest in web AP and I'm really excited to talk

### Excerpt da transcript

hello everyone welcome to coupon um my name is purvy hi I work at honeycom um I've worked with browsers for a really large part of my career and I'm really interested in getting frontend observability to a standard that's on par with the kind of observability we have for backend systems today as I mentioned I work at honeycomb where we're trying to solve this problem and I'm an approver on the open Telemetry JS project with a special interest in web AP and I'm really excited to talk about open Telemetry and browser performance today so I want to start by getting to us getting us to a common understanding of what I mean by web performance because it can mean a lot of different things to a lot of different people as devs I think sometimes we try to make things as fast as possible and honestly that's really fun it is really fun and Engineering problem to make things fast and performant and we kind of like end up convincing the execs by saying something like improving our page load times will get us increased conversions and you know um exacts like money so it's it's a good argument but it's honestly pretty hard to correlate that or I guess caate that directly with data so when I'm talking about performance on the web today I'm more interested in if the users of those website think that that website is performant it's much more it's a much more accurate indicator of how your website is going to be used and whether your website is easy to use based on what users think more than what your page load metrics might say because ultimately and this is from the mdn docs which are kind of the the main browser source of documentation web performance is really all about making websites fast but that also includes making slow processes seem fast to users and that's a really important distinction that perceived performance is really really important so what are our web performance goals before we get into what we measure and how we measure things I think it helps to think about what components make up a performant web page and that includes that definitely includes reducing our overall load time but it also includes making the site usable as soon as possible are people actually able to carry out the interactions that they expect to after the page has loaded without getting frustrated is the site reliable and pleasant to use are things moving all over the page can I get a show of hands if you've ever used a website that has really annoyed you to no end yes right we're all u
