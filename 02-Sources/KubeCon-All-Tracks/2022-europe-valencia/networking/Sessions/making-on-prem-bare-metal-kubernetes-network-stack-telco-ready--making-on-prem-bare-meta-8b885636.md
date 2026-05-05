---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Christopher Dziomba", "Marcel Fest", "Deutsche Telekom"]
sched_url: https://kccnceu2022.sched.com/event/ytuA/making-on-prem-bare-metal-kubernetes-network-stack-telco-ready-christopher-dziomba-marcel-fest-deutsche-telekom
youtube_search_url: https://www.youtube.com/results?search_query=Making+On-Prem+Bare-Metal+Kubernetes+Network+Stack+Telco+Ready+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Making On-Prem Bare-Metal Kubernetes Network Stack Telco Ready - Christopher Dziomba & Marcel Fest, Deutsche Telekom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Christopher Dziomba, Marcel Fest, Deutsche Telekom
- Schedule: https://kccnceu2022.sched.com/event/ytuA/making-on-prem-bare-metal-kubernetes-network-stack-telco-ready-christopher-dziomba-marcel-fest-deutsche-telekom
- Busca YouTube: https://www.youtube.com/results?search_query=Making+On-Prem+Bare-Metal+Kubernetes+Network+Stack+Telco+Ready+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Making On-Prem Bare-Metal Kubernetes Network Stack Telco Ready.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuA/making-on-prem-bare-metal-kubernetes-network-stack-telco-ready-christopher-dziomba-marcel-fest-deutsche-telekom
- YouTube search: https://www.youtube.com/results?search_query=Making+On-Prem+Bare-Metal+Kubernetes+Network+Stack+Telco+Ready+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ICvfr0sPSjs
- YouTube title: Making On-Prem Bare-Metal Kubernetes Network Stack Telco Ready - Christopher Dziomba & Marcel Fest
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/making-on-prem-bare-metal-kubernetes-network-stack-telco-ready/ICvfr0sPSjs.txt
- Transcript chars: 17602
- Keywords: network, actually, networks, cluster, traffic, configuration, border, platform, sr-iov, currently, netplan, connectivity, everything, heavily, support, company, native, around

### Resumo baseado na transcript

Yeah, hello and welcome to our talk uh making on-prem bare metal Kubernetes ready. And um yeah, so Christopher and I will guide you of who we are as a company and also what our platform is and in the end there will be a tech savvy thing which we open sourced. Um so we are building an internal GitOps based Kubernetes cluster as a service platform almost exclusively built using open source components and that was exactly the answer I got from one of our uh developers sitting in front here. So our mission is to reliably build Kubernetes clusters with well-defined APIs for our customers. Um but we are kind of like for some parts especially in the networking world um have using uh Kubernetes a bit I would say. So this is kind of how it looks like um in your let's say normal VMware Kubernetes bare metal cluster.

### Excerpt da transcript

Yeah, hello and welcome to our talk uh making on-prem bare metal Kubernetes ready. Uh network stack take already. And um yeah, so Christopher and I will guide you of who we are as a company and also what our platform is and in the end there will be a tech savvy thing which we open sourced. Um so we yeah, guide you through that. Um next thing would be um just our introduction where we are. So we are located under It's not working? Yeah, it's okay. Um so yeah, I'm located in Düsseldorf, uh Germany and I'm very I'm drinking a lot of coffee and um yeah, I'm cycling, doing stuff and I'm also hacking. And yeah, I'm also now since 2 years I'm an amateur snowboarder. And if you want to check me out, um you can also click in the presentation. Uh the things below. And yeah, guide you through you. Christopher. Uh yeah, hi. My name is Christopher Jamba. Um I'm located in Bonn right next to the headquarter of Deutsche Telekom Group. Um I love to cook actually. Um at night I'm a software and hardware tinkerer and in my free time I'm actually a passionate skier.

Um and I'm a DevOps engineer at Deutsche Telekom at the uh Telekom cluster or container as a service team. Um and we are building platform for cloud native uh telco workloads. Yeah, now we come to our organization so you all know DT as a company. Um it's a little bit bigger than most of you think. So we have like T-Mobile US which you all know, I think. They bought uh Sprint and all of that. We're not that. We're also not T-Systems. Um we are in the German subsidiary of the German company which is called Telekom Deutschland GmbH. And um yeah, so we are below that in a subsidiary company. And then we built the platform this shift. So um yeah, so let's go to our company and what we do. Um we have around 33k of cell towers and um yeah, 75% of them are connected by fiber. Um and we want to build in the next years like 1 and 1/2 k new cell towers and also want to cover in 2025 90% of all Germany with 5G. Um then we are also in the broadband and fixed and there we have like 650 km of um a thousand kilometers of fiber.

And we also have a lot of um over over earth uh lines and masts um where we follow telco lines. And we want to um automate our fiber planning for Germany and also we uh want to cover in every household in Germany with fiber connectivity. Yeah, now back to our platform and what we do inside this organization. Um so what what is the shift? I don't know if every everyone of you know. Um so we are building
