---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Marcin Skalski", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcuk/project-lightning-talk-whats-new-in-kuma-advanced-service-mesh-capabilities-marcin-skalski-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%E2%80%99s+New+in+Kuma%3A+Advanced+Service+Mesh+Capabilities+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: What’s New in Kuma: Advanced Service Mesh Capabilities - Marcin Skalski, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Marcin Skalski, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcuk/project-lightning-talk-whats-new-in-kuma-advanced-service-mesh-capabilities-marcin-skalski-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%E2%80%99s+New+in+Kuma%3A+Advanced+Service+Mesh+Capabilities+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What’s New in Kuma: Advanced Service Mesh Capabilities.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcuk/project-lightning-talk-whats-new-in-kuma-advanced-service-mesh-capabilities-marcin-skalski-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%E2%80%99s+New+in+Kuma%3A+Advanced+Service+Mesh+Capabilities+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rRExAhVI1nU
- YouTube title: Project Lightning Talk: What’s New in Kuma: Advanced Service Mesh Capabilities - Marcin Skalski
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-whats-new-in-kuma-advanced-service-mesh-capabil/rRExAhVI1nU.txt
- Transcript chars: 3026
- Keywords: select, mesh, subset, policies, inbound, configuration, workloads, basically, previously, section, traffic, support, default, cubecon, policy, target, selecting, workload

### Resumo baseado na transcript

So it's easy to integrate uh VM workloads into your Kubernetes uh cluster and into your mesh. So in policies uh they are basically main concept of configuration in Kuma. Uh so now we are moving towards rules which is more kubernetes native and uh gateway API similar API.

### Excerpt da transcript

Hello everyone. My name is Martin. I currently work at Kong and I'm ankuma contributor. And today I will show you what's uh new in Kuma. So just a quick recap, Kuma is a envoy based service mesh. It was built with uh multi-tenency and multicluster support in mind. We also support uh by default brownfield uh deployments. So it's easy to integrate uh VM workloads into your Kubernetes uh cluster and into your mesh. So what's actually new since the last CubeCon? We've added new kind data plane in policies. Uh we redesigned inbound policies API. We've added ability to define secrets on zone level. We've added option to exclude policy from sync between zones. And there was couple of stability improvement. So let's take a quick look at the new kind data plane. So in policies uh they are basically main concept of configuration in Kuma. You configure for example timeouts, retries etc using the policies and previously when you wanted to select some subset of workloads in your mesh uh you needed to use mesh subset uh kind in the target ref selector and you were selecting workload by tax.

Those stacks were taken from uh data plane inbounds which could be problematic to understand and uh it wasn't that easy to use. So now we've introduced new kind data plane when you where you are selecting the real resource data plane. Every workload has its own data plane and on Kubernetes we are basically building data planes from pots and we the data planes have the same labels as pots. So it's easy to select your workloads by labels. Also with addition to section name, you can now simply select single inbound uh to apply the configuration to which comes in handy with our new uh inbound uh configuration API. So previously we were using the from section with uh target ref uh that selected the subset. traffic that should be configured and in most policies you are only able to select mesh uh with exception of traffic permission where you will able to select some subset of uh clients to which the policy should apply. Uh so now we are moving towards rules which is more kubernetes native and uh gateway API similar API.

uh right now there is only the default uh field with the configuration itself but with the addition of section name as I mentioned previously you can select the single inbound and apply configuration to that inbound um and we will be adding the more possibilities to this app with the matches field uh where you will be able to select subset of traffic for example based on
