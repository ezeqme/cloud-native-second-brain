---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Theophilus Benson", "Prankur Gupta", "Meta"]
sched_url: https://kccncna2025.sched.com/event/27FeA/fast-and-the-furious-cicd-pipeline-for-ebpf-programs-at-meta-scale-theophilus-benson-prankur-gupta-meta
youtube_search_url: https://www.youtube.com/results?search_query=Fast+and+the+Furious%3A+CICD+Pipeline+for+eBPF+Programs+at+Meta+Scale+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Fast and the Furious: CICD Pipeline for eBPF Programs at Meta Scale - Theophilus Benson & Prankur Gupta, Meta

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Theophilus Benson, Prankur Gupta, Meta
- Schedule: https://kccncna2025.sched.com/event/27FeA/fast-and-the-furious-cicd-pipeline-for-ebpf-programs-at-meta-scale-theophilus-benson-prankur-gupta-meta
- Busca YouTube: https://www.youtube.com/results?search_query=Fast+and+the+Furious%3A+CICD+Pipeline+for+eBPF+Programs+at+Meta+Scale+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Fast and the Furious: CICD Pipeline for eBPF Programs at Meta Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FeA/fast-and-the-furious-cicd-pipeline-for-ebpf-programs-at-meta-scale-theophilus-benson-prankur-gupta-meta
- YouTube search: https://www.youtube.com/results?search_query=Fast+and+the+Furious%3A+CICD+Pipeline+for+eBPF+Programs+at+Meta+Scale+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wXuykaYSFCQ
- YouTube title: Fast and the Furious: CICD Pipeline for eBPF Programs at Meta S... Theophilus Benson & Prankur Gupta
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/fast-and-the-furious-cicd-pipeline-for-ebpf-programs-at-meta-scale/wXuykaYSFCQ.txt
- Transcript chars: 27835
- Keywords: actually, ebpf, kernel, programs, production, various, testing, basically, points, control, program, pipeline, little, attach, multiple, versions, change, metrics

### Resumo baseado na transcript

So yeah, so the topic for today's presentation is like fast and the furious CI/CD pipeline for EBPF programs at metas scale. Basically I first want to like start by setting up some context for the talk. So yeah, recently well again recent is of course relative a lot of companies have started adopting a BPF a motivating factor being impressive performance wins and now eBPF is becoming crucial and crucial for the cloudnative workloads especially in the AI area where the At Meta, we have had several significant wins across various metrics and the services. For example, we were able to do like 40% improvements in the P99 latency for commerce and research apps, 30% faster image generation, 100% faster storage read. A little bit of caveat, these metrics might be a little bit old, but I'm using it as it is because the recent ones are not made actual public yet.

### Excerpt da transcript

So yeah, so the topic for today's presentation is like fast and the furious CI/CD pipeline for EBPF programs at metas scale. Basically I first want to like start by setting up some context for the talk. These are all the people who are involved in developing and supporting our net binary which basically manages and deploys a bunch of ebpf programs across various attach points doing multiple tunings for packets and connections and also managing the entire congestion control algorithm in the entire meta fleet. So last year we published a paper for this and this talk is adding on top of that paper where we will go a little bit into details on like how we are able to manage so many ebpa programs at metas scale. One thing to remember throughout the presentation would be our majority of EBPA programs are are actively changing the status of the packets and the connection not just actually monitoring and obsering the states. Okay. So about us. I'm pranker. I'm a software engineer. My partner in crime Theo unfortunately he has to attend an urgent um teaching commitment in the Bay Area.

So he had to like skip the event. One thing if I want to like talk about myself is like um I started by writing the Rocky V2 RDMA AI transfer protocol in like assembly language into the nick firmware. Then I moved on to like the kernels and now I'm doing all the network optimization at like the user space level. So over my 12 plus years of career I have been very deep into like the tech the network stack. Cool. So yeah, recently well again recent is of course relative a lot of companies have started adopting a BPF a motivating factor being impressive performance wins and now eBPF is becoming crucial and crucial for the cloudnative workloads especially in the AI area where the the demand of the cloud and the efficiency requirements are going off the charts. At Meta, we have had several significant wins across various metrics and the services. For example, we were able to do like 40% improvements in the P99 latency for commerce and research apps, 30% faster image generation, 100% faster storage read.

A little bit of caveat, these metrics might be a little bit old, but I'm using it as it is because the recent ones are not made actual public yet. So motivated by these wins, we want to use ebpf almost everywhere. So the graph here on the right actually shows like the ebpf deployment. So at like a 99% of all our machines, we actively use ebpf by default and we are constantly evolving our
