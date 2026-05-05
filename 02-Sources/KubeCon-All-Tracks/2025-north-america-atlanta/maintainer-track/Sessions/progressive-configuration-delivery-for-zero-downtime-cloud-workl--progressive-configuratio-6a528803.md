---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Yuxing Yuan", "Alibaba Cloud", "Hao Wu", "Independent"]
sched_url: https://kccncna2025.sched.com/event/27Nn8/progressive-configuration-delivery-for-zero-downtime-cloud-workloads-yuxing-yuan-alibaba-cloud-hao-wu-independent
youtube_search_url: https://www.youtube.com/results?search_query=Progressive+Configuration+Delivery+for+Zero-Downtime+Cloud+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Progressive Configuration Delivery for Zero-Downtime Cloud Workloads - Yuxing Yuan, Alibaba Cloud & Hao Wu, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Yuxing Yuan, Alibaba Cloud, Hao Wu, Independent
- Schedule: https://kccncna2025.sched.com/event/27Nn8/progressive-configuration-delivery-for-zero-downtime-cloud-workloads-yuxing-yuan-alibaba-cloud-hao-wu-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Progressive+Configuration+Delivery+for+Zero-Downtime+Cloud+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Progressive Configuration Delivery for Zero-Downtime Cloud Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nn8/progressive-configuration-delivery-for-zero-downtime-cloud-workloads-yuxing-yuan-alibaba-cloud-hao-wu-independent
- YouTube search: https://www.youtube.com/results?search_query=Progressive+Configuration+Delivery+for+Zero-Downtime+Cloud+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vozl2HAiMNU
- YouTube title: Progressive Configuration Delivery for Zero-Downtime Cloud Workloads - Yuxing Yuan & Hao Wu
- Match score: 0.957
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/progressive-configuration-delivery-for-zero-downtime-cloud-workloads/vozl2HAiMNU.txt
- Transcript chars: 13927
- Keywords: configuration, version, config, versions, cruise, containers, updates, update, volume, reload, management, container, controller, control, revision, target, delivery, future

### Resumo baseado na transcript

I'm excited to share with you today a re innovation approach to configuration management that addresses one of the most critical changing challenges in cloud native environments achieving zero downtime configuration updates. My name is I'm one of the maintainers of open cruise as well as a software senior software engineer from Alibaba and my partner Hawu is a independent contributor in open groups. On July 13th, 2024, AWS uh express a large scale outstage tracked back to uh configuration issues. Just 11 days later on June 26 uh Alipa clouds CDN experience not scale failure from similar configuration problems. Uh this design was refined through real world scenarios for end users who faced these excellent challenging study. We welcome contributors to join us in designing and incributing productive production ready failure futures that solve real problems.

### Excerpt da transcript

Good afternoon everyone. I'm excited to share with you today a re innovation approach to configuration management that addresses one of the most critical changing challenges in cloud native environments achieving zero downtime configuration updates. My name is I'm one of the maintainers of open cruise as well as a software senior software engineer from Alibaba and my partner Hawu is a independent contributor in open groups. Today we will employ three key areas. What's project open groups? The innovative config map website mapate future how it works in practice and our vision for the future. This is the first time for open cruise showing in North American. Let me started by introducing the project first. Open Cruise is a CNCF incubating project that has been adopted by hundreds of companies worldwide. What make it special? It's it's focused on application automation with two standout features that has driven its adoption. That's uh [sighs] in place updates and set management. The project addresses real world operational challenges that naive uh ladies doesn't handle elegant companies who choose open groups because it solve problems they face daily in product environments.

Now let me show you one of the open cruise most powerful capabilities that relate to our topic today. Sycas is a game changer for sata n life n life n life n life n life n life n life n life n life n life n cycle management. It decoups the side car container life cycle from your main application containers allowing you to roll updates set without disrupting your main container. This how it works. The set controller use admission web hooks to admissionally inject set containers into selected ports during correction. But it goes beyond simple injection. It enables in place silicon image updates, volume mountings and the life cycle management. This is particularly valuable for operational tools like uh mo moniting agent login collectors or service match side cars essentially a stateful uh side car that needs independent management from your main application. It can be seen that the the car is actually the config uh loading motions we expected. It can be decoupled from image changes and also control the uh calorie release ratio to achieve progressing development.

It it's possible to employ employment uh config map loading measurities based on celica. This story uh begins at KubeCon Hong Kong 2024. During that conference, I present insight on new opportunities for open cruise especially highl
