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
themes: ["AI ML", "Observability", "Storage Data"]
speakers: ["Frederic Branczyk", "Polar Signals", "Shahar Azulay", "groundcover", "Valeri Pliskin", "Datadog", "Anna Kapuścińska", "Isovalent"]
sched_url: https://kccncna2023.sched.com/event/1R2pi/ebpf-for-observability-data-overload-panacea-or-pain-frederic-branczyk-polar-signals-shahar-azulay-groundcover-valeri-pliskin-datadog-anna-kapuscinska-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=eBPF+for+Observability%3A+Data+Overload+Panacea+or+Pain+CNCF+KubeCon+2023
slides: []
status: parsed
---

# eBPF for Observability: Data Overload Panacea or Pain - Frederic Branczyk, Polar Signals; Shahar Azulay, groundcover; Valeri Pliskin, Datadog; Anna Kapuścińska, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]]
- País/cidade: United States / Chicago
- Speakers: Frederic Branczyk, Polar Signals, Shahar Azulay, groundcover, Valeri Pliskin, Datadog, Anna Kapuścińska, Isovalent
- Schedule: https://kccncna2023.sched.com/event/1R2pi/ebpf-for-observability-data-overload-panacea-or-pain-frederic-branczyk-polar-signals-shahar-azulay-groundcover-valeri-pliskin-datadog-anna-kapuscinska-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=eBPF+for+Observability%3A+Data+Overload+Panacea+or+Pain+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre eBPF for Observability: Data Overload Panacea or Pain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pi/ebpf-for-observability-data-overload-panacea-or-pain-frederic-branczyk-polar-signals-shahar-azulay-groundcover-valeri-pliskin-datadog-anna-kapuscinska-isovalent
- YouTube search: https://www.youtube.com/results?search_query=eBPF+for+Observability%3A+Data+Overload+Panacea+or+Pain+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3wyfGmUNPE8
- YouTube title: eBPF for Observability: Data Overload Panacea or Pain...
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/ebpf-for-observability-data-overload-panacea-or-pain/3wyfGmUNPE8.txt
- Transcript chars: 35861
- Keywords: ebpf, kernel, observability, security, basically, application, actually, programs, pretty, started, performance, languages, instrumentation, everything, running, little, program, easier

### Resumo baseado na transcript

okay thanks everyone for coming today this is our panel ebpf for observability data overload Panacea or pain and the key question that we're going to be trying to understand here by the end of the panel is ebpf finally the Panacea to observability problems or will it just be another Deluge of unhelpful data only to bring pain to our already overloaded observability teams so with that let's get started uh we have a great set of panelists here and the first question I'd like you uh each to

### Excerpt da transcript

okay thanks everyone for coming today this is our panel ebpf for observability data overload Panacea or pain and the key question that we're going to be trying to understand here by the end of the panel is ebpf finally the Panacea to observability problems or will it just be another Deluge of unhelpful data only to bring pain to our already overloaded observability teams so with that let's get started uh we have a great set of panelists here and the first question I'd like you uh each to introduce yourself and tell me a little bit about how you're using ebpf for observability in your project all right cool so I'm Frederick um I founded a company called polar signals and we do uh profiling using ebpf um in case people are maybe not familiar profiling kind of allows you to see um where resources are being spent in your code down to your down to the line number in your source code and the way that our profiler works or that generally any sampling profiler works is um based on like a CPU overflow basis so every x amount of CPU Cycles our ebpf program gets run and the way our ebpf program works is that it figures out what is the current function call stack and saves that and then we can build statistics using that to say if we see the same function call stack multiple times we can say statistically speaking that's where that amount of time was being spent and so that's the product and um we have an open source project as well called parka PCA that you know you can you can go ahead and try out immediately has an awesome kubernetes integration thanks uh hi I'm Anna I work at ISA valent a company that is known mostly from uh now graduated project uh which ises ebpf for networking I work valent uh on the observability side uh on a few projects uh first of all hble which is uh observability layer for celium which doesn't use cbpf directly but sort of pigb backs on what celium does and um processes that networking data uh and second project is tetragon which is a security observability project uh using gpf mostly in security context to give a security teams visibility into what's going on and also to um provide enforcement hey everyone uh I'm shakar I'm uh the co-founder and CEO of gr cover uh gr cover is basically building a full observability stack on top of ebpf which basically means that we provide application metrics application tracing uh troubleshooting on top of a platform by correlating Metric log traces basically anything you can expect from Full APM or app
