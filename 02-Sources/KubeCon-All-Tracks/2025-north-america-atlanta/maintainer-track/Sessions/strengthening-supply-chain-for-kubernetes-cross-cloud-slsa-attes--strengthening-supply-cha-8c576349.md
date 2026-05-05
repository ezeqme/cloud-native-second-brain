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
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Feynman Zhou", "Microsoft", "Dahu Kuang", "Alibaba Cloud"]
sched_url: https://kccncna2025.sched.com/event/27NlO/strengthening-supply-chain-for-kubernetes-cross-cloud-slsa-attestation-verification-feynman-zhou-microsoft-dahu-kuang-alibaba-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Strengthening+Supply+Chain+for+Kubernetes%3A+Cross-Cloud+SLSA+Attestation+Verification+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Strengthening Supply Chain for Kubernetes: Cross-Cloud SLSA Attestation Verification - Feynman Zhou, Microsoft & Dahu Kuang, Alibaba Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Feynman Zhou, Microsoft, Dahu Kuang, Alibaba Cloud
- Schedule: https://kccncna2025.sched.com/event/27NlO/strengthening-supply-chain-for-kubernetes-cross-cloud-slsa-attestation-verification-feynman-zhou-microsoft-dahu-kuang-alibaba-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Strengthening+Supply+Chain+for+Kubernetes%3A+Cross-Cloud+SLSA+Attestation+Verification+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Strengthening Supply Chain for Kubernetes: Cross-Cloud SLSA Attestation Verification.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NlO/strengthening-supply-chain-for-kubernetes-cross-cloud-slsa-attestation-verification-feynman-zhou-microsoft-dahu-kuang-alibaba-cloud
- YouTube search: https://www.youtube.com/results?search_query=Strengthening+Supply+Chain+for+Kubernetes%3A+Cross-Cloud+SLSA+Attestation+Verification+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=no3Hg6u80YE
- YouTube title: Strengthening Supply Chain for Kubernetes: Cross-Cloud SLSA Attestation... Feynman Zhou & Dahu Kuang
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/strengthening-supply-chain-for-kubernetes-cross-cloud-slsa-attestation/no3Hg6u80YE.txt
- Transcript chars: 22602
- Keywords: source, ratify, security, supply, cluster, images, container, framework, deployed, deploy, admission, notary, github, compliant, attestation, software, environment, commit

### Resumo baseado na transcript

I'm currently a product manager working for Microsoft Azure and I'm also maintainer of CNCF notary project and rify project. I come from Alibaba cloud and I'm focus on the container security and I'm also a contributor for notary project. And uh could you please also let your team apply the security uh system and controls to your development life cycle and work workflow and pipelines? Hey Fman, our detector scan there's a five critical vulnerabilities and instance in your product environment and running image that's very risky I thought you have said you have deployed this security control in your environment is that right yes we did we actually we Um to be honest we only validate the supply chain metadata like signatures and as spawn when we download software from GitHub and from docker hub but when our customers when they deploy their images and AI workloads to container to their kubernetes clusters I But the hard thing is when you try to validate those images and enforce only trusted images and workloads can be deployed to your Kubernetes cluster to your production environment.

### Excerpt da transcript

All right, good afternoon everybody. I'm Feman. I'm currently a product manager working for Microsoft Azure and I'm also maintainer of CNCF notary project and rify project. I have my co-speaker Dahu from Alibaba cloud. Hello everyone, I am Dahu. I come from Alibaba cloud and I'm focus on the container security and I'm also a contributor for notary project. >> All right. I actually brought some very nice beanies, our project swags for everybody who have questions after our speech. Also, I think the room is relatively large and empty. So, if you want to sit in front of and get closer to our screen to the stage, that'll be super appreciated. All right. Today we're gonna share the real world problems and the challenges in software supply chain and we will introduce open source projects and framework like salsa rify notary project. We'll use these projects to demonstrate how to secure Kubernetes deployment and AI workloads in the real world examples and DAP will also demonstrate how to deploy a trusted AI workloads to Kubernetes cluster with sala framework and ratify.

All right, I believe most of you have security teams in your companies, right? And uh those security guys have been really annoying because they constantly ask you to follow in their security best practice and guidance. So in my company I have a security manager Dahu. Hey Dahoo. Hey there is some security best practice and checklist in our company. Could you please let your team obey this checklist? >> Let me take a look. All right, this is a good guidance. It's a long list. I will definitely bring this to our team and make sure our team to follow the best practice. Let's take that. Great. And uh could you please also let your team apply the security uh system and controls to your development life cycle and work workflow and pipelines? Yes. Um I will definitely bring this to our team's meeting and uh I want to make things really actionable in our daily development development life cycle. I will emphasize this in our team's meeting. Don't worry bro, trust us. Trust me. >> Okay, I will trust you for so actually our dependencies and software are acquired from GitHub.

You know the largest open source software in the world, right? So everything on GitHub, they are open source, they are transparent. So trust us. Hey Fman, our detector scan there's a five critical vulnerabilities and instance in your product environment and running image that's very risky I thought you have said you have deployed this
