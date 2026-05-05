---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Performance"
themes: ["SRE Reliability"]
speakers: ["Swati Sehgal", "Red Hat", "Marlow Weston", "Intel"]
sched_url: https://kccnceu2022.sched.com/event/ytlD/this-is-the-way-a-crash-course-on-the-intricacies-of-managing-cpus-in-k8s-swati-sehgal-red-hat-marlow-weston-intel
youtube_search_url: https://www.youtube.com/results?search_query=This+is+The+Way%3A+A+Crash+Course+on+the+Intricacies+of+Managing+CPUs+in+K8s+CNCF+KubeCon+2022
slides: []
status: parsed
---

# This is The Way: A Crash Course on the Intricacies of Managing CPUs in K8s - Swati Sehgal, Red Hat & Marlow Weston, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Swati Sehgal, Red Hat, Marlow Weston, Intel
- Schedule: https://kccnceu2022.sched.com/event/ytlD/this-is-the-way-a-crash-course-on-the-intricacies-of-managing-cpus-in-k8s-swati-sehgal-red-hat-marlow-weston-intel
- Busca YouTube: https://www.youtube.com/results?search_query=This+is+The+Way%3A+A+Crash+Course+on+the+Intricacies+of+Managing+CPUs+in+K8s+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre This is The Way: A Crash Course on the Intricacies of Managing CPUs in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlD/this-is-the-way-a-crash-course-on-the-intricacies-of-managing-cpus-in-k8s-swati-sehgal-red-hat-marlow-weston-intel
- YouTube search: https://www.youtube.com/results?search_query=This+is+The+Way%3A+A+Crash+Course+on+the+Intricacies+of+Managing+CPUs+in+K8s+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IFEJD1YOpXo
- YouTube title: This is The Way: A Crash Course on the Intricacies of Managing CPUs... Swati Sehgal & Marlow Weston
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/this-is-the-way-a-crash-course-on-the-intricacies-of-managing-cpus-in/IFEJD1YOpXo.txt
- Transcript chars: 19938
- Keywords: resource, manager, resources, container, containers, topology, workloads, policy, performance, option, working, management, kubelet, scheduling, memory, limits, scheduler, sensitive

### Resumo baseado na transcript

hello everyone i'm swati segal i'm a principal software engineer working for redhat and i'm marla weston i'm a cloud native architect working for intel and we're presenting this is the way a crash course in the intricacies of managing cpus and kubernetes the scope we will cover cpu management requirements only but we'll also reference other projects things aren't in a vacuum and your cpus are just part of the whole picture in the beginning systems were simple and here's an idea of why they were simple uh nodes

### Excerpt da transcript

hello everyone i'm swati segal i'm a principal software engineer working for redhat and i'm marla weston i'm a cloud native architect working for intel and we're presenting this is the way a crash course in the intricacies of managing cpus and kubernetes the scope we will cover cpu management requirements only but we'll also reference other projects things aren't in a vacuum and your cpus are just part of the whole picture in the beginning systems were simple and here's an idea of why they were simple uh nodes that had only single sockets there was a nick there was some memory there was some switch and there's world because you're only really running microservices at the beginning with kubernetes kubelet was designed for simple as well at first so here's what the early kubla looks like it has none of the the managers that we have today and it's just a simple throughput between your pod and the resources on the node so i want to take you back in time early 2017 free kubernetes 1.8 release and show you how the landscape looked like from resource point of view at this point we have cpu and memory as only two native resources supported requests and limits that you see highlighted here are mechanisms kubernetes uses to control these resources requests are what a container asks for and is guaranteed to get cube scheduler uses this to identify a suitable node that can fulfill the resource requirement limits on the other hand make sure a container never goes above certain value cubelet and container runtime uses this to enforce limits on contain on the resource consumption cfs quota is what is used to enforce cpu limits on the containers particularly from cpu perspective all the pods and containers running on a compute node can execute on any of the available cores on that node this level of resource control is not sufficient when pods are running cpu intensive workloads and contending for cpu resources available on that particular node these there can be scenarios where uh workloads get moved to different cpus which could impact the performance if it is sensitive to contact switches um one interesting thing to note here is that pod spec looks very similar to what it looks like today but there are some nuances that you need to know to be able to tap into some of the new advanced features that we'll cover in the subsequent slides so around this time there was a lot of discussion going on in the community to enhance kubernetes in order to support diverse and increas
