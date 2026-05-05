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
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["Dan Winship", "Surya Seetharaman", "Red Hat", "Nadia Pinaeva", "NVIDIA", "Bowei Du", "Google"]
sched_url: https://kccncna2025.sched.com/event/27Nnu/adminnetworkpolicy-from-alpha-to-beta-and-beyond-dan-winship-surya-seetharaman-red-hat-nadia-pinaeva-nvidia-bowei-du-google
youtube_search_url: https://www.youtube.com/results?search_query=AdminNetworkPolicy%3A+From+Alpha+To+Beta+and+Beyond+CNCF+KubeCon+2025
slides: []
status: parsed
---

# AdminNetworkPolicy: From Alpha To Beta and Beyond - Dan Winship & Surya Seetharaman, Red Hat; Nadia Pinaeva, NVIDIA; Bowei Du, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Dan Winship, Surya Seetharaman, Red Hat, Nadia Pinaeva, NVIDIA, Bowei Du, Google
- Schedule: https://kccncna2025.sched.com/event/27Nnu/adminnetworkpolicy-from-alpha-to-beta-and-beyond-dan-winship-surya-seetharaman-red-hat-nadia-pinaeva-nvidia-bowei-du-google
- Busca YouTube: https://www.youtube.com/results?search_query=AdminNetworkPolicy%3A+From+Alpha+To+Beta+and+Beyond+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre AdminNetworkPolicy: From Alpha To Beta and Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nnu/adminnetworkpolicy-from-alpha-to-beta-and-beyond-dan-winship-surya-seetharaman-red-hat-nadia-pinaeva-nvidia-bowei-du-google
- YouTube search: https://www.youtube.com/results?search_query=AdminNetworkPolicy%3A+From+Alpha+To+Beta+and+Beyond+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SWf3Z3fV0ic
- YouTube title: AdminNetworkPolicy: From Alpha To Beta... Dan Winship, Surya Seetharaman, Nadia Pinaeva & Bowei Du
- Match score: 0.732
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/adminnetworkpolicy-from-alpha-to-beta-and-beyond/SWf3Z3fV0ic.txt
- Transcript chars: 28002
- Keywords: network, policy, baseline, policies, cluster, priority, action, within, changes, basically, traffic, another, admins, evaluated, actually, priorities, default, mentioned

### Resumo baseado na transcript

Welcome to admin network policy from alpha sorry no cluster network policy from alpha to beta and beyond. I work at Red Hat on various uh Kubernetes SIG network stuff including the network policy API group. Our working group also owns and maintains that but that lives in the core Kubernetes repo. so the first adopters were anria CNI inovven kubernetes CNI we've had calico and cubovian implemented since and selium is in progress of implementing it though they might actually end up implementing alpha 2 instead which makes sense we also have our very own cube Um in the case where you have no policies configured this will be the default Kubernetes disposition in which case your traffic will just get accepted. Um assuming that we don't find any problems with the API that B was just talking about, then we're going to declare that to be v1 beta 1 and then cluster network policy will be beta.

### Excerpt da transcript

Welcome to admin network policy from alpha sorry no cluster network policy from alpha to beta and beyond. Um I'm Dan Winship. I work at Red Hat on various uh Kubernetes SIG network stuff including the network policy API group. >> Hey everyone, I'm Sia. I'm also an engineer working at Red Hat and Open Shift networking. I'm leading the network policy API working group. Happy to be here today. Hi, I'm Bowie from Google. I'm also working on network policy. Then >> hi, my name is Nadia. I work at Nvidia on network policy API. >> Cool. So, let's get started with our talk. I'll be doing the past. So, we're just sort of a recap. Nadia and Bu will be doing the present of our of all the cool things that our community has done and Dan will be doing the future. So, starting with we alpha one. How many of you are using admin network policy here? That's two, three. Good. Because we have some breaking API changes. So, it's better if you don't use it in production today. Um, which is basically the takeaway of our talk today.

Uh, some of the use cases. Why do we why did we do admin network policy API and I keep calling it admin network policy and Dan said it's cluster network policy. You'll see why in a moment. It's because I'm talking about we alphab admin network policy and in transition it'll become cluster network policy through the talk. So don't get confused for that. It's the same thing. Uh the first use case is obviously very obvious here that network policies were designed for application developers tenants. We needed something for admins and hence we did the cluster scoped policy API which is the admin network policy API and it was done to help admins be able to do policies to isolate tenant workloads in the cluster which is clusterwide non-overridable by the network policies. Other use cases could be to be able to put policies around the infrastructure services like being able to say that allow all traffic from your monitoring name space to egress always to scrape metrics from your workloads and this cannot be denied by any tenants who own the workloads and the same way to allow always ingress to DNS for example.

And another nice neat use case is the interaction with the network policy itself. So as an admin you can put policies that say I'm delegating the final action of this policy to your to my tenants which means it falls down to the network policies and we'll see this in a moment later. So that's another use case and also we have a guardrail API which let
