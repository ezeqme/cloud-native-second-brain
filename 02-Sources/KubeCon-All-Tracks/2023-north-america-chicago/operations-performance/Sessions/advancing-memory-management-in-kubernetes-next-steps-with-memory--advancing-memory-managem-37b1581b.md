---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Dixita Narang", "Google", "Antti Kervinen", "Intel"]
sched_url: https://kccncna2023.sched.com/event/1R2nL/advancing-memory-management-in-kubernetes-next-steps-with-memory-qos-dixita-narang-google-antti-kervinen-intel
youtube_search_url: https://www.youtube.com/results?search_query=Advancing+Memory+Management+in+Kubernetes%3A+Next+Steps+with+Memory+QoS+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Advancing Memory Management in Kubernetes: Next Steps with Memory QoS - Dixita Narang, Google & Antti Kervinen, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Dixita Narang, Google, Antti Kervinen, Intel
- Schedule: https://kccncna2023.sched.com/event/1R2nL/advancing-memory-management-in-kubernetes-next-steps-with-memory-qos-dixita-narang-google-antti-kervinen-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Advancing+Memory+Management+in+Kubernetes%3A+Next+Steps+with+Memory+QoS+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Advancing Memory Management in Kubernetes: Next Steps with Memory QoS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nL/advancing-memory-management-in-kubernetes-next-steps-with-memory-qos-dixita-narang-google-antti-kervinen-intel
- YouTube search: https://www.youtube.com/results?search_query=Advancing+Memory+Management+in+Kubernetes%3A+Next+Steps+with+Memory+QoS+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lbGe6hn_QwM
- YouTube title: Advancing Memory Management in Kubernetes: Next Steps with Memory... Dixita Narang & Antti Kervinen
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/advancing-memory-management-in-kubernetes-next-steps-with-memory-qos/lbGe6hn_QwM.txt
- Transcript chars: 21652
- Keywords: memory, container, process, workload, workloads, plug-in, actually, basically, requested, runtime, groups, processes, limits, plugins, values, configuration, information, throttle

### Resumo baseado na transcript

hello everyone thank you for coming to my session I am di Alias Dixie and I work for Google um my co-speaker who unfortunately couldn't make it to the conference because of personal reasons is anti-an and he works for Intel so this talk is about uh Advanced memory management techniques uh and memory Qs and uh some of the NRI plugins that you can use for managing the memory what is memory Qs so memory Qs feature is currently in Alpha it's actually Alpha since 127 and with cgroups Distributing the resources across those processes in a controlled manner so this is what a general uh kubernetes node would look like that has cgroups V2 configured it will have uh these three slices one is the cod slice one is system slice and the slice will then have U cgroup files basically the slices for each Qs classes that the kubernetes support so when you create a pod uh cuet takes care of uh creating the C group for the Pod and it places those files inside the Qs or kubernetes uh workloads so say this node has 1 GB of memory and there is a container one that requests 500 uh MB of memory and its usage is below the set value below the minimum uh requested value say 300 MB and then as well and we had to unfortunately uh stall the efforts uh to promote the feature to Beta I want to show uh give a demo of um how that live lock scenario looks like so say this is uh this is a PO spec

### Excerpt da transcript

hello everyone thank you for coming to my session I am di Alias Dixie and I work for Google um my co-speaker who unfortunately couldn't make it to the conference because of personal reasons is anti-an and he works for Intel so this talk is about uh Advanced memory management techniques uh and memory Qs and uh some of the NRI plugins that you can use for managing the memory what is memory Qs so memory Qs feature is currently in Alpha it's actually Alpha since 127 and with cgroups V2 exposing new memory controllers uh like memory. high and memory. Min we thought maybe we could configure uh these values to provide better memory guarantees and um memory. Min basically we wanted to map that to the requested memory and wanted to use memory. high for throttling the workloads so that uh kernel has enough chances to reclaim the memory before uh the container the containers reach the uh maximum limit so all of this sounded very promising theoretically but when we actually performed the test um we figured that our comprehension of memory.

high did not align with the recommended guidelines and before we delve into um what went wrong what are the key takeaways and our learnings from working on memory Qs Pro uh feature I would like to do a quick refresher on groups and what happens when you uh create a pod using podspec in kubernetes so what are c groups c groups are basically a mechanism that uh allows the processes to be uh organized hierarchically and the resources to be distributed um hierarchically as well and in a controlled manner uh and also in a configurable manner so c groups uh have two components one is the core and the other one is the controllers so core uh takes the responsibility of organizing the processes hierarchically and the controllers take the responsibility of Distributing the resources across those processes in a controlled manner so this is what a general uh kubernetes node would look like that has cgroups V2 configured it will have uh these three slices one is the cod slice one is system slice and the other one is user slice system slice will have uh all the configuration corresponding to the system services like container D cuet Etc and and cod.

slice will then have U cgroup files basically the slices for each Qs classes that the kubernetes support so when you create a pod uh cuet takes care of uh creating the C group for the Pod and it places those files inside the Qs uh to which inside the Qs directory to uh which the Pod belongs say best
