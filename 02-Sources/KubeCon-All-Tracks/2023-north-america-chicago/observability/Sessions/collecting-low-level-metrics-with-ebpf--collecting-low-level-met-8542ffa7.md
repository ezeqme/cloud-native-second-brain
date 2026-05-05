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
speakers: ["Mauricio Vásquez Bernal", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2pH/collecting-low-level-metrics-with-ebpf-mauricio-vasquez-bernal-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Collecting+Low-Level+Metrics+with+eBPF+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Collecting Low-Level Metrics with eBPF - Mauricio Vásquez Bernal, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Mauricio Vásquez Bernal, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2pH/collecting-low-level-metrics-with-ebpf-mauricio-vasquez-bernal-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Collecting+Low-Level+Metrics+with+eBPF+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Collecting Low-Level Metrics with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pH/collecting-low-level-metrics-with-ebpf-mauricio-vasquez-bernal-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Collecting+Low-Level+Metrics+with+eBPF+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_ft3iTw5uv8
- YouTube title: Collecting Low-Level Metrics with eBPF - Mauricio Vásquez Bernal, Microsoft
- Match score: 0.771
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/collecting-low-level-metrics-with-ebpf/_ft3iTw5uv8.txt
- Transcript chars: 25241
- Keywords: metrics, information, kernel, ebpf, provide, program, metric, understand, programs, inspector, specific, configuration, tetragon, gadget, labels, events, container, number

### Resumo baseado na transcript

okay hello everybody Welcome to this presentation thank you so much for attending my presentation I'm Mauricio I work as a software engineer for Microsoft and today I will be presenting you how to collect low level metrics by using BPF so yeah in the agenda of today I want to introduce the concept of metrics I hope that you many of you are already familiar with that otherwise this is just a quick introduction to metrics and the same for ebpf I will be covering very quickly what ebpf

### Excerpt da transcript

okay hello everybody Welcome to this presentation thank you so much for attending my presentation I'm Mauricio I work as a software engineer for Microsoft and today I will be presenting you how to collect low level metrics by using BPF so yeah in the agenda of today I want to introduce the concept of metrics I hope that you many of you are already familiar with that otherwise this is just a quick introduction to metrics and the same for ebpf I will be covering very quickly what ebpf is and some concept that we need to understand the content of this talk then after that I will be speaking what is the relationship between Matrix and ebpf and finally I will be presenting some of the projects that we can use to collect matrics by using BPF okay so there we are so metrics by definition a metric is a measurement of a service capture around time so we can think of a metric like a number that represents the performance of of the help of our service so yeah examples of metrics are the CP the percentage of CPU that our system is using the quantity of run that our system is using the error rate of the response that output of our system or yeah basically any numeric measurement that you can do on your system that represents the performance of that so why do we need metrics well by using metrics we are able to understand if our service is available and also we are able to understand what is the performance of our service yeah for sure probably many many of you get alerts when a metric is changing on the system when there is a an outage so yeah we we can configure those roles H to understand when there is an issue with our system and another thing that we can use metrix for is to perform trigger scheduling decision so if we need to allocate more resources for our system or maybe we have so many resources and we need to remove some of them for our system there are different kind of metrics so the first one is like the simplest one to understand is the counter so the counter is a numeric value that only can go up so we can use counters for representing the the numbers of bucket that are being on a system the total H the number of requests that are being processed and so on the second one is gauges so gauges are is also a single numerical type that can go up or down and example of gauge could be the CPU usage on our system so we can have high CPU usage but it can go down or up the same for memory so we can our system could consume more or less memory so yeah that's a numer
