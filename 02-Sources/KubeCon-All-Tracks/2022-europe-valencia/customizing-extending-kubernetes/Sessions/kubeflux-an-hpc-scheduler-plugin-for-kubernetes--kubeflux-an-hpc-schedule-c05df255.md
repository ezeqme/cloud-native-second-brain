---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Claudia Misale", "IBM T.J. Watson Research Center", "Daniel Milroy", "Lawrence Livermore National Laboratory"]
sched_url: https://kccnceu2022.sched.com/event/ytnO/kubeflux-an-hpc-scheduler-plugin-for-kubernetes-claudia-misale-ibm-tj-watson-research-center-daniel-milroy-lawrence-livermore-national-laboratory
youtube_search_url: https://www.youtube.com/results?search_query=KubeFlux%3A+An+HPC+Scheduler+Plugin+for+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# KubeFlux: An HPC Scheduler Plugin for Kubernetes - Claudia Misale, IBM T.J. Watson Research Center & Daniel Milroy, Lawrence Livermore National Laboratory

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Claudia Misale, IBM T.J. Watson Research Center, Daniel Milroy, Lawrence Livermore National Laboratory
- Schedule: https://kccnceu2022.sched.com/event/ytnO/kubeflux-an-hpc-scheduler-plugin-for-kubernetes-claudia-misale-ibm-tj-watson-research-center-daniel-milroy-lawrence-livermore-national-laboratory
- Busca YouTube: https://www.youtube.com/results?search_query=KubeFlux%3A+An+HPC+Scheduler+Plugin+for+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre KubeFlux: An HPC Scheduler Plugin for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytnO/kubeflux-an-hpc-scheduler-plugin-for-kubernetes-claudia-misale-ibm-tj-watson-research-center-daniel-milroy-lawrence-livermore-national-laboratory
- YouTube search: https://www.youtube.com/results?search_query=KubeFlux%3A+An+HPC+Scheduler+Plugin+for+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3HGzzfsFrGQ
- YouTube title: KubeFlux: An HPC Scheduler Plugin for Kubernetes - Claudia Misale & Daniel Milroy
- Match score: 0.844
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubeflux-an-hpc-scheduler-plugin-for-kubernetes/3HGzzfsFrGQ.txt
- Transcript chars: 24452
- Keywords: flux, performance, computing, resource, application, scheduling, resources, topology, framework, schedule, cluster, scheduler, applications, placement, schedu, requirements, allocation, default

### Resumo baseado na transcript

hello and welcome to our session at the cubon cloud native conference Europe 2022 taking place from Valencia we'll be talking today about CU flux and HPC or high performance Computing schedu or plug-in for kubernetes on this Wednesday May 18th of 2022 my name is Daniel Milroy and I'm a computer scientist at the Center for Applied scientific Computing at the Lawrence Livermore National Laboratory in California in the United States I'm going to be the first speaker um and we'll be introducing some of the background and then

### Excerpt da transcript

hello and welcome to our session at the cubon cloud native conference Europe 2022 taking place from Valencia we'll be talking today about CU flux and HPC or high performance Computing schedu or plug-in for kubernetes on this Wednesday May 18th of 2022 my name is Daniel Milroy and I'm a computer scientist at the Center for Applied scientific Computing at the Lawrence Livermore National Laboratory in California in the United States I'm going to be the first speaker um and we'll be introducing some of the background and then hand off to Claudia misale who is a re research staff member at the ibmt J Watson Research Center we are representing a larger collaboration between three organizations which are again uh IBM TJ Watson Research Center the Lawrence Livermore National Laboratory and red hat so to give you a little bit of a background in high performance computing and in particular supercomputing I want to introduce a supercomputer to you as an example or perhaps Exemplar I'll highlight the AL Capa 10 machine which is projected to achieve greater than two exif flops so that's 2 * 10 18th power floating Point operations per second and is projected to be the world's fastest machine in 2023 now high performance also has high power requirements which in the case of ALC Capitan will will be approximately or less than 40 megaw so with this power consumption um in order to fit everything into a relatively small space you need to have quite a bit of density the compute blades that compose the machine are packed very closely together in cabinets and typically require liquid cooling now supercomputers are becoming more and more heterogeneous which means that there are many different types of processors and co-processors that are integrated Beyond just simply CPUs for example gpus and now we're starting to see as6 and fpgas as well as dedicated machine learning co-processors these machines feature high perlink bandwidth So currently around greater than 200 gbit per second per link perhaps more noteworthy for those of you who are not familiar with supercomputing is the low latency requirements so often super computers have sub microsc switching latency finally uh one of the other differentiators or something that's particular to supercomputing is that there tends to be very high utilization you usually see uh 90 to 99% resource utilization at any time now beyond the performance capabilities um I'm featuring the elcap 10 machine because it will integrate Cloud technology
