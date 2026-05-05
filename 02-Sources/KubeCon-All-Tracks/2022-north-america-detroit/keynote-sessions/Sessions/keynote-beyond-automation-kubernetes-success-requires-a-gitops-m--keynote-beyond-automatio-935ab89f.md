---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Keynote Sessions"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Shatarupa Nandi", "Senior Director of Engineering", "VMware Tanzu"]
sched_url: https://kccncna2022.sched.com/event/182LA/keynote-beyond-automation-kubernetes-success-requires-a-gitops-mindset-shatarupa-nandi-senior-director-of-engineering-vmware-tanzu
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Beyond+Automation%3A+Kubernetes+Success+Requires+a+GitOps+Mindset+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Keynote: Beyond Automation: Kubernetes Success Requires a GitOps Mindset - Shatarupa Nandi, Senior Director of Engineering, VMware Tanzu

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Shatarupa Nandi, Senior Director of Engineering, VMware Tanzu
- Schedule: https://kccncna2022.sched.com/event/182LA/keynote-beyond-automation-kubernetes-success-requires-a-gitops-mindset-shatarupa-nandi-senior-director-of-engineering-vmware-tanzu
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Beyond+Automation%3A+Kubernetes+Success+Requires+a+GitOps+Mindset+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Keynote: Beyond Automation: Kubernetes Success Requires a GitOps Mindset.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182LA/keynote-beyond-automation-kubernetes-success-requires-a-gitops-mindset-shatarupa-nandi-senior-director-of-engineering-vmware-tanzu
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Beyond+Automation%3A+Kubernetes+Success+Requires+a+GitOps+Mindset+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8xg5SE3kO3Y
- YouTube title: Keynote: Beyond Automation: Kubernetes Success Requires a GitOps Mindset - Shatarupa Nandi
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keynote-beyond-automation-kubernetes-success-requires-a-gitops-mindset/8xg5SE3kO3Y.txt
- Transcript chars: 5388
- Keywords: clusters, configuration, software, carvel, production, applications, development, controller, platform, operations, mindset, following, scripts, various, get-offs, started, minutes, overlays

### Resumo baseado na transcript

hi everyone I'm chaparrupa I work on Project carvo where our goal is to provide a set of Reliable Tools that help you automate and run your software in production and today I want to share a real world story about a platform operations team that's been able to manage over 30 clusters and several applications in production in a highly regulated environment using the carpool tool chain but before that I cannot contain my excitement and I have to share that project Carvel was just accepted as a Sandbox

### Excerpt da transcript

hi everyone I'm chaparrupa I work on Project carvo where our goal is to provide a set of Reliable Tools that help you automate and run your software in production and today I want to share a real world story about a platform operations team that's been able to manage over 30 clusters and several applications in production in a highly regulated environment using the carpool tool chain but before that I cannot contain my excitement and I have to share that project Carvel was just accepted as a Sandbox project in the cncf and I am so happy to be here today saying that okay now back to the story um so let me talk a little bit about the challenges that this team faced on their production Journey so first their applications have complex deployment topologies so installing these applications by following a Playbook of scripts was toil heavy it was error prone and their development teams really didn't like that experience they the development teams didn't have the right level of access to run these scripts they didn't know where to run the scripts from and managing fine-grained access was hard for the platform operations team as all a lot of us today do they also depended on a lot of Open Source software on third-party software and they needed to have a way to ensure that the software was built securely it was easily accessible in their various environments and it was easily customizable security compliance reliability is really important to this team so this team knew that the least error prone and the most user-friendly way to satisfy these criteria was to do so programmatically they knew they wanted to adopt the get-offs mindset for managing their clusters and what really resonated with them about the get-offs mindset was this idea of deploying continuously declaratively and doing so collaboratively as an organization so what did they do the team first started to keep configuration in the central git repository this repository became a central point of collaboration for the entire organization they could Source changes to this repo from various teams then they started relying on Carvel's package manager cap controller to create clusters following this configuration now they could make a single change in their configuration and Cat controller would automatically roll it out to their many clusters previously updates of this kind took days of coordinative coordinated effort across multiple development teams but now they were able to update their applications and t
