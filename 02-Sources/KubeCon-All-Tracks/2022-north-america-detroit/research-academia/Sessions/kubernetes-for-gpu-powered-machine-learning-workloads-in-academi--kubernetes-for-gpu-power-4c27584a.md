---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Research + Academia"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Camille Rodriguez", "Canonical", "John-Paul Robinson", "University of Alabama at Birmingham"]
sched_url: https://kccncna2022.sched.com/event/182GK/kubernetes-for-gpu-powered-machine-learning-workloads-in-academia-camille-rodriguez-canonical-john-paul-robinson-university-of-alabama-at-birmingham
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+For+GPU+Powered+Machine+Learning+Workloads+In+Academia+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes For GPU Powered Machine Learning Workloads In Academia - Camille Rodriguez, Canonical & John-Paul Robinson, University of Alabama at Birmingham

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Research + Academia]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Camille Rodriguez, Canonical, John-Paul Robinson, University of Alabama at Birmingham
- Schedule: https://kccncna2022.sched.com/event/182GK/kubernetes-for-gpu-powered-machine-learning-workloads-in-academia-camille-rodriguez-canonical-john-paul-robinson-university-of-alabama-at-birmingham
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+For+GPU+Powered+Machine+Learning+Workloads+In+Academia+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes For GPU Powered Machine Learning Workloads In Academia.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GK/kubernetes-for-gpu-powered-machine-learning-workloads-in-academia-camille-rodriguez-canonical-john-paul-robinson-university-of-alabama-at-birmingham
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+For+GPU+Powered+Machine+Learning+Workloads+In+Academia+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eD73x7IH7lU
- YouTube title: Kubernetes For GPU Powered Machine Learning Workloads In... - Camille Rodriguez & John-Paul Robinson
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-for-gpu-powered-machine-learning-workloads-in-academia/eD73x7IH7lU.txt
- Transcript chars: 27130
- Keywords: environment, platform, cluster, research, essentially, gpu, openstack, applications, university, little, computing, researchers, compute, machine, environments, deploy, specific, resources

### Resumo baseado na transcript

thank you hello everyone so I'm Kimmy uh very happy to be here today so the idea behind this talk is essentially a project that the University of Alabama and canonical did together last winter so at the University they already had an HPC environment and an openstack based environment for their users but in terms of containers all of the different environments were like on laptops containers here and there some Docker swarm over there and the idea was to provide a dedicated kubernetes platform to their users and the same space You Are no great solution thank you so now it's a last question for today uh thanks very much the typically when you are using containers for machine learning projects like this the models or the containers can be very large to

### Excerpt da transcript

thank you hello everyone so I'm Kimmy uh very happy to be here today so the idea behind this talk is essentially a project that the University of Alabama and canonical did together last winter so at the University they already had an HPC environment and an openstack based environment for their users but in terms of containers all of the different environments were like on laptops containers here and there some Docker swarm over there and the idea was to provide a dedicated kubernetes platform to their users and so we worked together to get this done and we're going to go today through the kubernetes architecture that we chose and a few of the Integrations that we've done and then my colleague John Paul will go a little bit more through what type of research they do and and how they leverage that infrastructure for the research so for the kubernetes architecture in this case we're talking about the curving cheese on bare metal deployment so um when we talk about bare metal deployments we want to have some infrastructure nodes you can also call them like management nodes essentially those are outside of the kubernetes deployment to be able to manage the kubernetes environment um so the First Technology I'll highlight here is the metal as a service platform so Mars is a burmesole provisioning tool super useful when you have a large estate of bare metal servers it provides you with your asset inventory you can do a layout of the type of storage layout networking and all of the layout that you want to do when you pixiboot and deploy your servers can be automated through Mass so that was a really useful tool to use um then to choose which machine we're deploying and to deploy them with application to deploy the OS and to deploy different applications we're using Juju um Juju is called also a operator lifecycle controller essentially it's one of the best aspects of it is that there's a lot of day two operations built in so once you deploy applications you can relate them to each other so let's say you want to relate your kubernetes worker to the control plane it's a simple relation in a model that you define in yaml so it makes it simple and when you want to scale your cluster for example you want to add your kubernetes node you can simply do like Juju add unit kubernetes worker and it's going to scale for you you can also reduce you can upgrade and update um so that's the main manager that we're using In This Cloud in terms of observability it's pretty standard
