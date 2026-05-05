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
themes: ["AI ML", "Security", "Runtime Containers", "Community Governance"]
speakers: ["Iacopo Rozzo", "Sysdig", "Aldo Lacuku", "Kong Inc."]
sched_url: https://kccnceu2026.sched.com/event/2EF6W/in-falcos-nest-the-evolution-of-cloud-native-runtime-security-iacopo-rozzo-sysdig-aldo-lacuku-kong-inc
youtube_search_url: https://www.youtube.com/results?search_query=In+Falco%27s+Nest%3A+The+Evolution+of+Cloud+Native+Runtime+Security+CNCF+KubeCon+2026
slides: []
status: parsed
---

# In Falco's Nest: The Evolution of Cloud Native Runtime Security - Iacopo Rozzo, Sysdig; Aldo Lacuku, Kong Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Iacopo Rozzo, Sysdig, Aldo Lacuku, Kong Inc.
- Schedule: https://kccnceu2026.sched.com/event/2EF6W/in-falcos-nest-the-evolution-of-cloud-native-runtime-security-iacopo-rozzo-sysdig-aldo-lacuku-kong-inc
- Busca YouTube: https://www.youtube.com/results?search_query=In+Falco%27s+Nest%3A+The+Evolution+of+Cloud+Native+Runtime+Security+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre In Falco's Nest: The Evolution of Cloud Native Runtime Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6W/in-falcos-nest-the-evolution-of-cloud-native-runtime-security-iacopo-rozzo-sysdig-aldo-lacuku-kong-inc
- YouTube search: https://www.youtube.com/results?search_query=In+Falco%27s+Nest%3A+The+Evolution+of+Cloud+Native+Runtime+Security+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ztt3Wvd-pbI
- YouTube title: In Falco's Nest: The Evolution of Cloud Native Runtime Security - Iacopo Rozzo & Aldo Lacuku
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/in-falcos-nest-the-evolution-of-cloud-native-runtime-security/Ztt3Wvd-pbI.txt
- Transcript chars: 16914
- Keywords: operator, events, allows, basically, config, course, component, security, provide, important, version, artifact, moment, another, having, instance, kernel, information

### Resumo baseado na transcript

Uh we are going to uh discuss about the last evolution in the Falco and its ecosystem and we are also going to present uh what's uh coming next. Before moving to the more technical bits of my presentation, let's take a moment to celebrate a decade of detection. Maybe uh those uh probes as we call them generate events that are sent to the Falco detection engine in user space where a set of reuse is matched uh through those events uh generating alerts. provides a plug-in system that allows you to uh produce your own set of events or to enrich the existing built-in events with additional information collected either uh like uh to to make an example we can collect metadata from container runtime or Kubernetes and uh and this of course brings an important improvement from a performance standpoint because we uh achieved a lighter kernel instrumentation. Um if you have been using uh Kubernetes uh if you have been using Falcon Kubernetes for sure you have been deploying it with Helm chart and it works great uh it deploys Falco it's great for getting started but uh Helm is just a

### Excerpt da transcript

Hello CubeCon. Welcome to the Falcon maintainer track. I'm Jako Parazzo and joining me today is Aldo Lutaku from Kong. Uh we are going to uh discuss about the last evolution in the Falco and its ecosystem and we are also going to present uh what's uh coming next. Before moving to the more technical bits of my presentation, let's take a moment to celebrate a decade of detection. Everything started in uh 2016 when open uh when Falco have been open sourced and in uh 2018 it was donated from CESDIG to the CNCF where it started his maturation process uh that led to the um graduation in 2024 where it reached the highest level of maturity. uh of the uh CNCF program and now we are here in 2026 uh to celebrate one of the industry standard of uh uh runtime security in container native uh ecosystems. uh for the one that could have uh missed us in the last decade, let's take a moment just uh to uh reply a simple question. What exactly is Falco? Well, uh there is an analogy that we often use to explain uh what is Falco in a nutshell.

Uh, Falco can be seen as a security camera as a sec as a security camera in a building can uh detect um suspicious activity. It provides uh deep visibility into your system and into your uh infrastructure and uh allows to detect security threats in real time. uh we it provides a kernel level visibility either through an ebpf instrumentation or a kernel module for uh legacy uh systems. Maybe uh those uh probes as we call them generate events that are sent to the Falco detection engine in user space where a set of reuse is matched uh through those events uh generating alerts. Those reuse are expressed with a simple uh YAML based syntax and of course uh we provide a predefined set of rules but you can tweak them you can provide your own it's highly extensible and the extensibility of Falco doesn't end here because it provides a plug-in system that allows you to uh produce your own set of events or to enrich the existing built-in events with additional information collected either uh like uh to to make an example we can collect metadata from container runtime or Kubernetes and use this information to enrich existing events.

Uh now let's take a look to what has been the new features that have been delivered in the last six months. We had two releases that 0.42 42 uh back in October 2025 and 043 in uh uh January or February uh 2026. So um Falco 042 uh brings a feature called capture recording. It enables uh forensic analysis with Falco. Basica
