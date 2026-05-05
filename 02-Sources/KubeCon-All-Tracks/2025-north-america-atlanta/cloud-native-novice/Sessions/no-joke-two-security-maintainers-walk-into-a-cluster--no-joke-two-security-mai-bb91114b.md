---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Novice"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Jackie Maertens", "Nilekh Chaudhari", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27FWr/no-joke-two-security-maintainers-walk-into-a-cluster-jackie-maertens-nilekh-chaudhari-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=No+Joke%3A+Two+Security+Maintainers+Walk+Into+a+Cluster+CNCF+KubeCon+2025
slides: []
status: parsed
---

# No Joke: Two Security Maintainers Walk Into a Cluster - Jackie Maertens & Nilekh Chaudhari, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Jackie Maertens, Nilekh Chaudhari, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27FWr/no-joke-two-security-maintainers-walk-into-a-cluster-jackie-maertens-nilekh-chaudhari-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=No+Joke%3A+Two+Security+Maintainers+Walk+Into+a+Cluster+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre No Joke: Two Security Maintainers Walk Into a Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWr/no-joke-two-security-maintainers-walk-into-a-cluster-jackie-maertens-nilekh-chaudhari-microsoft
- YouTube search: https://www.youtube.com/results?search_query=No+Joke%3A+Two+Security+Maintainers+Walk+Into+a+Cluster+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HwS5UKD8dVM
- YouTube title: No Joke: Two Security Maintainers Walk Into a Cluster - Jackie Maertens & Nilekh Chaudhari
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/no-joke-two-security-maintainers-walk-into-a-cluster/HwS5UKD8dVM.txt
- Transcript chars: 28302
- Keywords: access, secrets, security, cluster, secret, encryption, network, essentially, policy, policies, whenever, common, create, external, encrypted, permissions, vulnerabilities, privilege

### Resumo baseado na transcript

Uh, welcome to our talk where, no joke, uh, two security maintainers are going to walk you through a cluster. I'm an ISTO security maintainer and co-lead of ISTO's product security working group. With that in mind, uh, in order to make the progress towards our security goals, we'll be explaining and inspect inspecting several essential Kubernetes components. So I'll take you through a journey well where where I will explain the arbback encryption at red rest secrets management and then Jackie will take us through the network policies port security standards and image vulnerabilities. So uh at the end of this at the end of this talk you will know you know where to start designing uh the security for your cluster or uh probably how to inspect and make sure that everything runs just fine. It will tell you uh what uh who can access what data inside your cluster and then uh you you can also think of it as an analogous to having security batches security batch which can grant you an access to different levels uh into a building.

### Excerpt da transcript

Okay. So, welcome everyone. Uh, welcome to our talk where, no joke, uh, two security maintainers are going to walk you through a cluster. Okay. So, my name is Jackie Martins. I'm a senior software engineer at Microsoft. I'm on the Azure Kubernetes upstream team. I'm an ISTO security maintainer and co-lead of ISTO's product security working group. >> Hi everyone. Uh, I'm Nilik. I'm a senior software engineer at Microsoft working on traffic team in Azure Kubernetes service or AKS. Uh I've been contributing to CNCF project since 2021 and have contributed to upstream kubernetes through cigot and sig API machinery and uh currently I am focused on uh networking and so I'm contributing to upstream service mesh project. Okay. So uh we wanted to set some security goals for our talks and I'm pretty sure you all wouldn't be here if you don't care about security or data at rest etc etc for your cluster. So with that in mind as your cluster inspector we are here to define uh our security goals and the Kubernetes components and tools that we will use in order to achieve those uh these goals.

So uh one of the thing that we wanted to sort of explicitly mention here is the the principle of list privileges and what it dictates that uh users or workloads don't have uh more access than what they should you know so the protecting the host isolating uh environment helps us prevent attackers from moving laterally uh if there is a if there is a bridge u safeguarding sensitive information keeps uh keeping the customer data safe uh we wanted to ensure that we have uh we have those guards in in place. Uh we wanted to minimize the open doors, remove unnecessary permissions and exposures. So we make it much harder for the attackers to sort of steal all of your data. And uh ultimately with these practices uh we wanted to make sure that your cluster is resilient, your data is safe and then essentially we are running our business safely and smoothly. With that in mind, uh, in order to make the progress towards our security goals, we'll be explaining and inspect inspecting several essential Kubernetes components.

This is not an exhaustive list, but this is definitely where you can get started and then uh you can build on top of that. So I'll take you through a journey well where where I will explain the arbback encryption at red rest secrets management and then Jackie will take us through the network policies port security standards and image vulnerabilities. So we are covering a lot I
