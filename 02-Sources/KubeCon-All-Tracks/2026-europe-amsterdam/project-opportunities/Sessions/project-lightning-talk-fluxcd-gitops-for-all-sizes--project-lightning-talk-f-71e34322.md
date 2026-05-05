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
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Matheus Pimenta", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyN/project-lightning-talk-fluxcd-gitops-for-all-sizes-matheus-pimenta-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+FluxCD+-+Gitops+For+All+Sizes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: FluxCD - Gitops For All Sizes - Matheus Pimenta, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matheus Pimenta, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyN/project-lightning-talk-fluxcd-gitops-for-all-sizes-matheus-pimenta-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+FluxCD+-+Gitops+For+All+Sizes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: FluxCD - Gitops For All Sizes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyN/project-lightning-talk-fluxcd-gitops-for-all-sizes-matheus-pimenta-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+FluxCD+-+Gitops+For+All+Sizes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qln3o8Ol7pQ
- YouTube title: Project Lightning Talk: FluxCD - Gitops For All Sizes - Matheus Pimenta, Maintainer
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-fluxcd-gitops-for-all-sizes/qln3o8Ol7pQ.txt
- Transcript chars: 5209
- Keywords: flux, cluster, resources, everything, manage, designed, security, clusters, declaratively, support, released, server, feature, expressions, recently, operator, thanks, control

### Resumo baseado na transcript

And the scenario is um you do devops uh ML ops, AI ops uh in and uh you need tools that we give you the the proper um best practices right everything has to work so with flux you can achieve that you can automate your CI/CD pipelines uh it's a githops tool so you reconcile the state of your cluster from from git, right? Uh so uh also because um yeah so it like the the way it can perform drift detection for you uh it's uh pretty good in in how Helm was designed. So this is a feature from Kubernetes that allows you to play nice with other tools, right? And uh Kubernetes build server side apply for for making this nicer um and and Flux has this natively. So you can like um in the ecosystem uh there like there are many different uh tools that you have to deal with and they don't like various uh Kubernetes controllers and they the way they um express the the healthy of their resources in the Kubernetes status field in in the in the state can vary.

### Excerpt da transcript

Hello everybody. Uh, thanks for being here today. My name is Matos Pimementa. I am a Flux maintainer and I work for control plane. Uh, so we're here today to talk about Flux. And the scenario is um you do devops uh ML ops, AI ops uh in and uh you need tools that we give you the the proper um best practices right everything has to work so with flux you can achieve that you can automate your CI/CD pipelines uh it's a githops tool so you reconcile the state of your cluster from from git, right? And uh it's designed for uh performance security. It integrates very well with the Kubernetes security model. It's designed as a set of Kubernetes controllers. So it has very comprehensive uh APIs, CRDs, right? So and it's also very lightweight. Um and Flux is trusted by uh several large orgs. For example, uh Azure and AWS. Azure even has like uh Flux extension uh in their marketplace that you can uh install in your Azure clusters. Also, for example, in the telco space, um uh many telco uh companies adopt flux. They even have this uh open source project on top of Flux which is called Silva.

It's like um it provisions for you this u management cluster that allows uh managing workload clusters. They they give uh a talk about it today in Flux Con. Really cool. Also very large uh financial in institutions uh adopt flux for it ability to scale right like because um obviously manual operations don't scale right and flux makes it possible for you to manage uh hundreds of clusters declaratively via GitHubs. So that's why it's uh trusted by uh all these organizations. Uh so yeah uh we put the the effort so you don't have to and uh so a few features and abilities that flux has for example I believe it has the best uh helm support in the landscape um we have uh a deep integration with the helm SDK we uh just released support for helm for which came out uh late last year and uh yeah we're worked with the with the helm project to to get this done. They were really helpful. Thank you. Uh so uh also because um yeah so it like the the way it can perform drift detection for you uh it's uh pretty good in in how Helm was designed.

So yeah uh also Flux uses server side apply natively. So this is a feature from Kubernetes that allows you to play nice with other tools, right? It's always a chaos when uh multiple tools are trying to manage the same resources inside the cluster. And uh Kubernetes build server side apply for for making this nicer um and and Flux has this natively. Also we ar
