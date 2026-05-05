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
themes: ["Observability", "SRE Reliability"]
speakers: ["Jia Deng", "Cong Xu", "Mingmeng Luo", "Bytedance"]
sched_url: https://kccncna2024.sched.com/event/1i7pp/service-profiling-based-management-and-scheduling-in-k8s-jia-deng-cong-xu-mingmeng-luo-bytedance
youtube_search_url: https://www.youtube.com/results?search_query=Service+Profiling+Based+Management+and+Scheduling+in+K8s+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Service Profiling Based Management and Scheduling in K8s - Jia Deng, Cong Xu & Mingmeng Luo, Bytedance

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Jia Deng, Cong Xu, Mingmeng Luo, Bytedance
- Schedule: https://kccncna2024.sched.com/event/1i7pp/service-profiling-based-management-and-scheduling-in-k8s-jia-deng-cong-xu-mingmeng-luo-bytedance
- Busca YouTube: https://www.youtube.com/results?search_query=Service+Profiling+Based+Management+and+Scheduling+in+K8s+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Service Profiling Based Management and Scheduling in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pp/service-profiling-based-management-and-scheduling-in-k8s-jia-deng-cong-xu-mingmeng-luo-bytedance
- YouTube search: https://www.youtube.com/results?search_query=Service+Profiling+Based+Management+and+Scheduling+in+K8s+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nbc5acJv9r0
- YouTube title: Service Profiling Based Management and Scheduling in K8- Jia Deng, Cong Xu & Mingmeng Luo, Bytedance
- Match score: 0.808
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/service-profiling-based-management-and-scheduling-in-k8s/nbc5acJv9r0.txt
- Transcript chars: 14209
- Keywords: resource, memory, workload, bandwidth, machine, scheduling, profiling, schedule, profile, catalyst, cluster, resources, better, management, session, online, network, performance

### Resumo baseado na transcript

all right thanks um people staying to the last this is the last session of this week and welcome to the session yeah after this one weekend um so yeah the session we talk about service profiling based resource management and scheduling I'm G Dan and this is my colleague Ming Mong and we're from by Dan so for today's talk um the overview would be I'm going to talk about the introduction like why we're doing this and how we do service profiling um how we use the profiling

### Excerpt da transcript

all right thanks um people staying to the last this is the last session of this week and welcome to the session yeah after this one weekend um so yeah the session we talk about service profiling based resource management and scheduling I'm G Dan and this is my colleague Ming Mong and we're from by Dan so for today's talk um the overview would be I'm going to talk about the introduction like why we're doing this and how we do service profiling um how we use the profiling into the scheduling and um this whole project is open sourced into a project named catalyst so mimo will talk about Catalyst and I believe some of gu some of you guys come here because you went to yesterday's session godell scheduler and you might wonder how godell schuer and calist how they work together and then we're talk about the future plan um and also I'll upload I'll upload the slides at after the session I'll upload to the ktic like the cucon website okay first is the project introduction so in bance um there are various machine types and worklad types in one cluster that we need to manage we have machine from different ver of different um vendors or Brands and different generator Generations in one cluster and we also have different kind of services running in one cluster like online services workload um model training and streaming Etc ideally those workload consuming different types of resources should distribute evenly according to all noes capacity however native kubernets only support CPU and memory as we all know but there are lots of resources like um dis IO memory bandwidth Network bandwidth power Etc uh and each resource has its upper limit on each node saying like we have different machines and different machine Generations they have different um limits on those resources so there are cases like workload scheduled at the same node are say um memory bandwidth intensive or network memory band bandwidth intensive but they don't consume High CPU or memory then the memory bandwidth or the network bandwidth or the other like resources becomes the bottom neck of a performance like um the left side figure shows um the scheduler should put those workloads on different noes so not a single resource is the shortest Board of the bucket on the other hand unlike CPU and memory um customers they don't have a direct sense of how much resources they're using or how much they should apply for so we need a way to better describe the workload for better scheduling um going forward I'll take
