---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Stefan Prodan", "ControlPlane"]
sched_url: https://kccnceu2026.sched.com/event/2EF4I/visualizing-gitops-a-tour-of-flux-uis-in-the-open-source-ecosystem-stefan-prodan-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Visualizing+GitOps%3A+A+Tour+of+Flux+UIs+in+the+Open+Source+Ecosystem+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Visualizing GitOps: A Tour of Flux UIs in the Open Source Ecosystem - Stefan Prodan, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Stefan Prodan, ControlPlane
- Schedule: https://kccnceu2026.sched.com/event/2EF4I/visualizing-gitops-a-tour-of-flux-uis-in-the-open-source-ecosystem-stefan-prodan-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Visualizing+GitOps%3A+A+Tour+of+Flux+UIs+in+the+Open+Source+Ecosystem+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Visualizing GitOps: A Tour of Flux UIs in the Open Source Ecosystem.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4I/visualizing-gitops-a-tour-of-flux-uis-in-the-open-source-ecosystem-stefan-prodan-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Visualizing+GitOps%3A+A+Tour+of+Flux+UIs+in+the+Open+Source+Ecosystem+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pSfmhblzE-Y
- YouTube title: Visualizing GitOps: A Tour of Flux UIs in the Open Source Ecosystem - Stefan Prodan, ControlPlane
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/visualizing-gitops-a-tour-of-flux-uis-in-the-open-source-ecosystem/pSfmhblzE-Y.txt
- Transcript chars: 24877
- Keywords: flux, cluster, release, everything, custom, controller, inside, operator, artifact, around, releases, having, another, resource, source, months, changes, resources

### Resumo baseado na transcript

So uh today I would like to give you like an overview of what's happening in the ecosystem around flux with all the UIs that we have and I'll try to uh show you the UI that I'm contributing to. Uh but before we go into that I would like to give you a short overview of u what we shipped in uh the last uh flux release. Um also from a security point of view we need to ensure the charts are sealed inside the controller so they can't escape. So we have a different security posture when it comes to integrating helm. We basically focused uh almost 3 months on this migration and I'm very very happy with what's happening right now in Helm we finally have Kubernetes serverside apply. If you have been a flux user for a long time, you know that um in flux we've adopted serverside apply when it was alpha in kubernetes and we we gave a lot of feedback to the kubernetes maintainers to make it uh better.

### Excerpt da transcript

Hello everyone. Congrats for making it to the last day of CubeCon. Yay. I almost didn't made it. I was like, hard night. Okay. So uh today I would like to give you like an overview of what's happening in the ecosystem around flux with all the UIs that we have and I'll try to uh show you the UI that I'm contributing to. Uh but before we go into that I would like to give you a short overview of u what we shipped in uh the last uh flux release. So we have 2.8 going GA. Um we do three releases per year um after each Kubernetes release and we usually skip the one in December because we don't want to you know spend Christmas uh dealing with client go not matching coign client go not matching helm client go and so on. Um so what we did in in 2.8 The the biggest thing that we pulled off was we finally have Helm before support. Um I want to thank the Helm team for working with us all these months to make it happen. Um Flux as you know has um native Helm support. What this means is that we don't use Helm as a templating um thing.

We actually use the helm go SDK inside flux. So everything has to be we rebuild all the flag all the helm actions and we improve the life cycle um inside helm controller and that means we are like tightly coupled inside helm controller with the helm SDK and if something changes upstream we have to make sure those changes are compatible with what we do in flux and our main main concern is always performance from you know a helm cli perspective If if you use Helm to deploy on a cluster, you'll probably run it in a CI runner, right? You don't care if it uh takes uh one minute instead of 20 seconds or if it uses I don't know how much memory is there is just a CLI call is one Helm release that you are installing or upgrading. Um flux is very different. We have to ensure we can upgrade hundreds of hand releases in parallel. We really care about you know the how many resources these are using how many queries to the cluster. Um also from a security point of view we need to ensure the charts are sealed inside the controller so they can't escape.

So we have a different security posture when it comes to integrating helm. So for us these kind of releases are a major disruptor. We basically focused uh almost 3 months on this migration and I'm very very happy with what's happening right now in Helm we finally have Kubernetes serverside apply. If you have been a flux user for a long time, you know that um in flux we've adopted serverside apply when it
