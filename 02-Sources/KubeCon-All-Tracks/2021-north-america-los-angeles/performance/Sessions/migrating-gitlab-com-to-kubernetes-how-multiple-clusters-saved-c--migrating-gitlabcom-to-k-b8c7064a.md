---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["John Skarbek", "Gitlab"]
sched_url: https://kccncna2021.sched.com/event/lV50/migrating-gitlabcom-to-kubernetes-how-multiple-clusters-saved-cost-john-skarbek-gitlab
youtube_search_url: https://www.youtube.com/results?search_query=Migrating+GitLab.com+to+Kubernetes%3A+How+Multiple+Clusters+Saved+Cost+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Migrating GitLab.com to Kubernetes: How Multiple Clusters Saved Cost - John Skarbek, Gitlab

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: John Skarbek, Gitlab
- Schedule: https://kccncna2021.sched.com/event/lV50/migrating-gitlabcom-to-kubernetes-how-multiple-clusters-saved-cost-john-skarbek-gitlab
- Busca YouTube: https://www.youtube.com/results?search_query=Migrating+GitLab.com+to+Kubernetes%3A+How+Multiple+Clusters+Saved+Cost+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Migrating GitLab.com to Kubernetes: How Multiple Clusters Saved Cost.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV50/migrating-gitlabcom-to-kubernetes-how-multiple-clusters-saved-cost-john-skarbek-gitlab
- YouTube search: https://www.youtube.com/results?search_query=Migrating+GitLab.com+to+Kubernetes%3A+How+Multiple+Clusters+Saved+Cost+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ie23wHFkEmI
- YouTube title: Migrating GitLab.com to Kubernetes: How Multiple Clusters Saved Cost - John Skarbek, Gitlab
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/migrating-gitlab-com-to-kubernetes-how-multiple-clusters-saved-cost/ie23wHFkEmI.txt
- Transcript chars: 17000
- Keywords: clusters, cluster, infrastructure, traffic, inside, cost, network, little, gitlab.com, course, having, deploy, deployed, started, within, workloads, across, ingress

### Resumo baseado na transcript

so again my name is john scarbeck and i'm going to have a conversation with you all regarding how gitlab.com has added additional clusters to their infrastructure to reduce overall cloud costs so i am john scarbeck i'm a site reliability engineer for get lab specifically on the delivery team i've been with gaylab for about three years and as you can see from this image i'm also a beekeeper sometimes in this conversation i'm going to talk a little bit about how gitlab.com got started with kubernetes um i'm

### Excerpt da transcript

so again my name is john scarbeck and i'm going to have a conversation with you all regarding how gitlab.com has added additional clusters to their infrastructure to reduce overall cloud costs so i am john scarbeck i'm a site reliability engineer for get lab specifically on the delivery team i've been with gaylab for about three years and as you can see from this image i'm also a beekeeper sometimes in this conversation i'm going to talk a little bit about how gitlab.com got started with kubernetes um i'm going to talk a little bit about how one of the problems that we encountered with cloud costs and how we got set up initially i will then dive into the solution that we chose to go about solving that problem and some of the wins that we got with the solution that we had chosen so firstly what is gitlab.com we are the get lab product itself at sas scale so you know we're serving roughly 2 million plus customers at this moment it took us a while to get started in kubernetes land we've got a large infrastructure we've had to scale out quite vastly over the course of time and in doing so our infrastructure team has had to break up parts of our infrastructure into smaller chunks in order to be make it a little easier for us to fully manage that large infrastructure at the scale that we operate at the same time we've also had customer demand to create a helm chart that would enable us to or enable customers rather to install an entire gitlab application on premise inside of their existing kubernetes clusters so with those two building blocks in place we've been able to get our feet wet within kubernetes and at this point we now have today we have a hybrid architecture both virtual machines that are still managed via terraform and chef and we now have about 90 of our front end workloads are inside of kubernetes at this point would have done a few more services but i decided to stress myself out and do a talk so here i am so when it came to getting started with kubernetes our infrastructure team needed a way to simply or create a cluster very quickly without having to work terribly hard we did not want to go the route of using our existing infrastructure management practices to build clusters manage the upgrades and figure out how to troubleshoot them and such we wanted to do something very quickly we wanted to get customer workloads inside of kubernetes as quickly as possible so with that we use google's cloud platform as our infrastructure provider so it was ve
