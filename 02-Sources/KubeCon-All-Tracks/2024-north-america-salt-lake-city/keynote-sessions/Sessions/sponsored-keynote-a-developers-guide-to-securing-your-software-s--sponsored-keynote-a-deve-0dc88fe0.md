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
themes: ["AI ML", "Security"]
speakers: ["Toddy Mladenov", "Principal Product Manager", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1iCSh/sponsored-keynote-a-developers-guide-to-securing-your-software-supply-chain-toddy-mladenov-principal-product-manager-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+A+Developer%E2%80%99s+Guide+to+Securing+Your+Software+Supply+Chain+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sponsored Keynote: A Developer’s Guide to Securing Your Software Supply Chain - Toddy Mladenov, Principal Product Manager, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Toddy Mladenov, Principal Product Manager, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1iCSh/sponsored-keynote-a-developers-guide-to-securing-your-software-supply-chain-toddy-mladenov-principal-product-manager-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+A+Developer%E2%80%99s+Guide+to+Securing+Your+Software+Supply+Chain+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: A Developer’s Guide to Securing Your Software Supply Chain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iCSh/sponsored-keynote-a-developers-guide-to-securing-your-software-supply-chain-toddy-mladenov-principal-product-manager-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+A+Developer%E2%80%99s+Guide+to+Securing+Your+Software+Supply+Chain+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YQuzhSGGPNk
- YouTube title: Sponsored Keynote: A Developer’s Guide to Securing Your Software Supply Chain - Toddy Mladenov
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sponsored-keynote-a-developers-guide-to-securing-your-software-supply/YQuzhSGGPNk.txt
- Transcript chars: 5171
- Keywords: supply, software, images, microsoft, secure, application, development, compliant, follow, security, deploy, clusters, stages, process, container, projects, observability, securing

### Resumo baseado na transcript

hello cucon it's great to be here and also I'm honored to be part of this amazing lineup of Keynotes once again my name is Tod marov and at Microsoft I lead the initiative to secure the supply chain for all Cloud native work worlds it's a fascinating topic and I'm very honored actually to be here and present it to you so let's dive in if you follow the cyber security news you have seen those articles those are just a few of the most prominent software supply chain

### Excerpt da transcript

hello cucon it's great to be here and also I'm honored to be part of this amazing lineup of Keynotes once again my name is Tod marov and at Microsoft I lead the initiative to secure the supply chain for all Cloud native work worlds it's a fascinating topic and I'm very honored actually to be here and present it to you so let's dive in if you follow the cyber security news you have seen those articles those are just a few of the most prominent software supply chain attacks that happen in the past few years while many are still financially motivated the highlighted ones are with most nefarious goals the question we need to ask ourselves is why do Bad actors think such attacks will succeed let's look at the steps we as developers take to get our application from source to production today we go to Registries like dockerhub and find images we go to public package managers and choose library to help us with our development but we end up with this images and libraries that we have absolutely no control over are included in our builds even worse we deploy them directly to our our production clusters this is what the Bad actors want us to do but we can make it harder for them we at Microsoft look at the software supply chain in different stages the first one is to acquire bits and pieces that help us speed up our development process those can be software from op Source can be vendor sdks can be even internal binaries but before we acquire those we need to make sure that they come from trusted sources using signing Technologies like notary project and Sixt allow us to verify the authenticity and integrity of any software supply chain artifact but our signatures enough identities can be compromised that is why we should build an internal catalog of approved artifacts and not allow random pools from the internet using oci compliant Registries like Azure container registry allow us to do much more than just storing container images we can store any supply chain artifact we want but more importantly we cannot metadata to drive our supply chain workflows for example we at Microsoft we annotate container images with end of life metadata and we don't allow those images to be used if they are outdated we can also scan images for vulnerabilities in malware or generate s bombs we can even use project coopa to patch images daily while waiting for the Upstream projects to provide updates now it is time to build our application and put all the pieces together but building the b
