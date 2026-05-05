---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Mauricio Vásquez Bernal", "Alban Crequy", "Microsoft"]
sched_url: https://kccncna2022.sched.com/event/182GW/using-the-ebpf-superpowers-to-generate-kubernetes-security-policies-mauricio-vasquez-bernal-alban-crequy-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Using+the+EBPF+Superpowers+To+Generate+Kubernetes+Security+Policies+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Using the EBPF Superpowers To Generate Kubernetes Security Policies - Mauricio Vásquez Bernal & Alban Crequy, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Mauricio Vásquez Bernal, Alban Crequy, Microsoft
- Schedule: https://kccncna2022.sched.com/event/182GW/using-the-ebpf-superpowers-to-generate-kubernetes-security-policies-mauricio-vasquez-bernal-alban-crequy-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Using+the+EBPF+Superpowers+To+Generate+Kubernetes+Security+Policies+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Using the EBPF Superpowers To Generate Kubernetes Security Policies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GW/using-the-ebpf-superpowers-to-generate-kubernetes-security-policies-mauricio-vasquez-bernal-alban-crequy-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Using+the+EBPF+Superpowers+To+Generate+Kubernetes+Security+Policies+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3dysej_Ydcw
- YouTube title: Using the EBPF Superpowers To Generate Kubernetes Security... Mauricio Vásquez Bernal & Alban Crequy
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/using-the-ebpf-superpowers-to-generate-kubernetes-security-policies/3dysej_Ydcw.txt
- Transcript chars: 31711
- Keywords: network, application, profile, second, policies, security, policy, generate, capabilities, actually, understand, running, define, profiles, traffic, deploy, gadget, difficult

### Resumo baseado na transcript

[Applause] [Music] security policies for our cluster [Music] we are going to show how can we generate those policies by using so many different tools then we'll show you how can audit those policies go under surrounding the cluster and then I will present the different Integrations of this [Music] demonstration like this okay so let's get started security policies we are not that coordinated software is different kind of security of security policies that we can use to make our cluster more secure there are so many of them

### Excerpt da transcript

[Applause] [Music] security policies for our cluster [Music] we are going to show how can we generate those policies by using so many different tools then we'll show you how can audit those policies go under surrounding the cluster and then I will present the different Integrations of this [Music] demonstration like this okay so let's get started security policies we are not that coordinated software is different kind of security of security policies that we can use to make our cluster more secure there are so many of them but in this case we will be concentrated on said come on capabilities there are 10 guys in another [Music] on this presentation today well the problem that we have with the security policies and coordinates is that they are physically continue so in order to configure those security policies we have to understand what our application is doing and this is something that we don't understand all the times for instance if you want to configure a second profile you know we have to know what other system codes are are executed by our application design applies for leadership abilities and in the case of network policies we have to understand how the different represent this is that we are running their communicate to each other also yeah this is something that unfortunately is through many of the times the person that is the finding those policies is not the personalities developing application maybe there is one person that develops everything and then there is another person on the day or maybe a different company also the hospital to give the security policy store on different modifications so this is for this person this is very difficult to understand what are the security policies [Music] because many times that person doesn't have a lot of knowledge about that so yeah in today's presentation I want to present you in a different way to generate those or I will different ways to define those policies so what about the way observe the application if we use some tools of certain application and based on the behavior based on the activity that application is doing we can Define the security policies that we want to use for our application so the idea is actually very simple there are two steps the first one is we have to observe the application we have to understand what the application is doing there are different Technologies for that in this case for sure we are going to use a BPF because it has a very low overhead so when we are observin
