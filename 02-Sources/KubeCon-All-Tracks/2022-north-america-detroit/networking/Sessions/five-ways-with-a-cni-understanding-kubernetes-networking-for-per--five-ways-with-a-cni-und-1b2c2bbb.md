---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Networking"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Stig Telfer", "StackHPC Ltd", "Erez Cohen", "Nvidia"]
sched_url: https://kccncna2022.sched.com/event/182D8/five-ways-with-a-cni-understanding-kubernetes-networking-for-performance-intensive-workloads-stig-telfer-stackhpc-ltd-erez-cohen-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Five+Ways+With+a+CNI%3A+Understanding+Kubernetes+Networking+For+Performance-Intensive+Workloads+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Five Ways With a CNI: Understanding Kubernetes Networking For Performance-Intensive Workloads - Stig Telfer, StackHPC Ltd & Erez Cohen, Nvidia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Stig Telfer, StackHPC Ltd, Erez Cohen, Nvidia
- Schedule: https://kccncna2022.sched.com/event/182D8/five-ways-with-a-cni-understanding-kubernetes-networking-for-performance-intensive-workloads-stig-telfer-stackhpc-ltd-erez-cohen-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Five+Ways+With+a+CNI%3A+Understanding+Kubernetes+Networking+For+Performance-Intensive+Workloads+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Five Ways With a CNI: Understanding Kubernetes Networking For Performance-Intensive Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182D8/five-ways-with-a-cni-understanding-kubernetes-networking-for-performance-intensive-workloads-stig-telfer-stackhpc-ltd-erez-cohen-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Five+Ways+With+a+CNI%3A+Understanding+Kubernetes+Networking+For+Performance-Intensive+Workloads+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m6o-KYF_s5E
- YouTube title: Five Ways With a CNI: Understanding Kubernetes Networking For Performance..-Stig Telfer & Erez Cohen
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/five-ways-with-a-cni-understanding-kubernetes-networking-for-performan/m6o-KYF_s5E.txt
- Transcript chars: 27164
- Keywords: performance, networking, network, calico, running, hardware, accelerated, bandwidth, latency, application, kernel, configuration, results, packet, virtual, second, offloads, openstack

### Resumo baseado na transcript

hello everyone today we're talking five ways for the cni I'm stick Telfer I'm CTO of a technical consultancy business called stack HPC we specialize in high performance Cloud infrastructure and platforms for scientific computing I'm responsible for cloud networking at Nvidia in this talk we will discuss and compare some of the most common kubernetes networking configurations for performance intensive workloads high performance Computing or HPC is a field of computer science that solves complex problems such as fluid dynamics for aircraft design for example large-scale weather forecast or servers are quite high-end for the performance benchmarking we're running HP DL 380 gen10 with 8380 CPUs uh two pneumas each one of 40 core so overall 80 cores and half a terabyte of RAM and those devices are and those servers running in video connecting 6dx with two ports of 100 gigabit each on the OS we're running Ubuntu 2004 with latest kernel and then video offered for latest uh networking drivers kubernetes version is 1.23.7 and we deployed with Cube spray and the port is running Ubuntu again

### Excerpt da transcript

hello everyone today we're talking five ways for the cni I'm stick Telfer I'm CTO of a technical consultancy business called stack HPC we specialize in high performance Cloud infrastructure and platforms for scientific computing I'm responsible for cloud networking at Nvidia in this talk we will discuss and compare some of the most common kubernetes networking configurations for performance intensive workloads high performance Computing or HPC is a field of computer science that solves complex problems such as fluid dynamics for aircraft design for example large-scale weather forecast or drug Discovery through the use of large-scale compute simulations HPC is one of the most compute Network and storage intensive workloads Technologies developed for HPC often make their way to more standout data center applications another example of compute intensive applications are artificial intelligence or AI AI is probably the greatest revolution of our time it allows computers to solve problems that only few years ago seemed impossible AI can create images and text from Human description translate languages recommend specific items from wealth of options and even write code AI is very common these days and used in many web services and other common applications both Ai and HPC are compute intensive and they typically cannot run on a single server they require a cluster of servers and run as a distributed application when we're running application in that fashion networking become a critical element for the proper execution of the application when we're looking at the natural consideration the first and foremost is throughput or bandwidth and here we would like to have as much as we can today we're running at 100 Gig and going forward we're already deploying 400 gigabit per second but latency and the predictability of latency is is as important for those kind of workloads and obviously we would like to have low and predictable latency across all packet types when we're running a lot of networking the CPU is uh very busy with the network itself and consumes quite a lot of core CPU cores um we would like obviously to free up those CPU for running the application itself and therefore we're looking for CPU off-road capabilities so that the networking will be handled by the neck and not by the CPU and lastly in many of those application environments gpus are in play and we would like to make sure that not only the CPU can access the network properly but also the GPU Techno
