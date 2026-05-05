---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Arka Saha", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyH/project-lightning-talk-lets-deploy-etcd-operator-arka-saha-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Let%E2%80%99s+Deploy+etcd+Operator+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Let’s Deploy etcd Operator - Arka Saha, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Arka Saha, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyH/project-lightning-talk-lets-deploy-etcd-operator-arka-saha-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Let%E2%80%99s+Deploy+etcd+Operator+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Let’s Deploy etcd Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyH/project-lightning-talk-lets-deploy-etcd-operator-arka-saha-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Let%E2%80%99s+Deploy+etcd+Operator+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FBV-fkNwyMU
- YouTube title: Project Lightning Talk: Let’s Deploy etcd Operator - Arka Saha, Maintainer
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-lets-deploy-etcd-operator/FBV-fkNwyMU.txt
- Transcript chars: 4616
- Keywords: operator, certificate, basically, cluster, manager, search, clusters, production, members, issuer, deploy, actually, started, address, scaling, environments, object, member

### Resumo baseado na transcript

Uh I am Orco Shaha from Broadcom uh software engineer and I'm also a reviewer in the city operator project. So let's look at uh what city operator is and why do we actually need it. So uh let's quickly jump into the demo of how uh like we can start uh using the city operator. Similarly, we have the function of scaling uh in which is basically yeah, if we have the uh seven member cluster like in the previous uh situation, we can scale it down to uh three members and that we can actually do an edit on the object and it will reconcile. So as we can see in the uh demo uh GIF that yes the certificate manager creates the certificates as well as the secret link to it and it will mount to the pods.

### Excerpt da transcript

Hi everyone. Uh I am Orco Shaha from Broadcom uh software engineer and I'm also a reviewer in the city operator project. So let's look at uh what city operator is and why do we actually need it. So in initially uh when people started using HCD clusters uh there was a problem that nobody started solving uh as a community was that uh basically managing those HCD clusters like uh there are many things that we will need to do to manage the HCD clusters and nobody was addressing it although we do did have one project in the core OS uh organization but that wasn't completely followed through and all the users started uh building their own operators to uh address those problems. So this uh having the city operator again as a revival project is basically uh to address that we will have one community supported and uh native uh operator which will basically uh address all these pain points that we have with authentication, scaling up and upgrades. And this will be starting off as more to um support your workload applications that runs on Kubernetes than the cubernetes itself.

So we do have two releases. The latest one being 0.2 which was released last week which added the certificate support for um helping the operator to be used in production environments. Although it's not production ready at this moment because we will have uh other releases like uh which will include recovery uh backup as well as the helmchart release. But yeah uh they can like users can start um playing around with it. So uh let's quickly jump into the demo of how uh like we can start uh using the city operator. So the official image that we have the latest one is 0.2 too. But if you want to do a local development on your kind cluster, you can uh just clone the repo, do a docker build, make a docker install and deploy. If you uh just want to try it out, you can just deploy with the uh official image that we have and you will see the city operator controller port coming up as well as the CRD uh city clusters installed. Uh so let's look at how the cluster cluster object looks like. So this is this is like a typical bare minimum uh clust uh cluster object which has the version defined of which at version you want and what is the size of it.

So scaling out will basically mean that we adding more and more members to it. So we have mentioned the size seven. So as we can see uh it keeps adding members until uh it has reached the size. Similarly, we have the function of scaling uh in which is basical
