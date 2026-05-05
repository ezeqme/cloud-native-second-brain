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
speakers: ["Amir Jakoby", "Sawmills", "Shiran Melamed", "JFrog"]
sched_url: https://kccncna2025.sched.com/event/27Fas/zero-downtime-telemetry-hot-reloading-opentelemetry-collector-pipelines-amir-jakoby-sawmills-shiran-melamed-jfrog
youtube_search_url: https://www.youtube.com/results?search_query=Zero-Downtime+Telemetry%3A+Hot+Reloading+OpenTelemetry+Collector+Pipelines+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Zero-Downtime Telemetry: Hot Reloading OpenTelemetry Collector Pipelines - Amir Jakoby, Sawmills & Shiran Melamed, JFrog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Amir Jakoby, Sawmills, Shiran Melamed, JFrog
- Schedule: https://kccncna2025.sched.com/event/27Fas/zero-downtime-telemetry-hot-reloading-opentelemetry-collector-pipelines-amir-jakoby-sawmills-shiran-melamed-jfrog
- Busca YouTube: https://www.youtube.com/results?search_query=Zero-Downtime+Telemetry%3A+Hot+Reloading+OpenTelemetry+Collector+Pipelines+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Zero-Downtime Telemetry: Hot Reloading OpenTelemetry Collector Pipelines.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fas/zero-downtime-telemetry-hot-reloading-opentelemetry-collector-pipelines-amir-jakoby-sawmills-shiran-melamed-jfrog
- YouTube search: https://www.youtube.com/results?search_query=Zero-Downtime+Telemetry%3A+Hot+Reloading+OpenTelemetry+Collector+Pipelines+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ngm1mHVfcgY
- YouTube title: Zero-Downtime Telemetry: Hot Reloading OpenTelemetry Collector Pipel... Amir Jakoby & Shiran Melamed
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/zero-downtime-telemetry-hot-reloading-opentelemetry-collector-pipeline/ngm1mHVfcgY.txt
- Transcript chars: 17842
- Keywords: collector, processor, configuration, change, reload, eventually, without, metrics, restart, working, entire, solution, destination, traces, incident, update, logs, vendor

### Resumo baseado na transcript

So when you go to the train station, you see people coming from all kind of places, the streets, their bus, their offices, their homes and eventually they want to reach their destination without getting lost. So there is a need in a control system or a person that will navigate those people to the right destination and to the right trains. Second example is Microsoft open AI they did a change at overl kubernetes control plane with thousands of APIs and three hours of downtime for open AI. The challenge in the industry was to manage binaries and images and J4 created artifactory for that. But within the years much more challenges arrived and JFrog today is not a one tool application. It's a a complete platform that handles more challenges security challenge machine learning channel and just lately we came out with the beta of JFK fly an MCP server that can communicate with your private repository.

### Excerpt da transcript

Hi everyone. Thank you for joining us today. It's really fun to be here and we are really happy. So when you go to the train station, you see people coming from all kind of places, the streets, their bus, their offices, their homes and eventually they want to reach their destination without getting lost. So there is a need in a control system or a person that will navigate those people to the right destination and to the right trains. We don't want them to get lost in the way. And the same goes for telemetry data logs, metrics and traces needs to reach their destination if it's storage or data dog vendor or any other back end. And we don't want this data to get lost. So when it comes to size, it can be between megabytes of data to pabytes of data a day. And eventually we need to deal with loads of data coming in and how we can handle this amount of data and even if it's small but we don't want the data to get lost. We want it to be fast. So what is the challenge here? >> So what's the challenge? >> Imagine turning tuning a system that never stops moving.

H at Netflix we they handle scale of about 500 billion events and 1.5 1.3 uh pabytes of data a day. On top of that they're doing dozen of configuration changes to their uh telemetry agents uh without an incident and how can you do that without incident? What's the issue with that? So incidents are enormous when it comes to configuration change and we see that the blast produce is is really really big. One example is crowd strike they brought an update for their configuration. The update was available for 78 minutes. On that time Windows machine starting to get this update and crashed. So all their system went down. Even after they removed this update they it still had effect and the blast radius was enormous because other companies also work with crowd strike and were were harmed from this issue. Second example is Microsoft open AI they did a change at overl kubernetes control plane with thousands of APIs and three hours of downtime for open AI. So the blast radius from doing such a small thing we want to change our configuration it's crazy we can take down the whole company because of this change.

So what we are trying to solve so today we're going to talk about open telemetry collector. The collector is part of the uh open telemetry initiative which is part of CNCF. Uh what what are we doing with the collector when it comes to uh configuration changes today? The collector only support full restart uh i
