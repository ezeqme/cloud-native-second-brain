---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8w/k8gb-global-load-balancing-the-kubernetes-way-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=k8gb%3A+Global+Load+Balancing%2C+the+Kubernetes+Way+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# k8gb: Global Load Balancing, the Kubernetes Way | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8w/k8gb-global-load-balancing-the-kubernetes-way-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=k8gb%3A+Global+Load+Balancing%2C+the+Kubernetes+Way+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre k8gb: Global Load Balancing, the Kubernetes Way | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8w/k8gb-global-load-balancing-the-kubernetes-way-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=k8gb%3A+Global+Load+Balancing%2C+the+Kubernetes+Way+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vCzl15AIoU0
- YouTube title: k8gb: Global Load Balancing, the Kubernetes Way | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/k8gb-global-load-balancing-the-kubernetes-way-project-lightning-talk/vCzl15AIoU0.txt
- Transcript chars: 4142
- Keywords: clusters, cluster, ingress, external, application, strategy, applications, controller, balancing, single, according, resource, domain, running, delegation, global, creator, management

### Resumo baseado na transcript

hi everyone my name is Andre uh I'm the latest maintainer of KGB uh you see also Yuri's name in the slides initially we plan to give this talk together he's the creator of KTB uh we were advised to have a single presenter today and he was so kind to let me take the stage today I really appreciate it okay so without further Ado what is KB KB addresses the challenge of global traffic management if your application is deployed in multiple clusters in various regions then KTB

### Excerpt da transcript

hi everyone my name is Andre uh I'm the latest maintainer of KGB uh you see also Yuri's name in the slides initially we plan to give this talk together he's the creator of KTB uh we were advised to have a single presenter today and he was so kind to let me take the stage today I really appreciate it okay so without further Ado what is KB KB addresses the challenge of global traffic management if your application is deployed in multiple clusters in various regions then KTB ensures it is highly available in this example KB will help routing uh we have an application that is uh deployed in three clusters and KB will help routing our users to one of those clusters according to a strategy there are many load balancing solutions that try to solve this problem what's special about KGB KGB is the only Sol solution that is uh that is provider agnostic and that is kubernetes native uh sorry vendor agnostic I meant and we leveraged the kubernetes API to assess the health of applications instead of active probing there is no need for a management cluster no central point of fa single point of failure and everything can be configured with a single custom resource here's how the crd looks like pretty simple we have a resource ref block where you'll select an Ingress resource from where the controller should learn the domain name IP address and pods running our application then we configure a strategy block where we have a load balancing strategy since a few weeks ago months ago actually we also support besides kubernetes Ingress EO Ingress configuration and we have a gateway gateway API in the road map this is actually feature that I developed that got me started in the project and on Friday we have a contri Fest session where we'll walk you through the process of adding New Ingress Integrations and I can promise you it is much much easier than it was when I did it a few months ago let's go over strategies now KTB supports the following strategies round robin either uh with equal weights or different weights per cluster failover where users are routed to a primary cluster if there is an issue with that cluster or the applications running on that cluster users have failed over to other clusters and goip where we route users to clusters according to their location how does this all work KGB leverages the battle tested DNS protocol and two other very stable cncf projects core DNS and external DNS core DNS is used to serve DNS requests external DNS is used to uh config figu
