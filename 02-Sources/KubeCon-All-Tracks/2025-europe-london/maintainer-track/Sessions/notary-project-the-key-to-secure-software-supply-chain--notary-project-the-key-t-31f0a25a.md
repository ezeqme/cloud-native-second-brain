---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Yi Zha", "Microsoft", "Guillaume Gill", "OrangeLogic"]
sched_url: https://kccnceu2025.sched.com/event/1td1W/notary-project-the-key-to-secure-software-supply-chain-yi-zha-microsoft-guillaume-gill-orangelogic
youtube_search_url: https://www.youtube.com/results?search_query=Notary+Project%3A+The+Key+To+Secure+Software+Supply+Chain+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Notary Project: The Key To Secure Software Supply Chain - Yi Zha, Microsoft & Guillaume Gill, OrangeLogic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Yi Zha, Microsoft, Guillaume Gill, OrangeLogic
- Schedule: https://kccnceu2025.sched.com/event/1td1W/notary-project-the-key-to-secure-software-supply-chain-yi-zha-microsoft-guillaume-gill-orangelogic
- Busca YouTube: https://www.youtube.com/results?search_query=Notary+Project%3A+The+Key+To+Secure+Software+Supply+Chain+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Notary Project: The Key To Secure Software Supply Chain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td1W/notary-project-the-key-to-secure-software-supply-chain-yi-zha-microsoft-guillaume-gill-orangelogic
- YouTube search: https://www.youtube.com/results?search_query=Notary+Project%3A+The+Key+To+Secure+Software+Supply+Chain+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1FwE0ajODU8
- YouTube title: Notary Project: The Key To Secure Software Supply Chain - Yi Zha & Guillaume Gill
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/notary-project-the-key-to-secure-software-supply-chain/1FwE0ajODU8.txt
- Transcript chars: 20281
- Keywords: signature, images, security, company, another, ensure, plug-in, notary, certificate, supply, support, notation, dependencies, verify, artifacts, application, mechanism, currently

### Resumo baseado na transcript

So hope everyone have discovered something interested um learned something new and made some new connections and especially having some fun. So currently I'm focusing on the cloud native security and the red tries and I'm Gil so the technical lead architect at onlogic and I'm leading the migration of the company to more cloud native solutions to modernize all the infrastructure and all the things since some years now. uh application images and you probably will also produce some other uh um security related image man metadata such as spawn for compl compliance purpose and also vulnerability reports. So for uh your application images and those uh uh security uh security related metadata you may also use not project tooling to sign so that later on you can validate the signature to ensure they are trust. So during deployment you can uh validate the notary project signatures and other uh and signatures of other uh um security metadata to ensure that the images can be trusted. So we try to modernize our infrastructure by being more cloud native and moving away from traditional installation to something based on Kubernetes with in the meantime more security.

### Excerpt da transcript

So hello everyone, welcome to the not project maintenance track. So today is the final day of CubeCon EU London uh this year. So hope everyone have discovered something interested um learned something new and made some new connections and especially having some fun. My name is E. I'm not a project maintainer. I'm also senior product manager at Microsoft. So currently I'm focusing on the cloud native security and the red tries and I'm Gil so the technical lead architect at onlogic and I'm leading the migration of the company to more cloud native solutions to modernize all the infrastructure and all the things since some years now. Okay. So uh it's very great to have J today as a co-speaker. He will share um his company's journey in software supply chain practice and also how not project can help to support this effort. So what is not project? So another project is uh incubating sab incubating project and it is in the cloud native security domain. So maybe some of you attended the uh uh the keynote today.

Uh there are some talk about the cyber attack resilience act this initiative. So not project definitely can provide the support from tuning perspective. uh not a project mainly answer two questions. The first one is as you see in the screen it is how I can trust the container images or other artifacts I used. How do I know they are from trusted source? This is about the authenticity. Another question is how can I make sure those artifacts are not modified by malicious users during publishing or distribution. So this is more about the integrity. So not project our mission is to ensure the authenticity and the integrity of cloud native uh artifacts by providing standard based solutions and tools. So a bit deep dive into the major scenario that not project that supports nowadays. uh you may see this uh diagram in the lighting talk. So this is actually a framework help you to understand how to address the uh supply uh uh supply chain issues in a systematic way. So starting from the left it is the acral stages.

So in this stages you normally across. So in this example uh there uh Bietnami is one of the major publisher in dog harp. So maybe you already know that. So Bidnami they uh sign they build sign and publish uh container images and hammer charts in dog harp and they sign with notary project signatures. And if you go to doc harbor and did a search you can find uh as a publisher they have a guide for consumer that it mentioned you can and use notation to va
