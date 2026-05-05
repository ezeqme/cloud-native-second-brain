---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Deepak Kosaraju", "James Dabbs", "Procore"]
sched_url: https://kccncna2025.sched.com/event/27FXj/zero-downtime-migration-of-monolith-to-k8s-using-sidecar-and-container-lifecycle-hooks-deepak-kosaraju-james-dabbs-procore
youtube_search_url: https://www.youtube.com/results?search_query=Zero+Downtime+Migration+of+Monolith+To+K8s+Using+Sidecar+and+Container+Lifecycle+Hooks+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Zero Downtime Migration of Monolith To K8s Using Sidecar and Container Lifecycle Hooks - Deepak Kosaraju & James Dabbs, Procore

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Deepak Kosaraju, James Dabbs, Procore
- Schedule: https://kccncna2025.sched.com/event/27FXj/zero-downtime-migration-of-monolith-to-k8s-using-sidecar-and-container-lifecycle-hooks-deepak-kosaraju-james-dabbs-procore
- Busca YouTube: https://www.youtube.com/results?search_query=Zero+Downtime+Migration+of+Monolith+To+K8s+Using+Sidecar+and+Container+Lifecycle+Hooks+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Zero Downtime Migration of Monolith To K8s Using Sidecar and Container Lifecycle Hooks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXj/zero-downtime-migration-of-monolith-to-k8s-using-sidecar-and-container-lifecycle-hooks-deepak-kosaraju-james-dabbs-procore
- YouTube search: https://www.youtube.com/results?search_query=Zero+Downtime+Migration+of+Monolith+To+K8s+Using+Sidecar+and+Container+Lifecycle+Hooks+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jR6Oex3wFCE
- YouTube title: Zero Downtime Migration of Monolith To K8s Using Sidecar and Contai... Deepak Kosaraju & James Dabbs
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/zero-downtime-migration-of-monolith-to-k8s-using-sidecar-and-container/jR6Oex3wFCE.txt
- Transcript chars: 31935
- Keywords: traffic, deploy, container, envoy, connections, pre-top, scaling, version, customers, running, platform, application, routing, ensure, seconds, started, changes, legacy

### Resumo baseado na transcript

Uh, and we are here today to tell you a little bit about uh our journey to Kubernetes, the potholes we hit along the way, and some that we swerve to avoid. Um, I'll give you a quick bit of background, kind of where we started from, how we started on our journey. Uh we have like 90-ish teams working in the ecosystem and and our contract to them is that we will deploy as continuously as we reasonably can given the scale of that artifact and and kind of complexities there which works out to about nine deploys a day. I I think if you dig a little bit deeper, a lot of our problems stemmed from it was hard to change things. It it felt like moving this onto a solid foundation Kubernetes could be a real win for us. Um if you kind of squint at the architecture diagram, you can see something that sort of looks like a pawn, right?

### Excerpt da transcript

Hey y'all. >> Uh, welcome. It's good to see you all. Thanks for hanging out at the end of the day. It is nice to see your faces. Um, I'm James. >> I'm Debbuck. Uh, and we are here today to tell you a little bit about uh our journey to Kubernetes, the potholes we hit along the way, and some that we swerve to avoid. Um, I'll give you a quick bit of background, kind of where we started from, how we started on our journey. Uh, Deepo's going to walk you through the tools we had on hand and how we deployed them to solve some of the challenges we had. And we'll close with a demo that you can kind of take home, kick the tires on, twiddle some knobs, get a feel for the sorts of configurations we're talking about here today. Uh, a little bit of background. We work at Procore. Procore aims to build the software that builds the world. Um, our customers range from small subs to enterprise GCS building buildings a lot like this one. Um, we work primarily on Cornerstone, which is our legacy Rails application from the the dawn of time.

It predates GitHub, so literally is prehistorical as far as I'm concerned. Um these days we have a large kind of constellation of microservices around it but like cornerstone is still a kind of core to the product. Uh we have like 90-ish teams working in the ecosystem and and our contract to them is that we will deploy as continuously as we reasonably can given the scale of that artifact and and kind of complexities there which works out to about nine deploys a day. Um it's an interestingly heterogeneous workload. Uh, you know, we've got weird wonky reporting queries that take two minutes served out of the production database for reasons best described as legacy software. It is a legacy system. Uh, and I say that with love. I love software that has a legacy. You know, um, I think I'm paraphrasing a quote here, but for you to get this story, it's important for you to understand some of the specific ways that our monolith was unhappy. If you have a legacy system, yours is probably different, and there's no substitute for spending some time thinking about that.

But we're going to tell you about ours. Um, before we got started working, we were running on autoscaling groups. And, and I say autoscaling extremely loosely here. The only scaling we did was at deploy time when we had a new code version. We would spin up new nodes with new code version. We wait for 80% to be ready. We would hard cut traffic, keep the offside warm for a time, let tho
