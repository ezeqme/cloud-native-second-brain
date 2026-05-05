---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Yury Tsarev", "Founder And Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5L/project-lightning-talk-introducing-k8gb-kubernetes-native-global-load-balancing-made-simple-yury-tsarev-founder-and-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Introducing+k8gb%3A+Kubernetes+Native+Global+Load+Balancing+Made+Simple+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Introducing k8gb: Kubernetes Native Global Load Balancing Made Simple - Yury Tsarev, Founder And Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Yury Tsarev, Founder And Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5L/project-lightning-talk-introducing-k8gb-kubernetes-native-global-load-balancing-made-simple-yury-tsarev-founder-and-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Introducing+k8gb%3A+Kubernetes+Native+Global+Load+Balancing+Made+Simple+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Introducing k8gb: Kubernetes Native Global Load Balancing Made Simple.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5L/project-lightning-talk-introducing-k8gb-kubernetes-native-global-load-balancing-made-simple-yury-tsarev-founder-and-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Introducing+k8gb%3A+Kubernetes+Native+Global+Load+Balancing+Made+Simple+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4rpPTWIV5DA
- YouTube title: Project Lightning Talk: Introducing k8gb: Kubernetes Native Global Load Balancing Mad... Yury Tsarev
- Match score: 0.983
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-introducing-k8gb-kubernetes-native-global-load/4rpPTWIV5DA.txt
- Transcript chars: 6831
- Keywords: global, traffic, strategy, balancing, workloads, enable, workload, provide, cluster, across, distributed, clusters, resource, recently, delegation, integration, deploy, globally

### Resumo baseado na transcript

So the idea is uh that you can um deploy workloads across a globally distributed Kubernetes clusters and KGB will enable a global traffic uh management for you in a seamless reliable and declarative manner. The main uh properties of the project is to enable this workload global workload resilience for Kubernetes um clusters and applications on top of them across global regions u clouds and any uh domain failures that you want to deploy your workloads to. So whenever you have a problematic workload in one cluster uh your global traffic will be automatically steered to the healthy locations. So if you look at the architecture diagram uh here is just two clusters we support two and more obviously. Um uh we are two times finalist of CNN CF security slam that increase the security posture of the project heavily. contributing there uh over a little bit more community metrics like more than 1,000 stars uh 37 contributors 37 releases and we recently switched to quarterly cadence so you will get all KGB updates in a reasonable time frames uh if you like what I

### Excerpt da transcript

Hello everyone. Let's chat about global load balancing. My name is Yuri. I am founder and maintainer maintainer of the project called KGB. And KGB stands for Kubernetes global balancer. So the idea is uh that you can um deploy workloads across a globally distributed Kubernetes clusters and KGB will enable a global traffic uh management for you in a seamless reliable and declarative manner. The main uh properties of the project is to enable this workload global workload resilience for Kubernetes um clusters and applications on top of them across global regions u clouds and any uh domain failures that you want to deploy your workloads to. We provide a seamless traffic management uh and utilizing uh multiple global load balancing strategies. And one of the core principles is that we do not have any single point of failure. So there is no control C cluster. We do not have any cluster that uh will affect your workloads when something is down. Everything is nicely distributed next to your workloads and everything is controlled with a single custom resource.

We have a pretty nice community adoption and uh several enterprises are trusting KGB in production as a adopters of their project. So if you talk about the functionality the main core of it is actually load balancing strategies and u visa round robbing for example you can spread the traffic roughly equally across the globally distributed clusters. With a weighted version of it you have a more control and you can pin the percentages across the geographical locations. With a failover one is probably one of our main most popular strategies. you can steer the traffic deterministically in automated manner. So whenever you have a problematic workload in one cluster uh your global traffic will be automatically steered to the healthy locations. Uh so with the strategy um companies frequently you doing interesting stuff like a global blue green disaster recovery maintenance and a global region. So you're basically ready for mass regional failure like recently happened with AWS for example. And the last but not least is GIP strategy.

It's probably most sophisticated one from an implementation standpoint. It's a geographical proximity. So you have a GP database and your client, you'll be steered to the closest uh uh cluster in a specific geographical location. uh main core components that we are shipping together with the project is embedded cord DNS that's actually uh serves the DNS request and provides this dynamica
