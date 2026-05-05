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
themes: ["Observability", "Storage Data"]
speakers: ["Pedro Célestin", "CLDF", "Julia Furst Morgado", "Dash0"]
sched_url: https://kccncna2025.sched.com/event/27FXU/integrating-data-center-observability-into-cloud-native-environment-pedro-celestin-cldf-julia-furst-morgado-dash0
youtube_search_url: https://www.youtube.com/results?search_query=Integrating+Data+Center+Observability+Into+Cloud+Native+Environment+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Integrating Data Center Observability Into Cloud Native Environment - Pedro Célestin, CLDF & Julia Furst Morgado, Dash0

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: United States / Atlanta
- Speakers: Pedro Célestin, CLDF, Julia Furst Morgado, Dash0
- Schedule: https://kccncna2025.sched.com/event/27FXU/integrating-data-center-observability-into-cloud-native-environment-pedro-celestin-cldf-julia-furst-morgado-dash0
- Busca YouTube: https://www.youtube.com/results?search_query=Integrating+Data+Center+Observability+Into+Cloud+Native+Environment+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Integrating Data Center Observability Into Cloud Native Environment.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXU/integrating-data-center-observability-into-cloud-native-environment-pedro-celestin-cldf-julia-furst-morgado-dash0
- YouTube search: https://www.youtube.com/results?search_query=Integrating+Data+Center+Observability+Into+Cloud+Native+Environment+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TsNfSKppiPU
- YouTube title: Integrating Data Center Observability Into Cloud Native Envi... Pedro Célestin & Julia Furst Morgado
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/integrating-data-center-observability-into-cloud-native-environment/TsNfSKppiPU.txt
- Transcript chars: 27204
- Keywords: logs, center, observability, metrics, infrastructure, running, collector, actually, layers, everything, physical, approach, pipeline, solution, environment, conventions, little, specific

### Resumo baseado na transcript

I'm a principal developer relations engineer at D-Zero as of last week. Uh we're both CNCF ambassadors, very involved in the Kubernetes and cloudnative communities. They're running everything on Kubernetes again Prometheus uh open telemetry uh defining SLIS SLOs's and they're trying to make everything observable from top down. So in the data center, the monitoring stack still speaks ancient dialect, SNMP, traps, the v center, APIs, uh sys logs, etc. But the other side, the cloud side speaks fluent promql OTP TLP and you've got you've got structured JSON logs etc. So, and if you've ever been in the middle of an incident, you know how how costly that is.

### Excerpt da transcript

Hi everyone, welcome to our talk. Thank you for being here. We're really excited to be presenting this case for you. My name is Julia. I'm a principal developer relations engineer at D-Zero as of last week. And uh I'm here with my partner in observability crime. Pedro Pedro, he's uh an a principal SR at CLLDF. And CLLDF is the legislative chamber in Brazil's capital, Brazilia. He's also a golden cubstronaut. Uh we're both CNCF ambassadors, very involved in the Kubernetes and cloudnative communities. If you're have questions about it, come ask us after. Now tell me if this sounds familiar. You've got part of your infrastructure running on Kubernetes containers, Prometheus, Open Telemetry, and then part of the the other part still lives in your data center. You have them running on an SMP vendor dashboards and tools that look like they were designed in Windows XP. And the question we're going to discuss today is how do we actually connect these two worlds? How do we bridge the gap between onrem and old school telemetry and modern observability uh pipelines?

So uh let's start with the elephant in the room which is the observ observability divide. the case that uh was in Pedro's organization. So technically everything runs in containers and on one side you can see the legislative chamber and then on one side you've got the infrastructure team. So CIS admins and knock folks uh who care about disks about switches power and all the phys physical things that keeps lights on and then their their world is all about stability uh keeping workloads up and keeping all the lights green. Now on the other side we have S surres and platform engineers. They're running everything on Kubernetes again Prometheus uh open telemetry uh defining SLIS SLOs's and they're trying to make everything observable from top down. So both sides they're doing critical work which is very important. They depend on each other but they're living two completely different realities and when something breaks they don't talk to each other they don't have visibility into each other's uh others layers and uh there is this they started this scientific troubleshooting process that we call blaming the other team.

So uh now let's break down why that happens. The first challenge is fragmented telemetry formats. So Pedro setup is the perfect example. Everything runs in containers, but the data that they emit depends entirely on where they live. So in the data center, the monitoring stack still speaks ancien
