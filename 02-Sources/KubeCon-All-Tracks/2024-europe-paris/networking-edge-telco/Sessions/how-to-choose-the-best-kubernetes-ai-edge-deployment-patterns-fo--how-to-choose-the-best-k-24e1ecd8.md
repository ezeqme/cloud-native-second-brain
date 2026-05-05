---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["AI ML", "Networking", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Jacqueline Koehler", "Myriam Fentanes Gutierrez", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YeMb/how-to-choose-the-best-kubernetes-ai-edge-deployment-patterns-for-your-use-case-jacqueline-koehler-myriam-fentanes-gutierrez-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Choose+the+Best+Kubernetes+AI+Edge+Deployment+Patterns+for+Your+Use+Case+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How to Choose the Best Kubernetes AI Edge Deployment Patterns for Your Use Case - Jacqueline Koehler & Myriam Fentanes Gutierrez, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[AI ML]], [[Networking]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Jacqueline Koehler, Myriam Fentanes Gutierrez, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YeMb/how-to-choose-the-best-kubernetes-ai-edge-deployment-patterns-for-your-use-case-jacqueline-koehler-myriam-fentanes-gutierrez-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Choose+the+Best+Kubernetes+AI+Edge+Deployment+Patterns+for+Your+Use+Case+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How to Choose the Best Kubernetes AI Edge Deployment Patterns for Your Use Case.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMb/how-to-choose-the-best-kubernetes-ai-edge-deployment-patterns-for-your-use-case-jacqueline-koehler-myriam-fentanes-gutierrez-red-hat
- YouTube search: https://www.youtube.com/results?search_query=How+to+Choose+the+Best+Kubernetes+AI+Edge+Deployment+Patterns+for+Your+Use+Case+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jVmbpo-NGDg
- YouTube title: How to Choose the Best Kubernetes AI Edge Deployment Patterns for Your Use Case
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-to-choose-the-best-kubernetes-ai-edge-deployment-patterns-for-your/jVmbpo-NGDg.txt
- Transcript chars: 22214
- Keywords: challenges, computing, management, environment, controller, customers, solution, manage, workloads, important, models, repository, constantly, inference, container, deploy, decided, everything

### Resumo baseado na transcript

thank you so much for coming to the session I see a lot of familiar faces I hope you guys like it um so we're going to talk about how to choose the best kubernetes to deploy AI workloads at the edge uh we're going to talk a little bit more about how to deploy itself um and my name is Miriam fanis I am product manager with the open shift AI be you and red hat and um I I think this works yes uh I'm Jacqueline Kohler and

### Excerpt da transcript

thank you so much for coming to the session I see a lot of familiar faces I hope you guys like it um so we're going to talk about how to choose the best kubernetes to deploy AI workloads at the edge uh we're going to talk a little bit more about how to deploy itself um and my name is Miriam fanis I am product manager with the open shift AI be you and red hat and um I I think this works yes uh I'm Jacqueline Kohler and I'm a senior manager at red hat for the engineering team yes so what we're going to see in this session is uh first of all we want to give you our definition of edge we know that everyone has their favorite but we want to kind of tell you where our mind is and that uh some use cases that we have seen with different customers on Telco and that can be used as a pattern uh from other for other Industries and then the challenges that we have seen when they are trying to productize AI workloads so the challenges with serving managing monitoring uh and observability of these workloads at the edge uh we're going to see in a little bit more detail the life cycle of the model how do we solve some of the management uh challenges uh the observability and at the end we want to give you the general picture of how we have implemented uh our solution so we're going to start with what is Edge uh that is a very overloaded term uh we decided to take to take the more simplistic approach to it uh which is Edge is everything that is outside of the data center there are a lot of companies that have been doing Edge for a very long time and they don't call it Edge so like retail they have they have had uh servers on the stores for a very long time and they never thought about it as Edge um but now we are seeing that it's more and more important to put powerful Computing at the edge and that's what is Edge Computing um and basically uh the reason why we are seeing a lot more interest in Edge Computing lately it's because of all of the challenges that you have when you have the data sources very far from where you want to do the Computing and all of the costs associated with moving that data between the source and whatever you want to do the analytics and these costs can be uh you know monetary so moving all that data it's it's expensive but also in terms of latency uh when you have applications that require really low latens like um VR and video games or or things that interact with end users uh latency is super important and also you know at the edge we tend to see
