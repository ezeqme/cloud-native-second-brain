---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability"]
speakers: ["Sam Alipio", "Mario Macías", "Grafana Labs"]
sched_url: https://kccncna2025.sched.com/event/27Fc8/observing-dark-matter-with-opentelemetry-sam-alipio-mario-macias-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Observing+Dark+Matter+With+OpenTelemetry+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Observing Dark Matter With OpenTelemetry - Sam Alipio & Mario Macías, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Sam Alipio, Mario Macías, Grafana Labs
- Schedule: https://kccncna2025.sched.com/event/27Fc8/observing-dark-matter-with-opentelemetry-sam-alipio-mario-macias-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Observing+Dark+Matter+With+OpenTelemetry+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Observing Dark Matter With OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fc8/observing-dark-matter-with-opentelemetry-sam-alipio-mario-macias-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Observing+Dark+Matter+With+OpenTelemetry+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pfBw4g1LdAM
- YouTube title: Observing Dark Matter With OpenTelemetry - Sam Alipio & Mario Macías, Grafana Labs
- Match score: 0.764
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/observing-dark-matter-with-opentelemetry/pfBw4g1LdAM.txt
- Transcript chars: 19003
- Keywords: instrumentation, network, application, traffic, traces, source, request, another, response, metrics, ebpf, measure, process, server, instrumented, collector, custom, whatever

### Resumo baseado na transcript

Thank you for attending this talk observing the dark matter with open telemetry. I'm principal software engineer in the graphana labs and maintainer of the open telemetry evpf instrumentation product. It can listen for uh application events and again use those to generate metrics and traces. Um asynchronous uh runtimes like Rust uh things like tracing might not work. What OB gives you are application level red metrics uh partial support for traces network level flow metrics and BA does all of the above plus some stuff that wasn't a great fit for the open telemetry project. Uh process level metrics and some graphana cloud specific integrations.

### Excerpt da transcript

Thank you for attending this talk observing the dark matter with open telemetry. I'm Mario Matias. I'm principal software engineer in the graphana labs and maintainer of the open telemetry evpf instrumentation product. >> Hi, I'm Sam. I'm a product manager for a product called Tessact Core and other open source stuff at a company called Paster Labs. We are an enduser of a number of CNCF technologies including open telemetry uh as we deliver our platform for simulation intelligence. So what are we talking about? Um let's say you've got an application and you want insights into how it's performing. Uh but this application is not instrumented and so you need to do something in order to start emitting telemetry to say an open telemetry collector so you can pass that along to your preferred observability tooling. Um, so what do you do? What are your options? One option would be agent-based instrumentation. So, uh, for runtimes like Java ornet, this is kind of the go-to option. You inject an agent that, um, listens for application events like, uh, network calls and uses those to generate metrics, logs, and traces that you can then pass along to an hotel collector.

For a compiled language, for example, Go or C++, you're going to need to do some manual instrumentation. So that means making some change to your code, rebuilding your application, uh, and then deploying that so that you can start emitting telemetry. So there's probably some obvious downsides to this. It's going to take you time and it's going to take you effort. So is there a third option, another way? Um, yes. So we've got eBPF auto instrumentation as an alternative. Ebpf at a really high level. um is a technology that runs in the Linux kernel. It allows you to attach small programs to different parts of your stack like your runtime or your libraries. It can listen for uh application events and again use those to generate metrics and traces. And there are a number of benefits of ebpf instrumentation. So it's pretty seamless. Um you don't need to reconfigure or rebuild and redeploy your application. You have a component, you drop it in and you basically get instant telemetry. um it's pretty low latency especially compared to um some interpreted language SDKs like Python and Ruby which add some non-negligible latency um ebpf is compiled just in time so it's really fast um and then what we'll mostly focus on today is this idea of improved system level data um because you can introspect your runtime and
