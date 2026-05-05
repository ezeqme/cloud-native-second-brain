---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Storage Data", "Community Governance"]
speakers: ["Jade Guiton", "Datadog", "Dmitrii Anoshin", "Cisco", "Alex Boten", "Honeycomb", "Evan Bradley", "Dynatrace LLC", "Antoine Toulme", "Splunk"]
sched_url: https://kccnceu2026.sched.com/event/2EF6f/opentelemetry-collector-sig-project-updates-jade-guiton-datadog-dmitrii-anoshin-cisco-alex-boten-honeycomb-evan-bradley-dynatrace-llc-antoine-toulme-splunk
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Collector+SIG%3A+Project+Updates+CNCF+KubeCon+2026
slides: []
status: parsed
---

# OpenTelemetry Collector SIG: Project Updates - Jade Guiton, Datadog; Dmitrii Anoshin, Cisco; Alex Boten, Honeycomb; Evan Bradley, Dynatrace LLC; Antoine Toulme, Splunk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jade Guiton, Datadog, Dmitrii Anoshin, Cisco, Alex Boten, Honeycomb, Evan Bradley, Dynatrace LLC, Antoine Toulme, Splunk
- Schedule: https://kccnceu2026.sched.com/event/2EF6f/opentelemetry-collector-sig-project-updates-jade-guiton-datadog-dmitrii-anoshin-cisco-alex-boten-honeycomb-evan-bradley-dynatrace-llc-antoine-toulme-splunk
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+Collector+SIG%3A+Project+Updates+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre OpenTelemetry Collector SIG: Project Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6f/opentelemetry-collector-sig-project-updates-jade-guiton-datadog-dmitrii-anoshin-cisco-alex-boten-honeycomb-evan-bradley-dynatrace-llc-antoine-toulme-splunk
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+Collector+SIG%3A+Project+Updates+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0zwLl8QGOdM
- YouTube title: OpenTelemetry Collector SIG: Project Updates - Jade G, Dmitrii A, Alex B, Evan B & Antoine T
- Match score: 0.757
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/opentelemetry-collector-sig-project-updates/0zwLl8QGOdM.txt
- Transcript chars: 32917
- Keywords: collector, components, component, receiver, contrib, processor, prometheus, metrics, trying, wanted, attributes, available, exporter, entities, update, builder, stabilize, having

### Resumo baseado na transcript

All right, thanks for I guess thanks for staying after the project update. So, all right, welcome to the open telemetry collector projector up project updates, not projector updates. Even uh core components like the Prometheus receiver uh lives in that repository for historical reasons which we won't get into. kind of started talking about okay well what can we do to enable stable by default meaning that um you know we we do away with any uh any surprises or any things that could be like affected the performance of the collector by default. This is the list of components we got from our uh user surveys and uh we are now going to talk about the Kubernetes component I think. So the Kubernetes components starting with the K8 attributes processor are working on um basically consolidating on the hotel sem um just declared RFC.

### Excerpt da transcript

All right, thanks for I guess thanks for staying after the project update. I think you really sold everybody on staying in the room. So, all right, welcome to the open telemetry collector projector up project updates, not projector updates. Um, this is I guess now year seven of the open telemetry collector, so it was probably about time that we put on a put on an update for you. Um, so I'm Alex. Uh with me I have Antoine, Dimmitri, Jad, and Evan. And we're all uh open telemetry collector contributors, maintainers, approvers. Um and we're going to give you uh an update on all of the efforts we've been putting into the collector, various components, as well as the stability effort as was uh advertised earlier in the previous session. If you would like to have a time machine and go back to the previous session, you can always do that. You're right. I have a button. I have a button and I can walk around. Great. Um, so just show of hands. Who here doesn't know what a collector is? I know you're lying. Okay.

All right. Thank you. So, this you I won't spend too much time on the slide. The collector is a multi-tool. It's a binary that the project makes available for people to use for receiving and sending data and processing it. So, I'm just going to move right along here. So um we're going to really focus on kind of the project the project status but also we're going to give because this is the first update that we've ever given. We're also going to talk a little bit about how the collector is organized. So the collector sig is u maintaining all of these three different repositories. We uh we split them into three repos based on you know roughly the following uh responsibilities. So the main collector repository the open telemetry collector repo we also call it the core the core repo contains things like the core libraries that every component relies on for implementing uh the various aspects of what they do. uh it includes also some key components like the OTLP receiver and exporter uh also the batch processor which eventually will I I don't want to spoil your your slide so um and uh it also includes things like the builder and m data genen so the builder is the tool that you can use to create your own uh open telemetry collector distro all of the distros that we maintain and make available use the builder to build them uh we'll talk a little bit more about that and uh the next repo we maintain is a collector contrib repo.

If you have you all run a collector i
