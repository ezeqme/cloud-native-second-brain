---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Abdul Qadeer", "PayPal", "Chen Wang", "IBM"]
sched_url: https://kccncna2021.sched.com/event/lV12/trimaran-real-load-aware-scheduling-in-kubernetes-abdul-qadeer-paypal-chen-wang-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Trimaran%3A+Real+Load+Aware+Scheduling+in+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Trimaran: Real Load Aware Scheduling in Kubernetes - Abdul Qadeer, PayPal & Chen Wang, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Abdul Qadeer, PayPal, Chen Wang, IBM
- Schedule: https://kccncna2021.sched.com/event/lV12/trimaran-real-load-aware-scheduling-in-kubernetes-abdul-qadeer-paypal-chen-wang-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Trimaran%3A+Real+Load+Aware+Scheduling+in+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Trimaran: Real Load Aware Scheduling in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV12/trimaran-real-load-aware-scheduling-in-kubernetes-abdul-qadeer-paypal-chen-wang-ibm
- YouTube search: https://www.youtube.com/results?search_query=Trimaran%3A+Real+Load+Aware+Scheduling+in+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aLQidRZvw60
- YouTube title: Trimaran: Real Load Aware Scheduling in Kubernetes - Abdul Qadeer, PayPal & Chen Wang, IBM
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/trimaran-real-load-aware-scheduling-in-kubernetes/aLQidRZvw60.txt
- Transcript chars: 24747
- Keywords: utilization, scheduler, plugins, average, packing, plugin, target, scheduling, metrics, cluster, higher, metric, variation, workload, standard, balancing, default, scoring

### Resumo baseado na transcript

okay good afternoon and welcome everybody uh in person and online um thank you for joining us for trimaran real load we're scheduling in kubernetes um would you all join me in welcoming um abdul kadir from paypal and chen wang from ibm [Applause] uh good afternoon everyone those present here and greetings to my uh my greetings to those virtual present virtually so i'm abdul khadir i i'm a senior software engineer at paypal i'll be presenting on load aware scheduling with my collaborator chen wang who is a

### Excerpt da transcript

okay good afternoon and welcome everybody uh in person and online um thank you for joining us for trimaran real load we're scheduling in kubernetes um would you all join me in welcoming um abdul kadir from paypal and chen wang from ibm [Applause] uh good afternoon everyone those present here and greetings to my uh my greetings to those virtual present virtually so i'm abdul khadir i i'm a senior software engineer at paypal i'll be presenting on load aware scheduling with my collaborator chen wang who is a research scientist at ibm so the image you see here is of trimaran so what it stands for is like a three hulled boat which provides more stability and safety in the ocean all right let's get started so this is the agenda for today uh we'll go over the motivation the background and the problem definition followed by the primer and architecture the design and the plugins we contributed to the open source community the first one is the target load packing and the second one the load variation risk balancing plug-in then we have a demo and then some of the challenges timer and phases how we overcome them followed by good practices in using primary in production and some future work that we have to do so let's get started with further review so as many of you may know kubernetes provides a declarative resource model for its pods what i mean by declarative model is that the resource usage that you define for your pod or the container needs to be defined in a spec before you're able to run it and run your workload and the core components in kubernetes namely the cubelet the scheduler uh they honor honor it to behave consistently with respect to the quality of service guarantees now given this the developers they tend to over provision the resources with this model uh which you know one of the reasons is that they want to avoid the penalties of evictions and cpu throttling that the kubernetes would do now one way to solve this problem of declarative uh model is to benchmark your applications but we we know that like it could be comparison to do for all your production applications and in general estimating real load is hard now with that background the main problem we are trying to solve is that the default scheduler in kubernetes it uses allocation based scheduling model and it can lead to under provision nodes in terms of resources and fragmentation of course across the cluster what you see on the right bottom right is a graph from 29 day google trace in their
