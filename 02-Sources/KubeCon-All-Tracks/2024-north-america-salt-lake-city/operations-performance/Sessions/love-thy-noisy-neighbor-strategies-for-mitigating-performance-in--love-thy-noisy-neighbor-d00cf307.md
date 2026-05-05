---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Jonathan Perry", "PerfPod"]
sched_url: https://kccncna2024.sched.com/event/1i7qF/love-thy-noisy-neighbor-strategies-for-mitigating-performance-interference-in-cloud-native-systems-jonathan-perry-perfpod
youtube_search_url: https://www.youtube.com/results?search_query=Love+thy+%28Noisy%29+Neighbor%3A+Strategies+for+Mitigating+Performance+Interference+in+Cloud-Native+Systems+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Love thy (Noisy) Neighbor: Strategies for Mitigating Performance Interference in Cloud-Native Systems - Jonathan Perry, PerfPod

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Jonathan Perry, PerfPod
- Schedule: https://kccncna2024.sched.com/event/1i7qF/love-thy-noisy-neighbor-strategies-for-mitigating-performance-interference-in-cloud-native-systems-jonathan-perry-perfpod
- Busca YouTube: https://www.youtube.com/results?search_query=Love+thy+%28Noisy%29+Neighbor%3A+Strategies+for+Mitigating+Performance+Interference+in+Cloud-Native+Systems+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Love thy (Noisy) Neighbor: Strategies for Mitigating Performance Interference in Cloud-Native Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qF/love-thy-noisy-neighbor-strategies-for-mitigating-performance-interference-in-cloud-native-systems-jonathan-perry-perfpod
- YouTube search: https://www.youtube.com/results?search_query=Love+thy+%28Noisy%29+Neighbor%3A+Strategies+for+Mitigating+Performance+Interference+in+Cloud-Native+Systems+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VsYp_Z1PvOc
- YouTube title: Love thy (Noisy) Neighbor: Strategies for Mitigating Performance Interference in Cloud-N... J. Perry
- Match score: 0.991
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/love-thy-noisy-neighbor-strategies-for-mitigating-performance-interfer/VsYp_Z1PvOc.txt
- Transcript chars: 30653
- Keywords: memory, neighbor, latency, systems, workloads, bandwidth, application, question, cluster, running, utilization, access, control, resources, cycles, applications, workload, performance

### Resumo baseado na transcript

hi everybody uh welcome uh to this talk about memory Noisy Neighbor what if I told you that a small group of Engineers got together and developed this secret capability that allowed them to run their workloads 20 to 50% more efficiently on less hardware and get you know significantly reduced tail latency four times five times 13 times that would sound fantastic right how could we not know about this well it turns out this capability seems to actually exist uh but the development has not been uh done

### Excerpt da transcript

hi everybody uh welcome uh to this talk about memory Noisy Neighbor what if I told you that a small group of Engineers got together and developed this secret capability that allowed them to run their workloads 20 to 50% more efficiently on less hardware and get you know significantly reduced tail latency four times five times 13 times that would sound fantastic right how could we not know about this well it turns out this capability seems to actually exist uh but the development has not been uh done in secret uh there have been dozens of papers over the last decades from hyperscalers from well-known uh research universities showing this capability so in this talk I'd like to give an overview of what uh I believe the the kind of knowledge there is out there uh the reason I'm giving this talk is because I think that there's enough knowledge out there that this we can make this into practical systems that can generalize across the kubernetes ecosystem uh you might know one of uh these surveys uh this one was published by dad doog in 2023 showing that many of the containers that we run in systems today uh use a lot less than the CPU that we request for them so I want to run a similar survey here today and I'm going to ask y'all to please raise your hands if you know the average uh CPU utilization in a production kubernetes cluster hands up all right and then leave your hands up uh if the cluster utilization is above 20% okay I guess a third lowered their hand above 30% yeah uh I guess another third lower there above 40 anybody has a cluster with above 50% CPU utilization with user facing traffic wow so good on you well if if uh you said between 20 and 40% you're in very good company uh some of the largest companies on the planets uh with large engineering teams capable of optimizing their deployments have public average CPU utilization between 20 and 40% but what seems to have happened in the last few years is that some companies have been able to increase their efficiency quite substantially uh Google was around 35% CPU utilization in 2011 and increased to 50% the reported CPU utilization in 2019 so what happened how did they manage to increase their efficiency so substantially well reading published work I found uh at least two contributors to that efficiency gain so one of them is advancement in vertical pod autoscaling and there's a very interesting paper published by Google called autopilot in eurosis 2020 and this is not the gke autopilot if you're famil
