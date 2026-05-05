---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Kostis Kapelonis", "Octopus Deploy", "Alexandre Gaudreault", "Intuit"]
sched_url: https://kccncna2025.sched.com/event/27Nnl/supercharge-your-canary-deployments-with-argo-rollouts-step-plugins-kostis-kapelonis-octopus-deploy-alexandre-gaudreault-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Supercharge+Your+Canary+Deployments+With+Argo+Rollouts+Step+Plugins+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Supercharge Your Canary Deployments With Argo Rollouts Step Plugins - Kostis Kapelonis, Octopus Deploy & Alexandre Gaudreault, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Kostis Kapelonis, Octopus Deploy, Alexandre Gaudreault, Intuit
- Schedule: https://kccncna2025.sched.com/event/27Nnl/supercharge-your-canary-deployments-with-argo-rollouts-step-plugins-kostis-kapelonis-octopus-deploy-alexandre-gaudreault-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Supercharge+Your+Canary+Deployments+With+Argo+Rollouts+Step+Plugins+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Supercharge Your Canary Deployments With Argo Rollouts Step Plugins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nnl/supercharge-your-canary-deployments-with-argo-rollouts-step-plugins-kostis-kapelonis-octopus-deploy-alexandre-gaudreault-intuit
- YouTube search: https://www.youtube.com/results?search_query=Supercharge+Your+Canary+Deployments+With+Argo+Rollouts+Step+Plugins+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=b2yYR9ARNaE
- YouTube title: Supercharge Your Canary Deployments With Argo Rollouts St... Kostis Kapelonis & Alexandre Gaudreault
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/supercharge-your-canary-deployments-with-argo-rollouts-step-plugins/b2yYR9ARNaE.txt
- Transcript chars: 21977
- Keywords: argo, plug-in, rollout, canary, version, traffic, plugins, deployment, plugin, controller, metrics, method, deployments, rollouts, create, mechanism, integrate, progressive

### Resumo baseado na transcript

Uh today we're going to talk about a new feature that came out uh with Argo rollout one version 1.8 and it's the ability to create custom canary step with the help of of a new plug-in system. I'm also an Argo CD maintainer and a partial contributor on Argo rollout and with me is Kostas. So this is progressive delivery in general and then uh this is how you do it with Kubernetes. So, Argo is a Kubernetes controller for uh doing progressive delivery in Kubernetes and it supports those scenarios I explained blue green deployments and canary deployments but you can also do other things with it like u experiments AB testing and several other things that you need to check out the documentation. It's running inside Kubernetes and just to make it clear it's a self-contained project. So once you install Argo rollouts in your cluster, you gain access to a new Kubernetes resource which is called a rollout.

### Excerpt da transcript

Hello everyone and thanks for joining us our session. Uh today we're going to talk about a new feature that came out uh with Argo rollout one version 1.8 and it's the ability to create custom canary step with the help of of a new plug-in system. So first things first, my name is Alexandro. I'm a staff software engineer at Inuit. I'm also an Argo CD maintainer and a partial contributor on Argo rollout and with me is Kostas. >> Hello, my name is Costis. I'm working as a developer advocate at Octopus deploy and I'm also a member of the Argo team. >> So in today's presentation, we'll first explain uh what is Argo rollout for the people that are not familiar with it and what's the status of the open source project. uh then we'll explain the different mechanism that exist in Argo rollout today to extend its functionalities and integrate with your infrastructure during your deployments. Uh after that we'll get down to our main topic the step plugins and we'll explain the different use cases uh that are solved with Canary step plugin how you can write your own and uh that's it on that note I'll give the floor to Kostas to talk more about progressive delivery so Algor is a controller for progressive delivery so let's define this first just to make sure that everybody's on the same page progressive delivery is a set of advanced deployment deployments where instead of sending the new version straight away to production, you do something smarter.

So in the case of blue green deployments on the left, you create a new version, but you do not send any traffic to it just yet. Then you can test it, make sure that it works, and then when you are confident, you switch the traffic to it. In the case of Canaris which is on the right, you do a similar thing but instead of having a single point in time where you do the switch, you instead gradually send more traffic to the new version as you gain more confidence. So you start let's say with 10% then 20% and so on and so on. So this is progressive delivery in general and then uh this is how you do it with Kubernetes. So we are working with replica sets. So whenever we use blue green we start a second replica set that defines a new version but all the traffic still goes to the old replica set and once we are confident we make the switch and in the case of canaris um we do this in a gradual way. So we use a traffic manager where we send let's say uh 25% of the new version then 50% then 100% and once we are ready we destroy the pre
