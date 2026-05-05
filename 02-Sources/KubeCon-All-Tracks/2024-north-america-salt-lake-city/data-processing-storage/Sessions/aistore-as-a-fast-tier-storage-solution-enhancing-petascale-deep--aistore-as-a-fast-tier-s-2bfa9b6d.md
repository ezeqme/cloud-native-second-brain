---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Abhishek Gaikwad", "Aaron Wilson", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7lG/aistore-as-a-fast-tier-storage-solution-enhancing-petascale-deep-learning-across-cloud-backends-abhishek-gaikwad-aaron-wilson-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=AIStore+as+a+Fast+Tier+Storage+Solution%3A+Enhancing+Petascale+Deep+Learning+Across+Cloud+Backends+CNCF+KubeCon+2024
slides: []
status: parsed
---

# AIStore as a Fast Tier Storage Solution: Enhancing Petascale Deep Learning Across Cloud Backends - Abhishek Gaikwad & Aaron Wilson, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Abhishek Gaikwad, Aaron Wilson, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7lG/aistore-as-a-fast-tier-storage-solution-enhancing-petascale-deep-learning-across-cloud-backends-abhishek-gaikwad-aaron-wilson-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=AIStore+as+a+Fast+Tier+Storage+Solution%3A+Enhancing+Petascale+Deep+Learning+Across+Cloud+Backends+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre AIStore as a Fast Tier Storage Solution: Enhancing Petascale Deep Learning Across Cloud Backends.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lG/aistore-as-a-fast-tier-storage-solution-enhancing-petascale-deep-learning-across-cloud-backends-abhishek-gaikwad-aaron-wilson-nvidia
- YouTube search: https://www.youtube.com/results?search_query=AIStore+as+a+Fast+Tier+Storage+Solution%3A+Enhancing+Petascale+Deep+Learning+Across+Cloud+Backends+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N-d9cbROndg
- YouTube title: AIStore as a Fast Tier Storage Solution: Enhancing Petascale Deep Learning... A. Gaikwad & A. Wilson
- Match score: 0.936
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/aistore-as-a-fast-tier-storage-solution-enhancing-petascale-deep-learn/N-d9cbROndg.txt
- Transcript chars: 29497
- Keywords: cluster, object, storage, performance, actually, running, target, objects, proxies, targets, clusters, workloads, throughput, network, multiple, clients, stored, compatible

### Resumo baseado na transcript

hello everyone I'm abishek and with me is Aaron and today we are presenting AI store as a fasti storage solution to enhance your P skill deep learning jobs across remote Cloud backends uh so um let's look at in in this presentation we're going to look at what are the current challenges that we are facing with loading data from the cloud introduce AI store and how AI store addresses these challenges um uh share some production numbers and workloads with you and finally dwell into the ongoing research

### Excerpt da transcript

hello everyone I'm abishek and with me is Aaron and today we are presenting AI store as a fasti storage solution to enhance your P skill deep learning jobs across remote Cloud backends uh so um let's look at in in this presentation we're going to look at what are the current challenges that we are facing with loading data from the cloud introduce AI store and how AI store addresses these challenges um uh share some production numbers and workloads with you and finally dwell into the ongoing research so let's look at the challenges um so at Nvidia our gpus are becoming insanely powerful but here's the kicker the io performance isn't keeping up this mismatch means that the gpus are often underutilized because they can process data at a faster rate than the data can be delivered let's talk about data in the cloud storing a petabyte up there isn't just expensive it's incredibly slow and if your gpus are in another region that's another cross layer and in such situations latency can be a real bottleneck as well um GPU nodes usually don't have enough local storage so if you're training for multiple epocs you might end up redownloading the same data again and again if you're really unlucky all your data might be scattered some might be on Prem some might be on Azure and some might be on AWS and trying to get a consist consistent throughput and latency from this hod Podge is like juggling lives so training a training on a paby of data is isn't just a walk in the park you need the right right tools libraries plugins and operations to handle data at this massive scale without them you are just left wrestling with data instead of training your models so from what we have observed in our workloads is that um usually machine Lear learning workloads make random reads to a vast amount of unstructured data and reading reading a paby of data randomly without having a petabyte of Ram or any similar fast G cachier it's really difficult and slow and hence storage becomes the primary bottleneck in contemporary machine learning so with all these challenges like storage bottlenecks latencies and Cloud how do we keep our gpus fed and avoid costly downtime let me introduce you to AI store so AI store is a fully open source lightweight software storage uh object storage system that is typically tailored for AI related workloads uh AI store offers linear scalability with each added node or drive so if you're adding more storage nodes to your cluster you'll increase your IO by that p
