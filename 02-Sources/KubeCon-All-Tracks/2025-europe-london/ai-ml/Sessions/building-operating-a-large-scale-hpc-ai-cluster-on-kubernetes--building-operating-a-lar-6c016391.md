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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Kalyan Saladi", "Chandan Avdhut", "Meta Platforms Inc."]
sched_url: https://kccnceu2025.sched.com/event/1tx7f/building-operating-a-large-scale-hpc-ai-cluster-on-kubernetes-kalyan-saladi-chandan-avdhut-meta-platforms-inc
youtube_search_url: https://www.youtube.com/results?search_query=Building+%26+Operating+a+Large-scale+HPC+AI+Cluster+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building & Operating a Large-scale HPC AI Cluster on Kubernetes - Kalyan Saladi & Chandan Avdhut, Meta Platforms Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Kalyan Saladi, Chandan Avdhut, Meta Platforms Inc.
- Schedule: https://kccnceu2025.sched.com/event/1tx7f/building-operating-a-large-scale-hpc-ai-cluster-on-kubernetes-kalyan-saladi-chandan-avdhut-meta-platforms-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Building+%26+Operating+a+Large-scale+HPC+AI+Cluster+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building & Operating a Large-scale HPC AI Cluster on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7f/building-operating-a-large-scale-hpc-ai-cluster-on-kubernetes-kalyan-saladi-chandan-avdhut-meta-platforms-inc
- YouTube search: https://www.youtube.com/results?search_query=Building+%26+Operating+a+Large-scale+HPC+AI+Cluster+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7KCBigZi_Rk
- YouTube title: Building & Operating a Large-scale HPC AI Cluster on Kubernetes - Kalyan Saladi & Chandan Avdhut
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-operating-a-large-scale-hpc-ai-cluster-on-kubernetes/7KCBigZi_Rk.txt
- Transcript chars: 34439
- Keywords: cluster, training, running, research, researcher, components, across, experience, public, storage, researchers, various, workload, infrastructure, reliability, multiple, providers, understand

### Resumo baseado na transcript

Uh hope you are having a good time here at CubeCon and um today we are going to share how we built a AI HPC cluster on the top of Kubernetes in public cloud. Uh so quick introduction my name is Chandraan Abdut I'm a production engineer at Meta and my co-presenter Kalen Saledi uh he's a software engineer uh he couldn't be here in person today uh but for his part of the presentation we have a recording As you can see given the lifetime of the job and the job size semantics reliability becomes that much more important in the context of training uh workload infrastructure. if you see these guys are um these researchers are creating are innovating in the model architecture or the model capabilities right let's go through a typical research life cycle researchers are um reading papers, understanding the latest model innovations. Um based on the directions identified the proposals result in a in in they move on to experimentation phase which may involve ablations sweeps hyperparameter sweeps and u new model architecture innovations where you need to modify the code and and prove that the architecture works. Eventually when everything settles down you go into your scale run mode meaning you're now ready to launch your workload on on on hundreds or thousands of GPUs based on your based on the models require compute requirements right once this process finishes the final

### Excerpt da transcript

Welcome everybody. Uh hope you are having a good time here at CubeCon and um today we are going to share how we built a AI HPC cluster on the top of Kubernetes in public cloud. Uh so quick introduction my name is Chandraan Abdut I'm a production engineer at Meta and my co-presenter Kalen Saledi uh he's a software engineer uh he couldn't be here in person today uh but for his part of the presentation we have a recording that we are going to play uh we both work on uh different teams but our team collaborate together to uh build and uh operate uh AHPC the cluster for research in public cloud. So today we'll go over uh like overview of a IML training how it looks like what are the uh in infrastructure requirements for running uh AIPC workloads uh running slum on communities and uh node node life cycle management and uh some of the storage aspects of the cluster. So with that I'm going to uh play a recording. Uh so first part of the session is called by Kalyan. So I'm just going to uh start the uh video recording.

Thank you Chandan. Uh hello everyone. My name is Kalyan. I'm a software engineer in research infrastructure team at MA. Sorry I couldn't be there in person at CubeCon this year, but I'm uh I partnered with Chandan to help you understand what ML training and research space looks like and what does it take to build a performant and uh uh highly productive research cluster in the cloud using Kubernetes. So let's move on and try to understand what ML training is at a high level. This is a oversimplified picture but you can imagine a training loop typically in PyTorch um deployed on a bunch of uh GPUs right each of these GPUs is operating on data um training data samples and iteratively computing and refining the weights. This goes on for a while eventually resulting in a set of weights that that would be called a model right the model is going to be released for production or for open sourcing right uh to give you um uh what are the examples of models like llama mistral GPT photo you all might be familiar with right um before we understand what does it take to build uh ML research cluster in the cloud it's very important to understand what are how does it differ from traditional workloads, right?

Uh I'll focus on three dimensions here. Number one, runtime or lifetime of the job. As opposed to web services where the requests take a few milliseconds or hundreds of milliseconds, right here, the jobs run for any anywhere from hours to weeks to months in so
