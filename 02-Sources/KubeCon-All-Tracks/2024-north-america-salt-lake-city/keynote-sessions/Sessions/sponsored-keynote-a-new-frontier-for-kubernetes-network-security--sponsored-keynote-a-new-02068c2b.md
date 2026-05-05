---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Keynote Sessions"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Idit Levine", "Founder and CEO", "Solo.io", "Keith Babo", "VP of Product", "Solo.io"]
sched_url: https://kccncna2024.sched.com/event/1noNv/sponsored-keynote-a-new-frontier-for-kubernetes-network-security-idit-levine-founder-and-ceo-soloio-keith-babo-vp-of-product-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+A+New+Frontier+for+Kubernetes+Network+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sponsored Keynote: A New Frontier for Kubernetes Network Security - Idit Levine, Founder and CEO, Solo.io & Keith Babo, VP of Product, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Idit Levine, Founder and CEO, Solo.io, Keith Babo, VP of Product, Solo.io
- Schedule: https://kccncna2024.sched.com/event/1noNv/sponsored-keynote-a-new-frontier-for-kubernetes-network-security-idit-levine-founder-and-ceo-soloio-keith-babo-vp-of-product-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+A+New+Frontier+for+Kubernetes+Network+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: A New Frontier for Kubernetes Network Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1noNv/sponsored-keynote-a-new-frontier-for-kubernetes-network-security-idit-levine-founder-and-ceo-soloio-keith-babo-vp-of-product-soloio
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+A+New+Frontier+for+Kubernetes+Network+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=psZi_T1np4U
- YouTube title: Sponsored Keynote: A New Frontier for Kubernetes Network Security- Idit Levine & Keith Babo, Solo.io
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sponsored-keynote-a-new-frontier-for-kubernetes-network-security/psZi_T1np4U.txt
- Transcript chars: 8070
- Keywords: gateway, actually, security, ingress, features, egress, traffic, mesh, implementation, envoy, gateways, running, pattern, production, important, talked, standard, existing

### Resumo baseado na transcript

hello cucon D and I are super excited to be here today to talk to you about a new frontier for kubernetes network security uh before we talk about New Frontiers though let's talk a little bit about the existing landscape for kubernetes security as long as there has been kubernetes there has been Ingress but Ingress has emerged as more than just getting traffic into the cluster Ingress gateways have become the go-to mechanism for implementing security observability and advanced routing into workloads running in your kubernetes cluster the

### Excerpt da transcript

hello cucon D and I are super excited to be here today to talk to you about a new frontier for kubernetes network security uh before we talk about New Frontiers though let's talk a little bit about the existing landscape for kubernetes security as long as there has been kubernetes there has been Ingress but Ingress has emerged as more than just getting traffic into the cluster Ingress gateways have become the go-to mechanism for implementing security observability and advanced routing into workloads running in your kubernetes cluster the community loved this approach so much that we said hey let's grab that Gateway that's so awesome at north south and I want that for servic to service interactions as well so let's bring that Gateway into the eastwest traffic plane and put it in a side car and that became service mesh thousands of organizations have been successful implementing the service mesh pattern but that has not been without challenges from a ux and resource consumption perspective so if we look at healthy and vibrant projects in this ecosystem they're constantly evolving and innovating and the iso project did exactly that creating a sidecar lless architecture that brings L4 security observability and routing to every workload in kubernetes without the need for a sidecar and this works great for L4 traffic but L7 is a whole another ball game right so security scalability L7 feature sets all require a Gateway but we don't need a side car for that what we need is the ability to dynamically provision individual micro gateways in the east west traffic plane only for services that require L7 features and this entire Vision coming to reality in mbn mesh where solo and Google force and quick created MN mesh and push the implementation Upstream to the sto Community with ambient you are getting the entire feature of esta but way simpler way and to adopt and and also less overhead an ambient is not an idea anymore it's reality it's here it's real a g and we actually have quite a lot of user running it in production today and even more important the reviews are stunning in order to make it extremely easy for all of you to adopt ambn we created a community website there you can find everything you need all the way from getting started to prod action I really really recommend you to check it out all right and if you want to hear more about the Journey of the iso Community from its very Beginnings to ambient mesh going GA Christian and Louie have an amazing talk t
