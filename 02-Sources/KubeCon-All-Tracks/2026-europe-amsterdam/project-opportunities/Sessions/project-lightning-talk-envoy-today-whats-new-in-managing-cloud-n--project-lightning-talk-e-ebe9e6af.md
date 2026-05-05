---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Karol Szwaj", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyB/project-lightning-talk-envoy-today-whats-new-in-managing-cloud-native-and-ai-workload-traffic-karol-szwaj-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Envoy+Today%3A+What%E2%80%99s+New+In+Managing+Cloud-Native+And+AI+Workload+Traffic%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Envoy Today: What’s New In Managing Cloud-Native And AI Workload Traffic? - Karol Szwaj, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Karol Szwaj, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyB/project-lightning-talk-envoy-today-whats-new-in-managing-cloud-native-and-ai-workload-traffic-karol-szwaj-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Envoy+Today%3A+What%E2%80%99s+New+In+Managing+Cloud-Native+And+AI+Workload+Traffic%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Envoy Today: What’s New In Managing Cloud-Native And AI Workload Traffic?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyB/project-lightning-talk-envoy-today-whats-new-in-managing-cloud-native-and-ai-workload-traffic-karol-szwaj-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Envoy+Today%3A+What%E2%80%99s+New+In+Managing+Cloud-Native+And+AI+Workload+Traffic%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g3CHzGl2zS0
- YouTube title: Project Lightning Talk: Envoy Today: What’s New In Managing Cloud-Native And AI Workl... Karol Szwaj
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-envoy-today-whats-new-in-managing-cloud-native/g3CHzGl2zS0.txt
- Transcript chars: 3653
- Keywords: envoy, gateway, traffic, native, inference, request, thanks, ecosystem, performance, another, control, adoption, proxies, cost, triggers, across, backends, moving

### Resumo baseado na transcript

It's 10 years of envoy project and it all started 10 years ago as a from proxy at a lift company and now it become a one of the key component in the cloud networking cloud native ecosystem. Uh what we have is our core envoy proxy which is of course high performance L7 proxy and it was been foundation for all these years. So if you are keen to learn more about the what we do and what end users are doing with Envoy, I prepared a Luma calendar that you can scan and see. Uh there are many end user specific performance uh details on on how they they using envoy and also we have on Tuesday the celebration of the envoy 10 years uh anniversary and yeah you can meet uh maintainers and contributors in project pavilion.

### Excerpt da transcript

Hello everyone. Thanks for attending this talk. So yeah, this year is something very special. It's 10 years of envoy project and it all started 10 years ago as a from proxy at a lift company and now it become a one of the key component in the cloud networking cloud native ecosystem. So let's take a look how the envoy ecosystem looks now. Uh what we have is our core envoy proxy which is of course high performance L7 proxy and it was been foundation for all these years. It been in every service mesh API gateway and edge edge proxy. Uh another sub project is envoy gateway. It's our Kubernetes control plane. It's Kubernetes native uh gateway and it makes uh adoption of envoy proxies much easier and it runs uh using gateway API and manages many infrastructure envoy proxies and the latest addition is a sub project named envoy AI gateway. It's a data and control plane extension. uh key key key functionality is to manage AML traffic uh using X X processor and internal CRDs for in AI inference. So why AI traffic is so different?

Uh first of all streaming inference calls is long live connections not traditional HTTP request response. Everything is based on the token. So single request can widely cost different amounts depending on the model size and also in aentic workflows we have like one triggers triggers many chains of tools across multiple backends. So that cause that we need to have perod observability. So not just the endpoint is slow but we need to find out which model how many tokens it uses and at what cost. So if we take a look at the road map across all the envoy projects we see that we are moving many features from AI traffic management into the core envoy proxy like uh native protocol support MCP and agent to agent. We have also inference improvements there like request buffering and cross service failover and in another gateway we also added many extensibility points and filter integration that supports uh our use case a gateway and na gateway AI gateway is moving into the API graduation we moved to from alpha to beta and we are planning to reach the our general availability milestones.

Uh also it supports open responses API for open AI standard agents. We provision like token budget and rate limit policies and have a richer telemetry for LM backends. for envoy gateway we also are focusing now on gateway API version 1.5 conformance and that also we have a lot of new load balancing features and if we take a look at the adoption I think it's very impr
