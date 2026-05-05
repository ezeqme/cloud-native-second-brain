---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Christos Kalkanis", "Elastic"]
sched_url: https://kccncna2024.sched.com/event/1i7nz/low-overhead-zero-instrumentation-continuous-profiling-for-opentelemetry-christos-kalkanis-elastic
youtube_search_url: https://www.youtube.com/results?search_query=Low-Overhead%2C+Zero-Instrumentation%2C+Continuous+Profiling+for+OpenTelemetry+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Low-Overhead, Zero-Instrumentation, Continuous Profiling for OpenTelemetry - Christos Kalkanis, Elastic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Christos Kalkanis, Elastic
- Schedule: https://kccncna2024.sched.com/event/1i7nz/low-overhead-zero-instrumentation-continuous-profiling-for-opentelemetry-christos-kalkanis-elastic
- Busca YouTube: https://www.youtube.com/results?search_query=Low-Overhead%2C+Zero-Instrumentation%2C+Continuous+Profiling+for+OpenTelemetry+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Low-Overhead, Zero-Instrumentation, Continuous Profiling for OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nz/low-overhead-zero-instrumentation-continuous-profiling-for-opentelemetry-christos-kalkanis-elastic
- YouTube search: https://www.youtube.com/results?search_query=Low-Overhead%2C+Zero-Instrumentation%2C+Continuous+Profiling+for+OpenTelemetry+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WtNDLgdIn24
- YouTube title: Low-Overhead, Zero-Instrumentation, Continuous Profiling for OpenTelemetry - Christos Kalkanis
- Match score: 0.969
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/low-overhead-zero-instrumentation-continuous-profiling-for-opentelemet/WtNDLgdIn24.txt
- Transcript chars: 34757
- Keywords: profiling, frames, ebpf, support, essentially, unwinding, kernel, language, native, memory, program, python, languages, programs, symbolization, trace, working, information

### Resumo baseado na transcript

hello everyone and welcome to this talk U this talk is about low overhead zero instrumentation profiling in the context of Home Telemetry and more specifically about the ebpf profiling agents that elastic has recently donated to open Telemetry my name is Chris calanis I'm currently working as a principal engineer at elastic I'm also a maintainer of the open Telemetry profiling Sig and a co-author and maintainer of the open cemetry ebpf profiler that is the subject of this talk I took this slide from one of my favorite

### Excerpt da transcript

hello everyone and welcome to this talk U this talk is about low overhead zero instrumentation profiling in the context of Home Telemetry and more specifically about the ebpf profiling agents that elastic has recently donated to open Telemetry my name is Chris calanis I'm currently working as a principal engineer at elastic I'm also a maintainer of the open Telemetry profiling Sig and a co-author and maintainer of the open cemetry ebpf profiler that is the subject of this talk I took this slide from one of my favorite lnk presentations it's called making progress and I highly recommend you watch it it's a photograph of the NASA Mission Control Center and the last line at the bottom reads software organizations who don't have a situation room don't understand where they are now in this and another presentations Alan argues for biologically inspired approaches to modeling complex systems with continuous feedback play playing a pro a prominent role I think that this is highly relevant to today's complicated observability landscape as information proliferation and the move to highly distributed microservice heavy architectures is making it a lot harder to distinguish signal from noise so this is something that continuous profiling can definitely help with Thomas Dulan has talked about the cloud becoming the new operating system and from this point of view continuous profilers can be seen seen as tools that are native to and designed for this new substrate as an example uh many companies have difficulty mapping CPU consumption down to specific lines of code and tracking performance regressions over time some hyperscalers have had data center-wide continuous profiling for some time for example Google they call it Google wide profiling they've even published a few papers about it so and those papers have been very influential but generally speaking continuous profiling hasn't been widely available contemporary profilers do not work well with production binaries that are usually compiled without frame pointers and without symbols and they don't typically support high level languages without application instrumentation it will be great uh if we could make a lightweight data center wide uh continuous profiler that could be easily deployed and supports all widely used programming languages available to everyone and uh this is exactly what we try to accomplish in a startup called optimize Cloud where in 2021 we launched the low overhead multi runtime uh zero instrumen
