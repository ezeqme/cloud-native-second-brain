---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Eduardo Arango Gutierrez", "NVIDIA", "Chaoyi Huang", "Huawei Technology Co.", "Ltd"]
sched_url: https://kccnceu2026.sched.com/event/2CW7r/k8s-sigs-nfd-x-sylva-declarative-image-to-node-compatibility-for-telco-clouds-eduardo-arango-gutierrez-nvidia-chaoyi-huang-huawei-technology-co-ltd
youtube_search_url: https://www.youtube.com/results?search_query=K8s-sigs+NFD+%C3%97+SYLVA%3A+Declarative+Image-to-Node+Compatibility+for+Telco+Clouds.+CNCF+KubeCon+2026
slides: []
status: parsed
---

# K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibility for Telco Clouds. - Eduardo Arango Gutierrez, NVIDIA & Chaoyi Huang, Huawei Technology Co., Ltd

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eduardo Arango Gutierrez, NVIDIA, Chaoyi Huang, Huawei Technology Co., Ltd
- Schedule: https://kccnceu2026.sched.com/event/2CW7r/k8s-sigs-nfd-x-sylva-declarative-image-to-node-compatibility-for-telco-clouds-eduardo-arango-gutierrez-nvidia-chaoyi-huang-huawei-technology-co-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=K8s-sigs+NFD+%C3%97+SYLVA%3A+Declarative+Image-to-Node+Compatibility+for+Telco+Clouds.+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibility for Telco Clouds..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7r/k8s-sigs-nfd-x-sylva-declarative-image-to-node-compatibility-for-telco-clouds-eduardo-arango-gutierrez-nvidia-chaoyi-huang-huawei-technology-co-ltd
- YouTube search: https://www.youtube.com/results?search_query=K8s-sigs+NFD+%C3%97+SYLVA%3A+Declarative+Image-to-Node+Compatibility+for+Telco+Clouds.+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GPnMIIfrmi0
- YouTube title: K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibi... Eduardo Arango Gutierrez & Chaoyi Huang
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/k8s-sigs-nfd-sylva-declarative-image-to-node-compatibility-for-telco-c/GPnMIIfrmi0.txt
- Transcript chars: 24242
- Keywords: feature, application, container, cluster, specific, compatibility, hardware, artifact, registry, information, telecom, network, multiple, foundation, containers, images, groups, scheduleuler

### Resumo baseado na transcript

Hey everyone, uh thank you for being here and for everyone watching this uh on your homes in YouTube. Let's make it quick, but also uh I'm super super excited to give this talk because this is a project that I really care about. and is HPC in HPC mostly because of the procurement process that happens within big institutions they end up having very clusters right so it's not a big cluster with a a singular architecture but they have uh chips from 10 years ago that are So this whole uh talk today is about how can we address this problem of having very eterogeneous architectures within uh or helping with Kubernetes. So the cubernetes community got together to help the Linux foundation sila which is another foundation within the Linux foundation and they had this big problem of having very heterogeneous hardware deployments. So representing the Kubernetes side it's me uh Eduardo I work at Nvidia mostly all things Kubernetes and you okay my name is Joe Ham and uh working for the Huawei and contributor to uh uh Kubernetes CNCF and SA and uh uh let me talk about uh Oh, you're the next >> challenge first.

### Excerpt da transcript

Hey everyone, uh thank you for being here and for everyone watching this uh on your homes in YouTube. Hi, welcome to this talk and let's bring us home, right? Like this is the last session at CUCOM. Let's make it fun. Let's make it quick, but also uh I'm super super excited to give this talk because this is a project that I really care about. I've been trying to have the NFD awards in a slide at coupon for years. Uh many many thank you to Marcus from Intel who is not here with me and many thank you to all the other NFD maintainers that have taken this project over the years. Uh so this today is uh integration that we have done with NFD and the Silva Foundation which we will talk later on on solving problems from sik cubernetes on real life. So this talk is about a real end user that uh they had a problem and we as a community got together and created solutions within a sik Kubernetes project to help them move forward and the problem is a very interesting problem and a very old school containers problem.

We have the promise on the clouds that once you build a container you can ship it everywhere and it will run everywhere. Well, there are some corner cases and not that corner like Telos are a big customer not corner case where they have tons of different SOC's right like they at your home every rout like Wi-Fi router has a different chip and if we go to Telos then every Wi-Fi router is different every antenna is different every 5G antenna has different SOC's and chipping containers there is very complicated But the second use case that also there are a lot of contributors to this effort is university is academia and is HPC in HPC mostly because of the procurement process that happens within big institutions they end up having very clusters right so it's not a big cluster with a a singular architecture but they have uh chips from 10 years ago that are still running because magic exist all the way to new chips and shipping one container to that academic cluster can lead to some errors. So this whole uh talk today is about how can we address this problem of having very eterogeneous architectures within uh or helping with Kubernetes.

So we are collaborating. So the cubernetes community got together to help the Linux foundation sila which is another foundation within the Linux foundation and they had this big problem of having very heterogeneous hardware deployments. So representing the Kubernetes side it's me uh Eduardo I work at Nvidia mostly all things Kube
