---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Andrey Velichkevich", "Apple", "Yuki Iwai", "CyberAgent", "inc"]
sched_url: https://kccnceu2025.sched.com/event/1tx9k/from-high-performance-computing-to-ai-workloads-on-kubernetes-mpi-runtime-in-kubeflow-trainjob-andrey-velichkevich-apple-yuki-iwai-cyberagent-inc
youtube_search_url: https://www.youtube.com/results?search_query=From+High+Performance+Computing+To+AI+Workloads+on+Kubernetes%3A+MPI+Runtime+in+Kubeflow+TrainJob+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From High Performance Computing To AI Workloads on Kubernetes: MPI Runtime in Kubeflow TrainJob - Andrey Velichkevich, Apple & Yuki Iwai, CyberAgent, inc

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Andrey Velichkevich, Apple, Yuki Iwai, CyberAgent, inc
- Schedule: https://kccnceu2025.sched.com/event/1tx9k/from-high-performance-computing-to-ai-workloads-on-kubernetes-mpi-runtime-in-kubeflow-trainjob-andrey-velichkevich-apple-yuki-iwai-cyberagent-inc
- Busca YouTube: https://www.youtube.com/results?search_query=From+High+Performance+Computing+To+AI+Workloads+on+Kubernetes%3A+MPI+Runtime+in+Kubeflow+TrainJob+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From High Performance Computing To AI Workloads on Kubernetes: MPI Runtime in Kubeflow TrainJob.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9k/from-high-performance-computing-to-ai-workloads-on-kubernetes-mpi-runtime-in-kubeflow-trainjob-andrey-velichkevich-apple-yuki-iwai-cyberagent-inc
- YouTube search: https://www.youtube.com/results?search_query=From+High+Performance+Computing+To+AI+Workloads+on+Kubernetes%3A+MPI+Runtime+in+Kubeflow+TrainJob+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Fnb1a5Kaxgo
- YouTube title: From High Performance Computing To AI Workloads on Kubernetes: M... Andrey Velichkevich, & Yuki Iwai
- Match score: 0.818
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-high-performance-computing-to-ai-workloads-on-kubernetes-mpi-runt/Fnb1a5Kaxgo.txt
- Transcript chars: 25158
- Keywords: training, actually, runtime, infrastructure, scientists, trainer, distributed, simple, consider, environment, scientist, perform, function, working, however, called, available, native

### Resumo baseado na transcript

Uh so what we hear from them we've been working there for the last 7 to 8 years. So what they really wants they want quick ability to write ML code using native libraries like torch speed jacks and scale it tricky part because it's kind of like to do multiple times sometimes associated with the process. So what actually the end users want they just want a simplicity flexibility and scalability and they don't want to learn anything about kubernetes. So how we can abstract kubernetes um complexity from them so for this we actually do this project called cubeflow trainer uh we introduced this project in the last coupon in 2024. Uh so with that let me actually give a new thing that we're going to introduce in this session which is actually API runtime and I think like uh the best thing to know about API is actually doing the demo about this new frameworks with MLX and GP. So for those who not know MLX is the um framework specifically designed by we're going through why we actually want to leverage it here because MLX using API for distributed communication and we try to see how we can make it easier for folks

### Excerpt da transcript

simple to use API and various to optimize distributed workloads. So first of all let me speak about about data scientists. Uh so what we hear from them we've been working there for the last 7 to 8 years. So what they really wants they want quick ability to write ML code using native libraries like torch speed jacks and scale it tricky part because it's kind of like to do multiple times sometimes associated with the process. So the problem is like they kind of like want to do multiple times without even knowing it's running. But the trick is like in reality there are a lot of things associated with this process. For example, like they told us they need to know how to start environment, how to configure Docker images, how to configure compute resources or data access. Sometimes they also need to learn more about API. Maybe they want to know about Galing HPC technologies or maybe even know about resource cues. So all this we kind of talk infrastructure claim and the goal of us as a community how we can actually remove it because data scientist stuck behind this group and right now we also live in a world of geni you know models become much more complex we have like huge data set huge amount of data we have like all different frameworks the ecosystem is um is just a lot technology API nickel blue how we can provide a unified way to give them you know ability to interact with all those diversity of frameworks and in the same way adopting new technologies like uh uh API and other things.

So what actually the end users want they just want a simplicity flexibility and scalability and they don't want to learn anything about kubernetes. So how we can abstract kubernetes um complexity from them so for this we actually do this project called cubeflow trainer uh we introduced this project in the last coupon in 2024. So this project was kind of like a next generation of training operator which we started in 2017 right 2017 and basically this is we kind of separate uh different services. So we have a service for data science called train and we have a service for devops engineers called training runtime. So the difference is is training runtime is like a blueprint that platform engineers can use to configure those uh those configurations and data science can work with the one Python interface to interact with the jobs and then we're using the job set to actually perform distributed communications. Uh so with that let me actually give a new thing that we're going to intr
