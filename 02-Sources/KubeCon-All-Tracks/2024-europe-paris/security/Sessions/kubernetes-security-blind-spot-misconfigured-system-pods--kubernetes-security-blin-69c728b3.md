---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["AI ML", "Security", "Networking", "Kubernetes Core"]
speakers: ["Shaul Ben Hai", "Palo Alto Networks"]
sched_url: https://kccnceu2024.sched.com/event/1YeQw/kubernetes-security-blind-spot-misconfigured-system-pods-shaul-ben-hai-palo-alto-networks
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Security+Blind+Spot%3A+Misconfigured+System+Pods+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Security Blind Spot: Misconfigured System Pods - Shaul Ben Hai, Palo Alto Networks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Shaul Ben Hai, Palo Alto Networks
- Schedule: https://kccnceu2024.sched.com/event/1YeQw/kubernetes-security-blind-spot-misconfigured-system-pods-shaul-ben-hai-palo-alto-networks
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Security+Blind+Spot%3A+Misconfigured+System+Pods+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Security Blind Spot: Misconfigured System Pods.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQw/kubernetes-security-blind-spot-misconfigured-system-pods-shaul-ben-hai-palo-alto-networks
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Security+Blind+Spot%3A+Misconfigured+System+Pods+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5scIQkclPfk
- YouTube title: Kubernetes Security Blind Spot: Misconfigured System Pods - Shaul Ben Hai, Palo Alto Networks
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-security-blind-spot-misconfigured-system-pods/5scIQkclPfk.txt
- Transcript chars: 15642
- Keywords: cluster, privileges, container, attack, security, misconfiguration, access, attacker, escape, permission, fluent, network, second, create, vulnerability, critical, configuration, within

### Resumo baseado na transcript

I'm Shaul benai and today we're going to talk about kubernetes blind spot the Unseen threat of system pods so a little bit about myself I'm a security researcher in Prisma cloud in falto network and I'm doing security research and threat hunting in Cloud ecosystem and I'm also dealing with some open source research and vulnerability management so our lineup topic for today we will start to talk about container escape and kubernetes second stage attack we will explore this concept and understand why they are so critical for

### Excerpt da transcript

I'm Shaul benai and today we're going to talk about kubernetes blind spot the Unseen threat of system pods so a little bit about myself I'm a security researcher in Prisma cloud in falto network and I'm doing security research and threat hunting in Cloud ecosystem and I'm also dealing with some open source research and vulnerability management so our lineup topic for today we will start to talk about container escape and kubernetes second stage attack we will explore this concept and understand why they are so critical for cloud security then we'll try to understand better system pods about their function and privileges following that we will talk about the system pods Paradox privilege against risk and the unique security challenge around it moving on to to real world misconfiguration and vulnerability we will examine real world case study combining two default misconfiguration in gke and then we we wrap it all to some key recommendation and best practices so ever since container came into our life we've been hearing more and more about container escape and the question that we need to ask ourself is do container actually contain there is no doubt that container are great for packaging and deploying software this is the reason why we are all use them but they are weak security boundary mostly because of the shared kernel and container Escape will probably continue to happen and it's here to stay even because vulnerability or even because misconfiguration the most known one is Village container with access to to the host so we must understand what is the impact what is the impact of container escape and the obvious impact in kubernetes at least is a compromise node an attacker escape from one container or one pod and Now to control over the entire node but let's imagine that our an attacker is an ambitious one and he might be not satisfied with only single compromise node he might want to take over the entire cluster may maybe for more business logic or more Computer Resources for crypto mining for example so one of the question that we will try to answer today is If a scenario of a single container esape could be escalated to full class and what is the part of system pods in this kind of scenario so before we will dive in we need to understand a little bit better what is exactly second stage attack in kubernetes so of course attacker gains some initial access to our environment and now we want to escalate these privileges or move literally so our starting
