---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Yuan Chen", "Yibo Zhuang", "Wei Huang", "Apple", "Chen Wang", "IBM Research"]
sched_url: https://kccncna2022.sched.com/event/182Fb/tutorial-unleash-the-full-potential-of-kubernetes-scheduler-configuration-extension-and-operation-in-production-yuan-chen-yibo-zhuang-wei-huang-apple-chen-wang-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Unleash+the+Full+Potential+Of+Kubernetes+Scheduler%3A+Configuration%2C+Extension+And+Operation+In+Production+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tutorial: Unleash the Full Potential Of Kubernetes Scheduler: Configuration, Extension And Operation In Production - Yuan Chen, Yibo Zhuang & Wei Huang, Apple; Chen Wang, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Yuan Chen, Yibo Zhuang, Wei Huang, Apple, Chen Wang, IBM Research
- Schedule: https://kccncna2022.sched.com/event/182Fb/tutorial-unleash-the-full-potential-of-kubernetes-scheduler-configuration-extension-and-operation-in-production-yuan-chen-yibo-zhuang-wei-huang-apple-chen-wang-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Unleash+the+Full+Potential+Of+Kubernetes+Scheduler%3A+Configuration%2C+Extension+And+Operation+In+Production+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tutorial: Unleash the Full Potential Of Kubernetes Scheduler: Configuration, Extension And Operation In Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fb/tutorial-unleash-the-full-potential-of-kubernetes-scheduler-configuration-extension-and-operation-in-production-yuan-chen-yibo-zhuang-wei-huang-apple-chen-wang-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Unleash+the+Full+Potential+Of+Kubernetes+Scheduler%3A+Configuration%2C+Extension+And+Operation+In+Production+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iRwGWt7jXH0
- YouTube title: Tutorial: Unleash the Full Potential Of Kubernetes Scheduler: Configuration, Extension And Operat...
- Match score: 0.997
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tutorial-unleash-the-full-potential-of-kubernetes-scheduler-configurat/iRwGWt7jXH0.txt
- Transcript chars: 66261
- Keywords: schedule, default, scheduler, basically, plugin, configuration, plugins, information, scheduling, extension, another, filter, scheduled, seconds, second, particular, cluster, called

### Resumo baseado na transcript

hi everyone welcome to join today's session I hope you have a great work week in Detroit uh so today we're going to share some handsome experience on running Cube schedule including configuration extension and operation we hope by the end of this talk you will get some uh practical ideas and actionable practice is to run your schedule more efficiently in your production environment and firstly let's introduce ourselves hi I'm Yan CH from Apple cloud service so glad to meet you and it's cool to so see so

### Excerpt da transcript

hi everyone welcome to join today's session I hope you have a great work week in Detroit uh so today we're going to share some handsome experience on running Cube schedule including configuration extension and operation we hope by the end of this talk you will get some uh practical ideas and actionable practice is to run your schedule more efficiently in your production environment and firstly let's introduce ourselves hi I'm Yan CH from Apple cloud service so glad to meet you and it's cool to so see so many people show up hopefully there are many more people online uh I'm Wayan I'm also from Apple uh I'm also the co-chair of the six scheduling uh I'm EO uh I work in as a software engineer in apple C Services uh this is actually my first cubec con so I'm pretty excited hello everyone I'm Chen Wong from IBM research and I actively uh contribute to uh schedular plugins and Autos scaling on the other side because I'm in research I also did a lot of research work uh in resource management for uh kubernetes and I also try to enhance kuber ntic with for all types of machine learning workload um very looking forward to talking to you in person cool uh so this is today's agenda firstly we will give a very high level introduction on the cube scheduling and then we'll Deep dive into each part configuration operation and extension and in the end we hope we can have five to 10 minutes for answering questions all right the first part is about what is scheding anyways so when we talk about scheduling we usually talk about the typical part life cycle because schedule is just playing a certain part in the whole life cycle so starts with the part creation you should either by a us directory creating a path or creating a deployment and the controller manager is responsible for spinning up The Path so after that the job of the controller manager is done then is turn to the schedule to try to use its knowledge on the whole cluster to find the best Note for the PA so right now it just treat the schedule as a black box the input is the pending part and the output is uh the part associated with Noe and after that it's culate is responsibility then the corresponding Cate will get notified okay there part coming to mind I know I so I should be responsible to bring it up to spin up the corresponding containers then the part gets into running State and after that optionally if it's a run to completion part then it will run its job finish the job and it's done then the part gets into
