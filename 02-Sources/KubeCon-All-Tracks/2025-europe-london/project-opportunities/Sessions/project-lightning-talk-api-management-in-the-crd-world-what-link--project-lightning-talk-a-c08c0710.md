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
themes: ["Community Governance"]
speakers: ["Phil Henderson", "Contributor"]
sched_url: https://kccnceu2025.sched.com/event/1tcvH/project-lightning-talk-api-management-in-the-crd-world-what-linkerd-has-learned-phil-henderson-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+API+Management+in+the+CRD+World%3A+What+Linkerd+Has+Learned+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: API Management in the CRD World: What Linkerd Has Learned - Phil Henderson, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Phil Henderson, Contributor
- Schedule: https://kccnceu2025.sched.com/event/1tcvH/project-lightning-talk-api-management-in-the-crd-world-what-linkerd-has-learned-phil-henderson-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+API+Management+in+the+CRD+World%3A+What+Linkerd+Has+Learned+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: API Management in the CRD World: What Linkerd Has Learned.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvH/project-lightning-talk-api-management-in-the-crd-world-what-linkerd-has-learned-phil-henderson-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+API+Management+in+the+CRD+World%3A+What+Linkerd+Has+Learned+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5CyAZBUH1f8
- YouTube title: Project Lightning Talk: API Management in the CRD World: What Linkerd Has Learned - Phil Henderson
- Match score: 0.993
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-api-management-in-the-crd-world-what-linkerd-ha/5CyAZBUH1f8.txt
- Transcript chars: 9110
- Keywords: mesh, linkerd, learned, simple, anyone, everyone, program, mentees, shared, review, management, created, mostly, question, overboard, application, install, humans

### Resumo baseado na transcript

Today I'm going to be talking about API management in the CRD world and what Linkerd has learned. Uh other than that, I'm in a you won't be able to find me on the internet. So when we start developing things the first question we ask is how is this going to affect people from developers to SR and anyone between again we use CRDs Kubernetes encourage CRDs but it's really hard to get a new API in the core of Kubernetes has anyone has anyone done it anyone tried any maintainers here doing that ah there's one there see very difficult we only have one in the crowd of of 300 people 400 people Um, it's really easy to add CRDs though and we Um, so lesson learned is it can we got to be very very careful what we ship as an API. It causes problems in the long term when we have multiple projects using one like gateway API.

### Excerpt da transcript

My name is Phil Henderson. I'm a customer success engineer at Buoyant. Today I'm going to be talking about API management in the CRD world and what Linkerd has learned. Again, my name is Phil Henderson. Uh I usually there's social media stuff on this page. I don't have any social media, so you cannot find me. You can find me on GitHub and any of the CNCF Slacks at Phil. Uh other than that, I'm in a you won't be able to find me on the internet. What What is linkerd? Linkerd is a service mesh. You've already been told what a service mesh is today, but what you may not have known is linkerd was the first service mesh. We're the ones who created the word service mesh. And what we do is bring security, reliability, and observability to your workloads in that order. No exceptions. Uh all in an ultra light package developed in Rust. Again, what other regardless of what other ones may tell you, linking is still the easiest to use and most secure service mesh out there. It just works. Zero config. You add an annotation to your namespace and everything's meshed.

It's ultra light. It's simple and it's secure by default with MTLS. Um, you can look up all the the statistics on online. You see our our uh control plane, our data plane take a very minimum footprint and again because it's based on Rust. But regardless of that, today I'm here to talk about how we manage CRDs in the API management world. We use CRDs. Most people use CRDs. Kubernetes as a whole encourages CRDs. Kubernetes is not helping us as a whole with CRDs though. Um, we use shared CRDs. This is mostly in the gateway API project right now, but this is just the beginning. We'll see more in the future. And we try really hard to keep our CRDs simple. One of the main goals of linkerd is to keep things simple. So when we start developing things the first question we ask is how is this going to affect people from developers to SR and anyone between again we use CRDs Kubernetes encourage CRDs but it's really hard to get a new API in the core of Kubernetes has anyone has anyone done it anyone tried any maintainers here doing that ah there's one there see very difficult we only have one in the crowd of of 300 people 400 people Um, it's really easy to add CRDs though and we can go overboard.

Who's who's created their own operator and CRDs in here? Who has gone overboard with their CRDs? Or who admit that they've gone overboard with their CDs, I may say, right? You know, yeah. Um, it can be unpleasant, right? Vers
