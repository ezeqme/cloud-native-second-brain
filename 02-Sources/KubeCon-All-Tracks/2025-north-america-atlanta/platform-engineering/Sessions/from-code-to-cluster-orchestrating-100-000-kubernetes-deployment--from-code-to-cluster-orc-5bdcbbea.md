---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Andrada Raducanu", "ING Hubs Romania"]
sched_url: https://kccncna2025.sched.com/event/27Ff8/from-code-to-cluster-orchestrating-100000+-kubernetes-deployments-with-1-pipeline-andrada-raducanu-ing-hubs-romania
youtube_search_url: https://www.youtube.com/results?search_query=From+Code+To+Cluster%3A+Orchestrating+100%2C000%2B+Kubernetes+Deployments+With+1+Pipeline+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Code To Cluster: Orchestrating 100,000+ Kubernetes Deployments With 1 Pipeline - Andrada Raducanu, ING Hubs Romania

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Andrada Raducanu, ING Hubs Romania
- Schedule: https://kccncna2025.sched.com/event/27Ff8/from-code-to-cluster-orchestrating-100000+-kubernetes-deployments-with-1-pipeline-andrada-raducanu-ing-hubs-romania
- Busca YouTube: https://www.youtube.com/results?search_query=From+Code+To+Cluster%3A+Orchestrating+100%2C000%2B+Kubernetes+Deployments+With+1+Pipeline+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Code To Cluster: Orchestrating 100,000+ Kubernetes Deployments With 1 Pipeline.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Ff8/from-code-to-cluster-orchestrating-100000+-kubernetes-deployments-with-1-pipeline-andrada-raducanu-ing-hubs-romania
- YouTube search: https://www.youtube.com/results?search_query=From+Code+To+Cluster%3A+Orchestrating+100%2C000%2B+Kubernetes+Deployments+With+1+Pipeline+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cO4f7-JDG0Y
- YouTube title: From Code To Cluster: Orchestrating 100,000+ Kubernetes Deployments With 1 Pipel... Andrada Raducanu
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-code-to-cluster-orchestrating-100-000-kubernetes-deployments-with/cO4f7-JDG0Y.txt
- Transcript chars: 23160
- Keywords: pipeline, application, configuration, version, deployment, canary, release, applications, certificate, autoscaler, actually, docker, lastly, organization, features, templates, namespace, around

### Resumo baseado na transcript

Thank you very much for being here and especially thank you for sticking to the not only the very end of the pres of the conference, the end of the last day and for choosing to come to this session. Uh lay back, relax and allow me to tell you the story of how we go from code to cluster in my organization. And finally, you will see a recorded demo of the pipeline because I lost my face in the demo guts. However, the number of deployments was being reduced to focus more on the resilience and reliability of how those deployments were happening. It can benchmark your application, run performances and some other features. To complement the Kings Road pipeline offers you the templates directory which contain every uh template for the Kubernetes objects you're going to need for your release and the chart information.

### Excerpt da transcript

Okay, hello everyone. Thank you very much for being here and especially thank you for sticking to the not only the very end of the pres of the conference, the end of the last day and for choosing to come to this session. Uh lay back, relax and allow me to tell you the story of how we go from code to cluster in my organization. My name is Andrada and for the past five years I've been working with ING Hubs Romania as a DevOps engineer. To clear a bit things up, what is ING Hubs Romania? We are part of the broader Dutch ING group which is a global bank with a strong European base. The hub in Romania where I work at delivers solution in software development, data management, compliancy, non-financial risk management to other hubs in to other units of ING worldwide. I'm not going to tell you about that. I'm going to tell you about the pipeline. Uh the agenda for the next half hour is going to look like this. I'm going to tell you about the context, what was happening in the organization around five years ago and how we got here.

We're going to look at the solution layout, its building blocks in how it actually looks like. Uh I'm going to tell you about some of the features we implement and some of the ones we built. Second to last, we're going to look a bit at the risks and how we dealt with them. And finally, you will see a recorded demo of the pipeline because I lost my face in the demo guts. I'm not taking any chances. Hopefully, we're going to have time for a few uh Q&A for a few questions at the very end. The context. It was 2019 when inside our organization a technology shift was happening. The stack consisting of GitLab, Jenkins, TFS, and Enible tower was being replaced with Asia DevOps and Open Shift. Due to this applications were being migrated from VMs to containers. Uh before this engineers will would create the pipelines however they saw fit but they were respecting some guidelines and policies. A need for a more standard deployment approach was identified. To take advantage of this a small group of engineers collaborated with the developers of a tier zero application from ING to create a P.

The idea to create the Kings Road pipeline was born then. If we were successful with a very complex application like that one, we would be successful with all of them. The next year in 2020, the tier zero application went live in production in ING's private cloud using the Kings Road pipeline. They became our main promoter and soon other applications and teams
