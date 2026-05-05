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
speakers: ["Andy Anderson", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvZ/project-lightning-talk-multi-cluster-configuration-management-with-kubestellar-andy-anderson-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Configuration+Management+with+KubeStellar+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Multi-Cluster Configuration Management with KubeStellar - Andy Anderson, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Andy Anderson, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvZ/project-lightning-talk-multi-cluster-configuration-management-with-kubestellar-andy-anderson-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Configuration+Management+with+KubeStellar+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Multi-Cluster Configuration Management with KubeStellar.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvZ/project-lightning-talk-multi-cluster-configuration-management-with-kubestellar-andy-anderson-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Configuration+Management+with+KubeStellar+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tHMKF5sUSgI
- YouTube title: Project Lightning Talk: Multi-Cluster Configuration Management With KubeStellar - Andy Anderson
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-multi-cluster-configuration-management-with-kub/tHMKF5sUSgI.txt
- Transcript chars: 5950
- Keywords: clusters, allows, workload, stellar, workloads, inventory, working, cluster, cuddle, across, configuration, management, coupube, multicluster, anderson, software, descriptor, execution

### Resumo baseado na transcript

So for basics of what coupe stellar is you have an inventory of remote managed work clusters and you have a workload namespaces where you stage your workloads and that allows you to put workloads into a namespace where pods don't run and you can then say I want to connect this workload with this cluster. Okay so in coupe stellar you define an inventory a workload descriptor space and a workload execution clusters. We get a lot of draw from around the the uh the world uh on joining us and and learning how to code against Kubernetes.

### Excerpt da transcript

Okay, so what I'm here to talk to you today about is coupube stellar. It's a multicluster configuration management tool. Uh we've been in the CNCF for quite a while. My name is Andy Anderson. You can find me at club Anderson. I'm a software architect for IBM research. So the ven diagram long used by many of us to describe. So for basics of what coupe stellar is you have an inventory of remote managed work clusters and you have a workload namespaces where you stage your workloads and that allows you to put workloads into a namespace where pods don't run and you can then say I want to connect this workload with this cluster. Okay so in coupe stellar you define an inventory a workload descriptor space and a workload execution clusters. You add those clusters to your your train uh your uh inventory. Then you add workloads to your workload descriptor space and then you assign them via binding policy. Okay. So this is allows you to have a very small size cluster where you centralize all your workloads and then you distribute them via policy and when they are sent out to the workload execution clusters they spin up.

This is the API point of view. Uh we use the SIG M uh multiclusters workload API uh as uh as our u main mode of communication back and forth between the inventory transport space and the definition spaces. This is allows us to do things that Kubernetes doesn't naturally allow because it it times out after some time. You know, if a cluster goes offline uh after a few minutes it's marked unschedulable. Well, Kubstellar gets around that. Some of the newest things that we've been working on at Coupe Stellar are things like localization. We're now localized in English, French, Italian, German, Spanish, Japanese, Hindi, traditional and simplified Chinese, and Portuguese. Bring your language. We're happy to do it. Only took a couple weeks to do this. It was great effort uh for the team. We've got a new website that's coming out, localiz localization help wanted there. Um we have a build your own multicluster plugin uh with our new plug-in framework. You can create plugins for our UI and distribute them to your uh your favorite adopter.

We also automated our multi browser UI testing with playright. Uh and we have now what we call the multi-plugin for coupube cuddle allows you to work with multiple clusters from the command line. So if you do a coupe cuddle get pods- a it'll give you all the pods that are running and all the clusters and all the uh contexts
