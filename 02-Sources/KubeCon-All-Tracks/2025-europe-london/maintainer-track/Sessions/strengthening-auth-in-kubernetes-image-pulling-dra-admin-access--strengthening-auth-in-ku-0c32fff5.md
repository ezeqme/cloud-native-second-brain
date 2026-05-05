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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Rita Zhang", "Stanislav Láznička", "Microsoft"]
sched_url: https://kccnceu2025.sched.com/event/1tczC/strengthening-auth-in-kubernetes-image-pulling-dra-admin-access-pod-certificates-rita-zhang-stanislav-laznicka-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Strengthening+Auth+in+Kubernetes%3A+Image+Pulling%2C+DRA+Admin+Access+%26+Pod+Certificates+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Strengthening Auth in Kubernetes: Image Pulling, DRA Admin Access & Pod Certificates - Rita Zhang & Stanislav Láznička, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Rita Zhang, Stanislav Láznička, Microsoft
- Schedule: https://kccnceu2025.sched.com/event/1tczC/strengthening-auth-in-kubernetes-image-pulling-dra-admin-access-pod-certificates-rita-zhang-stanislav-laznicka-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Strengthening+Auth+in+Kubernetes%3A+Image+Pulling%2C+DRA+Admin+Access+%26+Pod+Certificates+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Strengthening Auth in Kubernetes: Image Pulling, DRA Admin Access & Pod Certificates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczC/strengthening-auth-in-kubernetes-image-pulling-dra-admin-access-pod-certificates-rita-zhang-stanislav-laznicka-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Strengthening+Auth+in+Kubernetes%3A+Image+Pulling%2C+DRA+Admin+Access+%26+Pod+Certificates+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rVz-vIFGT4k
- YouTube title: Strengthening Auth in Kubernetes: Image Pulling, DRA Admin Acces... Rita Zhang & Stanislav Láznička
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/strengthening-auth-in-kubernetes-image-pulling-dra-admin-access-pod-ce/rVz-vIFGT4k.txt
- Transcript chars: 24350
- Keywords: feature, actually, basically, cluster, resource, access, server, request, specific, bundle, secret, create, account, cublet, another, features, object, eventually

### Resumo baseado na transcript

Uh today we will talk about some of the updates from SIG O uh both for a and authorization. Um and we will touch on upon a lot of features that are coming in uh v133 that's coming out in a couple of weeks and then we will talk about some new features uh that are planned for future releases. just want to add to here started the original design and stand made it possible to move to beta in 133. Uh, so you may know that UIDs in and in Kubernetes clusters maybe don't seem as important, but UIDs are actually quite or maybe important in in some external systems, right? Not only because I got to work on it, but you know this this is a feature that actually will eventually when it reaches G it should uh improve the security stance of Kubernetes by default. from the critical path when uh you know so so when when previously you would have to use the always put policy and you would always have to query it.

### Excerpt da transcript

Hi everyone, thank you for being in the session. Uh today we will talk about some of the updates from SIG O uh both for a and authorization. Um and we will touch on upon a lot of features that are coming in uh v133 that's coming out in a couple of weeks and then we will talk about some new features uh that are planned for future releases. My name is Rita. Uh I'm an engineer at Microsoft. I'm also a SEO co-chair. I am. I'm also an engineer in Microsoft and well I do all things well all things contributions in sego. That's true. Um and throughout the slide uh we will also be mentioning contributors who are contributing to all the different features um because uh none of this would be possible without the contributors. So let's start with the graduated features uh bound um service account token improvements. This is a a kept an enhancement that has been uh done by Mo, James and Jordan for the past few releases and it's going to GA in 133. Um so what is this feature? Right. So in the past when attempting to verify a service account token associated with a pod, it was very it wasn't possible to verify the pod associated to a specific node.

um you would have to do a lot to get the relevant pod um get the pod object from the private claim in the drop token and cross referencing that to find the specific node name. Um, this feature actually allows us to uh have a robust chain of identifi identity verification all the way from the requester to um the projected token and and we want to get the no object reference in the requested pod where it's embedded in the sign jot. This feature um incorporates additional claims like the node name uh and JTI in the token itself so that we can do this traceability and prevent any replay attacks. Uh cluster trust bundles. So uh this feature uh makes it really easy for you to install and maintain an additional trust in your cluster. Right? So previously if you wanted to add a trusted signer into your cluster you would probably have to juggle a lot of config maps around and with the rotation those those were some some nightmares out there and so we've got these cluster trust bundles which basically with which basically you define uh your serer your trusted serer as an API object and then in your ports you you just mount uh the trust uh the trust TR bundle of that trusted object of trusted signer into your pots.

Yi projected volume. U so uh yeah you know one of the showcases here was uh a ser for the QPS server that I was actually
