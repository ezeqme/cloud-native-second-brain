---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["William Wang", "Huawei", "Mengxuan Li", "4paradigm"]
sched_url: https://kccnceu2024.sched.com/event/1Yhif/cloud-native-batch-computing-with-volcano-updates-and-future-william-wang-huawei-mengxuan-li-4paradigm
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Batch+Computing+with+Volcano%3A+Updates+and+Future+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cloud Native Batch Computing with Volcano: Updates and Future - William Wang, Huawei & Mengxuan Li, 4paradigm

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: William Wang, Huawei, Mengxuan Li, 4paradigm
- Schedule: https://kccnceu2024.sched.com/event/1Yhif/cloud-native-batch-computing-with-volcano-updates-and-future-william-wang-huawei-mengxuan-li-4paradigm
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Batch+Computing+with+Volcano%3A+Updates+and+Future+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cloud Native Batch Computing with Volcano: Updates and Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhif/cloud-native-batch-computing-with-volcano-updates-and-future-william-wang-huawei-mengxuan-li-4paradigm
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Batch+Computing+with+Volcano%3A+Updates+and+Future+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fVYKk6xSOsw
- YouTube title: Cloud Native Batch Computing with Volcano: Updates and Future - William Wang & Mengxuan Li
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cloud-native-batch-computing-with-volcano-updates-and-future/fVYKk6xSOsw.txt
- Transcript chars: 18378
- Keywords: volcano, resources, support, gpu, scheduler, scheduling, feature, workload, priority, resource, utilization, cluster, training, device, memory, computing, sharing, features

### Resumo baseado na transcript

I'm I'm William Wang and I'm the maintainer of Volcano community and from Huawei Cloud. Uh we we have some updates and the the future roadmap share for you in this topic. The Volcano agent is is designed to provide the uh queues management for the for the workload. So, this rescheduler will work with the Prometheuses Prometheuses monitor system to balance the resources more efficiently in Kubernetes cluster. So, in at the beginning we support we support we we we we designed the a set of batch API to support the AI workload running on the Kubernetes. So, in this feature we this feature we support the Volcano scheduler to communicate with the monitor system like Prometheuses and the ERQ system.

### Excerpt da transcript

Good morning, everyone. Welcome to this topic. I'm I'm William Wang and I'm the maintainer of Volcano community and from Huawei Cloud. This is my partner. Uh my name is Liming come from the Force Paradigm. Okay. And today our topic is cloud native batch computing with Volcano. Uh we we have some updates and the the future roadmap share for you in this topic. So, there are four parts. The first The first part is is about the Volcano intro- introduction. And then I will share the updates and the improvement uh of Volcano community. And third part is about the GPU sharing and isolation from my partner. They will uh deep dive. And finally, I'm going to share the community and the roadmap. So, here is a overall Volcano architecture. Uh from the picture, we can see that uh Volcano community have strong strong relationship with the upstream computing frameworks like TensorFlow, PyTorch, Spark, Flink, and so on. And also we can see that Volcano is not just a scheduler. So, it has a pod group and job group controller to provide the enhancement job enhanced job management.

And also it has the queue CRD to help user to share their resources more efficiently. And also we have lot of we we spend a lot of effort to work with the analyzing hardware to support different kind of heterogeneous devices such as GPU, x86, uh Intel MPU, TPU, something like that. And also we we work with the Kubernetes team to improve some im- some some performance, especially for the AI workload and Spark workload. So, this year we will add two more component in the architecture. First one is the Volcano agent. The Volcano agent is is designed to provide the uh queues management for the for the workload. And also we will we will add a new component that named the rescheduler. So, this rescheduler will work with the Prometheuses Prometheuses monitor system to balance the resources more efficiently in Kubernetes cluster. Here is the the the general of Volcano. So, in at the beginning we support we support we we we we designed the a set of batch API to support the AI workload running on the Kubernetes.

And and then we supported the pod group, the the the queue CRD, and provide a set of uh scheduling policies for big data area like the fair fair share scheduling, the resource reservation to prevent the resource competition between the Spark driver and the workers. And then we have received a lot of feedback from the community users. Uh so, they they said there are so many kind of uh training oper
