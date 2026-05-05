---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["AI ML", "Security", "GitOps Delivery"]
speakers: ["Yuji Watanabe", "Hirokuni Kitahara", "IBM Research"]
sched_url: https://kccncna2022.sched.com/event/182HF/trust-but-verify-bringing-supply-chain-integrity-to-cd-gitops-yuji-watanabe-hirokuni-kitahara-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=Trust+But+Verify%3A+Bringing+Supply+Chain+Integrity+To+CD+GitOps+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Trust But Verify: Bringing Supply Chain Integrity To CD GitOps - Yuji Watanabe & Hirokuni Kitahara, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Security]], [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Yuji Watanabe, Hirokuni Kitahara, IBM Research
- Schedule: https://kccncna2022.sched.com/event/182HF/trust-but-verify-bringing-supply-chain-integrity-to-cd-gitops-yuji-watanabe-hirokuni-kitahara-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=Trust+But+Verify%3A+Bringing+Supply+Chain+Integrity+To+CD+GitOps+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Trust But Verify: Bringing Supply Chain Integrity To CD GitOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HF/trust-but-verify-bringing-supply-chain-integrity-to-cd-gitops-yuji-watanabe-hirokuni-kitahara-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=Trust+But+Verify%3A+Bringing+Supply+Chain+Integrity+To+CD+GitOps+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dcCbtYrbjzE
- YouTube title: Trust But Verify: Bringing Supply Chain Integrity To CD GitOps - Yuji Watanabe & Hirokuni Kitahara
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/trust-but-verify-bringing-supply-chain-integrity-to-cd-gitops/dcCbtYrbjzE.txt
- Transcript chars: 21454
- Keywords: manifest, signature, source, application, interest, cluster, admission, material, target, repository, change, actually, signing, resource, verification, verify, control, controller

### Resumo baseado na transcript

uh today uh we will talk about the uh against the software supply chain topic but the unique things about this session is we are through Enterprises safe and use software supply chain security Integrity to the specifically in the CD kit of scenario so we will discuss the issue and the proposed solution to this from IBM research I'm a senior technical staff member and I'm leading the several software supply chain security project in the research so and you know yes I am hero kitahara from idea okay

### Excerpt da transcript

uh today uh we will talk about the uh against the software supply chain topic but the unique things about this session is we are through Enterprises safe and use software supply chain security Integrity to the specifically in the CD kit of scenario so we will discuss the issue and the proposed solution to this from IBM research I'm a senior technical staff member and I'm leading the several software supply chain security project in the research so and you know yes I am hero kitahara from idea okay so I okay I'm here and from I'm in research Tokyo and I'm I'm working on CD githubs are everywhere and I'm doing several OSS contributions like Secret store or today's main topic rocd yep thank you so much okay so today the the first uh I will talk about the background of this topic and then the what we are trying to discuss in this story in this talk then we will explain the several building blocks the Yemen manifest signature and its enforcement so then discussed how we we just how can we apply the technology to the CD guitars and we found we just point out some similar issues and talk about the proposed solution called interest then uh hero will do the demo okay so the first supply chain is a product so the protecting the product from The Source they are sourced and it's built at the factory and go to the up each package then become the product so but from the end user perspectives we need more protection like it should be securely delivered and it should be securely painted and at before actually the protect it should be protected at the time of the use so the whole this end to end is at the scope of the uh protection from the user perspective when we think about the same things in the uh application deployment in the coordinative case the very high level right picture the fastest source is in iterable it comes it goes to the CI Pi Prime then we use the image and push it to the registry and manifest is created at this git report then the when the deploy the application the image goes to the cluster manifest to go to the cluster by your CD pipeline then application is stand up to the cluster so this is a kind of the end-to-end from the source to the actual the time of the use so what is the risk so the maybe some case uh image on the registry maybe the Target and manifest on the gate Ripple is also the target so under the even after the deployment the Manifest is on the cluster so that it may be changed by some someone so those uh uh attack and measures activi
