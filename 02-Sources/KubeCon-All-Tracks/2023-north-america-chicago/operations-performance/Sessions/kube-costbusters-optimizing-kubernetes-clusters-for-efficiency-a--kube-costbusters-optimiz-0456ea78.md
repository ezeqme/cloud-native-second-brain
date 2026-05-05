---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Rachel Leekin", "Antoinette Mills", "AWS"]
sched_url: https://kccncna2023.sched.com/event/1R2r2/kube-costbusters-optimizing-kubernetes-clusters-for-efficiency-and-epic-savings-rachel-leekin-antoinette-mills-aws
youtube_search_url: https://www.youtube.com/results?search_query=Kube-Costbusters%3A+Optimizing+Kubernetes+Clusters+for+Efficiency+and+Epic+Savings%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kube-Costbusters: Optimizing Kubernetes Clusters for Efficiency and Epic Savings! - Rachel Leekin & Antoinette Mills, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Rachel Leekin, Antoinette Mills, AWS
- Schedule: https://kccncna2023.sched.com/event/1R2r2/kube-costbusters-optimizing-kubernetes-clusters-for-efficiency-and-epic-savings-rachel-leekin-antoinette-mills-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Kube-Costbusters%3A+Optimizing+Kubernetes+Clusters+for+Efficiency+and+Epic+Savings%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kube-Costbusters: Optimizing Kubernetes Clusters for Efficiency and Epic Savings!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2r2/kube-costbusters-optimizing-kubernetes-clusters-for-efficiency-and-epic-savings-rachel-leekin-antoinette-mills-aws
- YouTube search: https://www.youtube.com/results?search_query=Kube-Costbusters%3A+Optimizing+Kubernetes+Clusters+for+Efficiency+and+Epic+Savings%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-PPwZEGfac0
- YouTube title: Kube-Costbusters: Optimizing Kubernetes Clusters for Efficiency... Rachel Leekin & Antoinette Mills
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kube-costbusters-optimizing-kubernetes-clusters-for-efficiency-and-epi/-PPwZEGfac0.txt
- Transcript chars: 24324
- Keywords: cost, resources, cluster, storage, talking, rachel, associated, resource, carpenter, clusters, little, hidden, especially, another, automation, consider, details, instance

### Resumo baseado na transcript

all right welcome everyone are you ready to unleash the power of cost driven kuber's optimization all right we're going to embark on an venture to achieve cost optimization and efficiency so we'll jump straight into it because we got a lot of stuff to talk about so meet the Cube cost Buster team I'm Rachel leakin code name razor because I cut through those costs I'll pass it over to my teammate and and I'm Antoinette code name little Gigi means little go-getter some of you who know me

### Excerpt da transcript

all right welcome everyone are you ready to unleash the power of cost driven kuber's optimization all right we're going to embark on an venture to achieve cost optimization and efficiency so we'll jump straight into it because we got a lot of stuff to talk about so meet the Cube cost Buster team I'm Rachel leakin code name razor because I cut through those costs I'll pass it over to my teammate and and I'm Antoinette code name little Gigi means little go-getter some of you who know me know what that means for those who don't by the end of this presentation you will definitely know I earned that name and meet our mascot little cuy so if you see little cuy on the slide that means we want you to pay special attention to this particular information all right let's jump straight into it all right so yeah we're basically here today to share with you a few ghosts that you might be encountering when you as you begin your kubernetes journey but before we go there with the hidden aspects of it Rachel I thought it might be a good idea to review some standard costs that you might have already experienced to date so when we talk about infrastructure in essence what we're really talking about are compute resources and this is where you're build on the number and the types of nodes that you're utilizing and so if you're using managed kubernetes okay and welcome everyone but if you're using managed kubernetes you incur costs for the management and the control plane Services you ingest from your service provider okay so let me pause and think about this so when our kubernetes applications often use persistent storage and the cost depends on the size the type and the duration of that storage um and also when you we're looking at networking what we're looking at are traffic Ingress and egress which also can add significant costs as well okay so for monitoring and logging here we're talking about the cost associated with using tools like Prometheus grafana or commercial U Monitoring Solutions and also there are licensing fees associated with um or reinforcing your security part uh posture in your kubernetes space as well okay so I know all of us in here knows that the complexity of building maintaining a kubernetes environment developing applications are fairly complex and so the talent needed to uh maintain and build these and develop in this in this environment um associated with attracting that talent and keeping that Talent may be significant as well so you need to consid
