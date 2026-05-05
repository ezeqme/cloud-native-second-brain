---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability"]
speakers: ["Dom Del Nano", "Cosmic"]
sched_url: https://kccnceu2025.sched.com/event/1txE6/expanding-ebpfs-reach-from-batteries-included-auto-instrumentation-to-e2e-observability-pipelines-dom-del-nano-cosmic
youtube_search_url: https://www.youtube.com/results?search_query=Expanding+eBPF%E2%80%99s+Reach%3A+From+Batteries-Included+Auto-Instrumentation+To+E2E+Observability+Pipelines+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Expanding eBPF’s Reach: From Batteries-Included Auto-Instrumentation To E2E Observability Pipelines - Dom Del Nano, Cosmic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Dom Del Nano, Cosmic
- Schedule: https://kccnceu2025.sched.com/event/1txE6/expanding-ebpfs-reach-from-batteries-included-auto-instrumentation-to-e2e-observability-pipelines-dom-del-nano-cosmic
- Busca YouTube: https://www.youtube.com/results?search_query=Expanding+eBPF%E2%80%99s+Reach%3A+From+Batteries-Included+Auto-Instrumentation+To+E2E+Observability+Pipelines+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Expanding eBPF’s Reach: From Batteries-Included Auto-Instrumentation To E2E Observability Pipelines.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txE6/expanding-ebpfs-reach-from-batteries-included-auto-instrumentation-to-e2e-observability-pipelines-dom-del-nano-cosmic
- YouTube search: https://www.youtube.com/results?search_query=Expanding+eBPF%E2%80%99s+Reach%3A+From+Batteries-Included+Auto-Instrumentation+To+E2E+Observability+Pipelines+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I236sjooftw
- YouTube title: Expanding eBPF’s Reach: From Batteries-Included Auto-Instrumentation To E2E Observab... Dom Del Nano
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/expanding-ebpfs-reach-from-batteries-included-auto-instrumentation-to/I236sjooftw.txt
- Transcript chars: 20481
- Keywords: ebpf, basically, observability, events, hubble, instrumentation, actually, projects, security, programmability, important, properties, gadget, provides, script, mentioned, looking, interface

### Resumo baseado na transcript

So before we jump into things, I wanted to give myself a brief introduction. I also spent a bit of time at CrowdStrike working on their ebpf Linux sensor. With ebpf, the instrumentation cost goes down dramatically because hooking into the kernel, you instrument it once and it's already available. And so these tools need to enrich your data with Kubernetes primitives with container primitives in order to make it useful. If you're using a, you know, ebpf is applicable in security context in observability context and you need the ebpf tool to not just like filter the data, but you actually want to be able to like apply observability focus on it or security focus. It's container and Kubernetes aware and it provides rich filtering, collection, and the ability to export it to other systems.

### Excerpt da transcript

Hello, CubeCon. Hope you all are having a great start to your week. Um, my name is Dom Donano. I'm CEO and founder of Cosmic and also a CNCF Pixie core maintainer. And I'm excited to talk to you about expanding EBPF's reach. So before we jump into things, I wanted to give myself a brief introduction. Um, as I mentioned, I work on the CNCF Pixie project. I got started back with the project three and a half years ago. First as an enduser and then turned maintainer. I also spent a bit of time at CrowdStrike working on their ebpf Linux sensor. So I've been working in the ebpf space the last few years. So before we get into the ebpf stuff, I wanted to talk about where things came from. So before the cloud and containers, we had these monolithic architectures. They were simplistic. It was easy to debug issues. You know, these three pillars of observability weren't really a thing at this point because inspecting and finding bugs were easy. They were in the big monolithic application. And so it wasn't until microservices and containers and Kubernetes came along that observability became a really important uh operational tool.

And so you can see on this picture here that um these are what our environments look like today. We have services written in different programming languages. We have SAS services. You know, we depend on all these third party APIs that we have to talk to over the internet. And also there's a variety of data stores used. And so observing these things becomes very important when there's so many different logical pieces. and monitoring and observability started off with manual instrumentation. So back when there was the monolith or less programming languages, it was easy to instrument each piece. But as the number of combinations grew, it became a lot more effort and work to support Go, to support Java, to support all these different flavors of things. And so this manual instrumentation started to become very expensive in these polygot environments. This is where ebpf comes into the picture. So looking uh we're going to kind of compare how you would traditionally do monitoring observability against how autot telemetry works.

And so uh there's sort of three verticals to think about. There's coverage, effort, and flexibility. So for the manual instrumentation, the coverage tends to be sparse. um for thirdparty applications and SAS it's often infeasible you know unless you can change the code you can't instrument it or for SAS tools you know you'r
