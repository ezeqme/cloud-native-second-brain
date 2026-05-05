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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Radostin Stoyanov", "University of Oxford", "Adrian Reber", "Red Hat", "Viktória Spišáková", "Masaryk University"]
sched_url: https://kccnceu2025.sched.com/event/1tx7i/efficient-transparent-checkpointing-of-aiml-workloads-in-kubernetes-radostin-stoyanov-university-of-oxford-adrian-reber-red-hat-viktoria-spisakova-masaryk-university
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Transparent+Checkpointing+of+AI%2FML+Workloads+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Efficient Transparent Checkpointing of AI/ML Workloads in Kubernetes - Radostin Stoyanov, University of Oxford; Adrian Reber, Red Hat; Viktória Spišáková, Masaryk University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Radostin Stoyanov, University of Oxford, Adrian Reber, Red Hat, Viktória Spišáková, Masaryk University
- Schedule: https://kccnceu2025.sched.com/event/1tx7i/efficient-transparent-checkpointing-of-aiml-workloads-in-kubernetes-radostin-stoyanov-university-of-oxford-adrian-reber-red-hat-viktoria-spisakova-masaryk-university
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Transparent+Checkpointing+of+AI%2FML+Workloads+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Efficient Transparent Checkpointing of AI/ML Workloads in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7i/efficient-transparent-checkpointing-of-aiml-workloads-in-kubernetes-radostin-stoyanov-university-of-oxford-adrian-reber-red-hat-viktoria-spisakova-masaryk-university
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Transparent+Checkpointing+of+AI%2FML+Workloads+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BSoEY_tpxIo
- YouTube title: Efficient Transparent Checkpointing of AI/ML Workloads in Kub... R. Stoyanov, A. Reber, V. Spišáková
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/efficient-transparent-checkpointing-of-ai-ml-workloads-in-kubernetes/BSoEY_tpxIo.txt
- Transcript chars: 26242
- Keywords: container, gpu, checkpoint, essentially, checkpointing, workloads, running, restore, utilization, another, memory, process, transparent, workload, information, around, mechanism, applications

### Resumo baseado na transcript

Um so today we are going to be talking about how we use efficient transparent checkpointing for um AI workloads and in Kubernetes and uh this work is a collaboration between my supervisors professor Rodrigo Bruno and professor Wes Armo and a few people from um Nvidia and AMD. So, during past CubeCons, folks have already presented some problems regarding inefficient resource utilization and fault tolerance. it is worth noting that overprovisioning such underutil underutilized workloads even worsens the problem of ineffective utilization. And of course there exists some existing approaches to these problems concerning utilization. Overprovisioning is not suitable for all workload types because workloads need to be aware that they can be autoscaled. Time sharing can worsen the performance and also is not suitable in environments where resources are shared by unrelated groups.

### Excerpt da transcript

Um so today we are going to be talking about how we use efficient transparent checkpointing for um AI workloads and in Kubernetes and uh this work is a collaboration between my supervisors professor Rodrigo Bruno and professor Wes Armo and a few people from um Nvidia and AMD. Um Victoria over to you. Hi. So, do you know what all these talks have in common? So, during past CubeCons, folks have already presented some problems regarding inefficient resource utilization and fault tolerance. These people were worried and concerned about ensuring that GPUs are used efficiently and that any problems that arise concerning GPU are resolved simply because GPUs are expensive resource. We can see that people from companies like Google, Microsoft, Huawei, Nvidia or CERN were um invested in this and they suggested various solutions uh mostly using mix or time sharing or some mentioned some new scheduling strategies and the thing is that this problem persists and in our case we experience it too but we are suggesting slightly different approach to solving these problems.

So who is we? Um I represent Czech national e infrastructure that operates multi-tenant multi-purpose kubernetes clusters that are free of charge for researchers and academics in Czech Republic. These clusters feature around 50 GPUs of various uh types and around 300 active users that operate uh different kinds of workloads that generally fall into two categories of bench workloads or interactive workloads. In operations, we aim for simplicity and some level of general applicability because of these variety of workloads, but also because by far not all users are proficient with containers, Kubernetes or generally complex setups. Now I will present three insights from our infrastructure. So starting with the first one on this graph we can see the said reality. So computational nodes seem generally occupied due to generous requests but the in reality the real utilization is quite low. Um in this data utilization in this like CPU utilization graph uh we can see computational nodes and their real utilization and the whole capacity and the ratio between these two generally vise between 1 to 50% with an average being 6%.

which is quite sad and definitely could be improved. But overall in cloud some level of overprovisioning is necessary because cloud should be elastic. Cloud should be able to provision for sudden spikes and also cloud should be able to accommodate redundant workloads and if this is the case
