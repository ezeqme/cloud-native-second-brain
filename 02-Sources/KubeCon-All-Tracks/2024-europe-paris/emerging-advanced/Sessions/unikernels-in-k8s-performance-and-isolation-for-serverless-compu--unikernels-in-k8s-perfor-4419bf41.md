---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["SRE Reliability"]
speakers: ["Anastassios Nanos", "Ioannis Plakas", "NUBIS PC"]
sched_url: https://kccnceu2024.sched.com/event/1YeRd/unikernels-in-k8s-performance-and-isolation-for-serverless-computing-with-knative-anastassios-nanos-ioannis-plakas-nubis-pc
youtube_search_url: https://www.youtube.com/results?search_query=Unikernels+in+K8s%3A+Performance+and+Isolation+for+Serverless+Computing+with+Knative+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unikernels in K8s: Performance and Isolation for Serverless Computing with Knative - Anastassios Nanos & Ioannis Plakas, NUBIS PC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Anastassios Nanos, Ioannis Plakas, NUBIS PC
- Schedule: https://kccnceu2024.sched.com/event/1YeRd/unikernels-in-k8s-performance-and-isolation-for-serverless-computing-with-knative-anastassios-nanos-ioannis-plakas-nubis-pc
- Busca YouTube: https://www.youtube.com/results?search_query=Unikernels+in+K8s%3A+Performance+and+Isolation+for+Serverless+Computing+with+Knative+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unikernels in K8s: Performance and Isolation for Serverless Computing with Knative.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRd/unikernels-in-k8s-performance-and-isolation-for-serverless-computing-with-knative-anastassios-nanos-ioannis-plakas-nubis-pc
- YouTube search: https://www.youtube.com/results?search_query=Unikernels+in+K8s%3A+Performance+and+Isolation+for+Serverless+Computing+with+Knative+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YTE7OvxotDE
- YouTube title: Unikernels in K8s: Performance and Isolation for Serverless Computing with Knative
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unikernels-in-k8s-performance-and-isolation-for-serverless-computing-w/YTE7OvxotDE.txt
- Transcript chars: 21071
- Keywords: container, native, essentially, function, generic, containers, response, isolation, runtime, application, request, memory, latency, create, consumption, kernels, kernel, actually

### Resumo baseado na transcript

thanks very much for being here and thanks to the organizers for inviting us so I'm Anastasio Nanos um I'm going to talk about uh our work on uni kernels H how we integrated them into kubernetes and um how we um uh actually applied uni Kels in a use case like uh uh K native and uh and serverless um a bit of information about uh us so we're a young uh company um a young we're doing research um we're involved in the in research and Commercial projects

### Excerpt da transcript

thanks very much for being here and thanks to the organizers for inviting us so I'm Anastasio Nanos um I'm going to talk about uh our work on uni kernels H how we integrated them into kubernetes and um how we um uh actually applied uni Kels in a use case like uh uh K native and uh and serverless um a bit of information about uh us so we're a young uh company um a young we're doing research um we're involved in the in research and Commercial projects and uh we focus mainly on system software on the low level parts of the of the stock uh this is the team involved in the specific project so it's uh it's babies myself yorgos and yanis all Greeks um so let's let's first go through uh the the the broader topic of the of the presentation so we we were we were interested in um um in in seress platforms where users write a function in a high level language they pick the event to trigger this function and the underlying framework handles everything else the um instance selection deployment scaling um monitoring logging all all all this stuff um now there's a there's a group in uh at hauri where they they they are doing work on on systems in general um and they they focused on on serverless platforms and the requirements of these platforms so they are building their own uh system so they they they identified that there are issues regarding um execution latency uh throughput um Energy Efficiency regarding the the execution of the function on the on the hardware and um uh security and isolation of these functions um in in this talk we focus on the first and the last one so low latency uh um really uh low um the response times of the uh of the of the function and um on isolating the actual function from the rest of the of the of the platform uh so these these guys have concerns about the systems software stack so they they mentioned that um it retrofits Legacy infrastructure and presents High overhead when managing short LIF tasks so [Music] um however uh kubernetes is still the dominant orchestration framework and K native is a kubernetes native seress framework so our our take was it's it's not a random project it's it's actually something deployed and used by many many people so we we focus on trying to optimize the parts of the stock that we care about and and see what's going on there uh let's let's have a look at the at the architecture of K native so K native has a couple of components the activator the autoscaler and the function pods these components are being
