---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Klaus Ma", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwR/project-lightning-talk-extend-large-language-model-training-beyond-single-kubernetes-cluster-klaus-ma-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Extend+Large+Language+Model+Training+Beyond+Single+Kubernetes+Cluster+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Extend Large Language Model Training Beyond Single Kubernetes Cluster - Klaus Ma, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Klaus Ma, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwR/project-lightning-talk-extend-large-language-model-training-beyond-single-kubernetes-cluster-klaus-ma-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Extend+Large+Language+Model+Training+Beyond+Single+Kubernetes+Cluster+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Extend Large Language Model Training Beyond Single Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwR/project-lightning-talk-extend-large-language-model-training-beyond-single-kubernetes-cluster-klaus-ma-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Extend+Large+Language+Model+Training+Beyond+Single+Kubernetes+Cluster+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BlzHv9KV1Z4
- YouTube title: Project Lightning Talk: Extend Large Language Model Training Beyond Single Kubernetes Cl... Klaus Ma
- Match score: 1.027
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-extend-large-language-model-training-beyond-sin/BlzHv9KV1Z4.txt
- Transcript chars: 4320
- Keywords: cluster, volcano, information, several, single, enough, handle, network, language, resource, utilization, infrastructure, federation, provide, gpu, second, framework, networking

### Resumo baseado na transcript

Uh this is Klaus from uh Nvidia and uh my jit hub ID is K82CN and I'm the I'm the founder of volcano project and used to be the co-chair of six scaling. So I'm going to give a really quick introduction about what we have done about uh uh for language model uh to you know for multiple cluster. single cluster so we will provide a unified API for all the case so that's going to be the simple to handle this one and the second one is about networking and storage right for volcano and for the cubes we for for AI uh We can see that on the on the button head that we are going to change all the information networking storage of the workload to the infrastructure layer. So volcano can use this information and al also the volcano global can use this information to you know to place the workload better for the all the workload and so we can improve the resource utilization and get a better performance for the things.

### Excerpt da transcript

Okay, let's start. Uh this is Klaus from uh Nvidia and uh my jit hub ID is K82CN and I'm the I'm the founder of volcano project and used to be the co-chair of six scaling. So I'm going to give a really quick introduction about what we have done about uh uh for language model uh to you know for multiple cluster. Now the first one is that we why we have such kind of activity to enhance the Kubernetes and enhance the volcano to to do that. You know the first one is that for language modeling we also is say that we we don't have enough results right we have really large cluster we have requirement of lots of uh GPU hardware and the network uh network things now the first one I think the challenge is the single cluster the scalability of single cluster is not enough right the by default is 5,000 but for language model there's going to be require lots of uh GPU hardware the second one is that we you know when we have enough GPU or we have enough network but how about the resource utilization if they didn't have a good uh resource utilization I think the performance is also not good enough I think the third one maybe the a kind of new topic is that we have several framework right parch several enhancement but lots of framework didn't talk with the infrastructure layer right they didn't export the information or how the data was exchanged between the agent and infrastructure didn't know that right the kubernetes volcano didn't know that information so they it's hard for them to you know to do the improvement to do any improvement for that and we just guess right okay the first one is I think for the federation for the multicluster is a really how to say really long topic we have several topic about federation I I think it's about five or 10 years ago right there several challenge things and we try to handle them in our in our inino project.

So the first one is API right uh for federation they try to keep the backward compatibility of uh several APIs such as deployment several things but in volcano we have a single project right volcano global for federation case and volcano core part for single cluster so we will provide a unified API for all the case so that's going to be the simple to handle this one and the second one is about networking and storage right for volcano and for the cubes we for for AI uh scenario we focus on the we we d we dedicated this part to you know to other project I think the major thing is that we are going to have a a powerful really pow
