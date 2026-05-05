---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Kaysie Yu", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7rK/divide-and-conquer-master-gpu-partitioning-and-visualize-savings-with-opencost-kaysie-yu-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Divide+and+Conquer%3A+Master+GPU+Partitioning+and+Visualize+Savings+with+OpenCost+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Divide and Conquer: Master GPU Partitioning and Visualize Savings with OpenCost - Kaysie Yu, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Kaysie Yu, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7rK/divide-and-conquer-master-gpu-partitioning-and-visualize-savings-with-opencost-kaysie-yu-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Divide+and+Conquer%3A+Master+GPU+Partitioning+and+Visualize+Savings+with+OpenCost+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Divide and Conquer: Master GPU Partitioning and Visualize Savings with OpenCost.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rK/divide-and-conquer-master-gpu-partitioning-and-visualize-savings-with-opencost-kaysie-yu-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Divide+and+Conquer%3A+Master+GPU+Partitioning+and+Visualize+Savings+with+OpenCost+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sH699gmFC0o
- YouTube title: Divide and Conquer: Master GPU Partitioning and Visualize Savings with OpenCost - Kaysie Yu
- Match score: 1.02
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/divide-and-conquer-master-gpu-partitioning-and-visualize-savings-with/sH699gmFC0o.txt
- Transcript chars: 23660
- Keywords: gpu, cost, slicing, actually, metrics, partitioning, running, utilization, workloads, resources, operator, nvidia, monitoring, cluster, access, prometheus, install, single

### Resumo baseado na transcript

welcome to the session divide and conquer Master GPU partitioning and visualize savings with open cost my name is Casey U I'm a product manager on Azure kubernetes service team at Microsoft uh I work on everything cost management optimization so really excited to talk about this topic with you uh unfortunately my Cobra Cent and colleague Ally wasn't able to make it today so it's just me all right so today we'll chat a bit about why people are even running gpus uh what this looks like in the

### Excerpt da transcript

welcome to the session divide and conquer Master GPU partitioning and visualize savings with open cost my name is Casey U I'm a product manager on Azure kubernetes service team at Microsoft uh I work on everything cost management optimization so really excited to talk about this topic with you uh unfortunately my Cobra Cent and colleague Ally wasn't able to make it today so it's just me all right so today we'll chat a bit about why people are even running gpus uh what this looks like in the industry we'll layer in costs so when we think about gpus and costs what are some of the challenges and issues that we're facing and then we'll talk about how to monitor GPU usage metrics uh visualize your GPU costs and then ultimately Implement partitioning techniques to go and optimize your GPU utilization uh and we'll tie it together in the end with a demo showing how to set up uh Nvidia GPU operator Implement time slicing and then also leverage open cost so as we all know gpus are scarce and expensive uh the scarcity often means that when we get a GPU we may want to hold on to it even if we're not using it and if we're doing that if we have a GPU we want to make sure we're extracting every penny every cent out of it that we can because they're so expensive uh so really why why do we want to pay for these gpus if they're not going to be utilized and they're sitting their idle GPU uh utilization this is the amount of time during which one or more kernels um are are executing on the GPU and by default when kubernetes is scheduling GPU workloads uh it assigns a whole GPU to a single workload or job exclusively this is called exclusive access uh and with kubernetes uh in the Pod manifest when you're actually requesting your GPU resource uh you have to request in whole integers so it's a little bit of a different model compared to CPUs where you can request uh fractions of a CPU the exclusive access model means that usually a workload is not going to use the entire gpus resources so a lot of the utilization is actually going to be sitting their idle um this this means you know when we think about at skill is this actually feasible is it economical to run AI workloads on gpus well it absolutely can be if we you know Implement certain strategies but before we talk about the strategies uh let's take a look at some data so in a recent Gartner Pier survey of over 500 Tech leaders they found that over 48% of organizations are actually using kubernetes already to run their AI ml
