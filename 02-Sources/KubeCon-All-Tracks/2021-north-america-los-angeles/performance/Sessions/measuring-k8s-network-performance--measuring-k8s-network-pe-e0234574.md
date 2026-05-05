---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Performance"
themes: ["Networking", "SRE Reliability"]
speakers: ["Kornilios Kourtis", "Isovalent"]
sched_url: https://kccncna2021.sched.com/event/lV5y/measuring-k8s-network-performance-kornilios-kourtis-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Measuring+K8s+Network+Performance+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Measuring K8s Network Performance - Kornilios Kourtis, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Performance]]
- Temas: [[Networking]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Kornilios Kourtis, Isovalent
- Schedule: https://kccncna2021.sched.com/event/lV5y/measuring-k8s-network-performance-kornilios-kourtis-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Measuring+K8s+Network+Performance+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Measuring K8s Network Performance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5y/measuring-k8s-network-performance-kornilios-kourtis-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Measuring+K8s+Network+Performance+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EaoAJ0-Qsc8
- YouTube title: Measuring K8s Network Performance - Kornilios Kourtis, Isovalent
- Match score: 0.782
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/measuring-k8s-network-performance/EaoAJ0-Qsc8.txt
- Transcript chars: 21311
- Keywords: performance, network, latency, multiple, evaluation, useful, hardware, experiment, specific, workload, includes, optimizations, another, important, actually, software, applications, benchmarks

### Resumo baseado na transcript

hello i'm cornelius and i will be talking about measuring magnetic network performance i am a software engineer at suvelant where i work on cilium which is a network observability and security platform for container environments such as kubernetes we implement celium by extensively using ebpf but this talk is not about celium or ebpf in the ceiling team we spend a lot of time evaluating network performance identifying bottlenecks and fixing them so in this talk i would like to offer some practical advice for practitioners who also want

### Excerpt da transcript

hello i'm cornelius and i will be talking about measuring magnetic network performance i am a software engineer at suvelant where i work on cilium which is a network observability and security platform for container environments such as kubernetes we implement celium by extensively using ebpf but this talk is not about celium or ebpf in the ceiling team we spend a lot of time evaluating network performance identifying bottlenecks and fixing them so in this talk i would like to offer some practical advice for practitioners who also want to evaluate the network performance of the kubernetes cluster and i will start by discussing potential motivations for doing so performance valuation is really useful for asserting or disproving assumptions for example it can be used to verify that using more expensive machines with better network cards will actually improve application performance and going even further it can also check or verify that the benefit the performance benefit that applications will get will actually justify the additional cost of acquiring this new hardware on a related topic evaluation can be used to offer concrete and objective arguments for making technical choices for example if an organization wants to select a cloud provider and data performance is a factor in this decision evaluation can be used to actually quantify the different tradeoffs between the different cloud providers and also um try to do the experiment considering what are the unique needs or workloads for this specific organization and finally evaluation can help with better understanding your platform for example if there are applications that exhibit random delays in communication you can use evaluation to try to figure out whether this is a network problem or something else is going on and generally speaking playing with benchmarks it's a great way to understand your infrastructure the problem is that benchmarking is a really hard process and kubernetes network benchmarking even more so and the reason for that is that there are many different layers involved in making for example two kubernetes boards talk to each other first there is a network itself which in many cases might have an unknown topology and also it might be used by multiple different users having different workloads and this means that performance might vary between different times or even depending on where the machine is located furthermore uh the nik or the network interface card which is the part the hard
