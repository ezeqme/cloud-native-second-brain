---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Parul Singh", "Red Hat", "Krishnasuri Narayanam", "IBM"]
sched_url: https://kccnceu2024.sched.com/event/1YeP1/empowering-efficiency-peaks-orchestrating-power-aware-kubernetes-scheduling-parul-singh-red-hat-krishnasuri-narayanam-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Empowering+Efficiency%3A+PEAKS+-+Orchestrating+Power-Aware+Kubernetes+Scheduling+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Empowering Efficiency: PEAKS - Orchestrating Power-Aware Kubernetes Scheduling - Parul Singh, Red Hat & Krishnasuri Narayanam, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Parul Singh, Red Hat, Krishnasuri Narayanam, IBM
- Schedule: https://kccnceu2024.sched.com/event/1YeP1/empowering-efficiency-peaks-orchestrating-power-aware-kubernetes-scheduling-parul-singh-red-hat-krishnasuri-narayanam-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Empowering+Efficiency%3A+PEAKS+-+Orchestrating+Power-Aware+Kubernetes+Scheduling+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Empowering Efficiency: PEAKS - Orchestrating Power-Aware Kubernetes Scheduling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeP1/empowering-efficiency-peaks-orchestrating-power-aware-kubernetes-scheduling-parul-singh-red-hat-krishnasuri-narayanam-ibm
- YouTube search: https://www.youtube.com/results?search_query=Empowering+Efficiency%3A+PEAKS+-+Orchestrating+Power-Aware+Kubernetes+Scheduling+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WPrSnZ4lyjw
- YouTube title: Empowering Efficiency: PEAKS - Orchestrating Power-Aware Kubernetes Scheduling
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/empowering-efficiency-peaks-orchestrating-power-aware-kubernetes-sched/WPrSnZ4lyjw.txt
- Transcript chars: 31286
- Keywords: energy, cluster, scheduler, consumption, efficient, default, utilization, actually, running, efficiency, scheduling, metrics, resources, plugin, application, across, particular, plug-in

### Resumo baseado na transcript

hi uh if you're not asleep already you can join us in the next talk I am paru and with me you have Krishna uh we are going to talk about how you can empower the efficiency of your clusters by using power aware kubernetes scheduling so we've had too many Ai and LM sessions this is a good refresher for you and stay with us so first who we are we are open- Source contributors that are working on cloud native sustainability stack and the major contribution comes from

### Excerpt da transcript

hi uh if you're not asleep already you can join us in the next talk I am paru and with me you have Krishna uh we are going to talk about how you can empower the efficiency of your clusters by using power aware kubernetes scheduling so we've had too many Ai and LM sessions this is a good refresher for you and stay with us so first who we are we are open- Source contributors that are working on cloud native sustainability stack and the major contribution comes from IBM Intel and red hat any intel folks here no we have few ibmers and any Red Hats okay so at the Cornerstone we have the project Kepler which gives you energy observability metrics of your CL cler and around Kepler we have other projects that we are using to consume those observability metrics to do cluster optimization Kepler is a CNC of sandbox project already and feel free to drop at a kiosk on Friday 10:30 to 12:30 if you want to know more about Kepler but today we are talking about weaks which uses Kepler observability data to do energy and and power aware kuity scheduling so what problem are we trying to solve well we all know that the I'm not sure if all know like anybody familiar with kubernetes scheduling framework okay so like kubernetes scheduling framework gives you the provision to have your inbuilt or like custom schuer plugin that you just hook up with the uh scheduling framework and you can uh optimize or you can try to solve whatever problem you're solving in the scheduling or whatever objectives you are uh trying to maximize or minimize but within the ecosystem we found that there's a lack of schedular plugins that focuses on uh Power optimization or Energy Efficiency while also taking care of the other objectives that they are trying to solve so uh we thought of developing Peaks that can address this Gap and what Peaks does it it essentially try tries to maximize the Energy Efficiency of your cluster while also focusing or letting you do other stuffs uh like how to optimize on topology and how to optimize on network um Network or CPU utilization so our goal was to come up with a configural scheduling plug-in that minimize the aggregate power consumption of the entire cluster and we wanted to implement it as a score plug-in while making sure that we are not altering the default scoring plugging U of the kubernetes framework so the solution obviously Peaks been just talked about Peaks for so long so uh paks is a kubernetes schedul plugging that aims to optimize the aggregate power
